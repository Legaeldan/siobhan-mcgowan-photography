import os
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
from photos.models import Photo
import stripe
import requests
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user_name = request.user.username
            order.email = request.user.email
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                photo = get_object_or_404(Photo, pk=id)
                total += photo.price
                order_line_item = OrderLineItem(
                    order = order, 
                    photo = photo, 
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                subject = 'Thank you for your order SMG Photography to our site'
                message = "Thank you %s for your order with SMG Photography." \
                          " " \
                          "Please find attached your digital prints." % (request.user.username)
                from_email = os.environ.get('EMAIL_MASTER_SENDER')
                recipient_list = [request.user.email]
                print(request.user.email)
                email = EmailMessage(subject, message, from_email , recipient_list)
                for id, quantity in cart.items():
                    photo = get_object_or_404(Photo, pk=id)
                    response = requests.get(settings.MEDIA_URL+str(photo.image))                
                    print(photo.image)
                    email.attach(photo.name, response.content,mimetype="image/jpg")
                email.send()
                messages.success(request, "Congratulations! Your order completed successfully! You should recieve a mail containing your prints!")
                request.session['cart'] = {}


                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                
            