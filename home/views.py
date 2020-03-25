import os
from django.shortcuts import render, redirect, get_object_or_404
from photos.models import Photo
from .models import Review
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import ContactForm

# Create your views here.
def index(request):
    """A view that displays the index page"""
    photos = Photo.objects.all()
    reviews = Review.objects.all()
    try:
        pre_banner = Photo.objects.filter(banner=True)
        for image in pre_banner:
            banner = get_object_or_404(Photo, pk=image.id)
        return render(request, "index.html", {"photos": photos, "reviews": reviews, "banner":banner})
    except:
        return render(request, "index.html", {"photos": photos, "reviews": reviews})
   
def contact(request):
    """A simple contact page for users to contact the photographer"""
    contact_form = ContactForm()
    if request.method == 'POST':
        subject = 'Thank you for contacting SMG Photography to our site'
        form_name = request.POST['user_name']
        form_message = request.POST['message']
        sender = request.POST['user_email']
        message = "Thank you %s for contact us here at SMG Photography." \
                  " " \
                  "We endeavor to contact everyone as soon as possible, and will be in touch shortly." \
                  " " \
                  "The message you sent was: %s from %s" % (form_name, form_message, sender)
        from_email = os.environ.get("EMAIL_MASTER_SENDER")
        recipient_list = [request.POST['user_email'], 'Legaeldan@gmail.com']
        print("Sending mail")
        email = EmailMessage(subject, message, from_email , recipient_list)
        email.send()
        messages.success(request, 'You message was sent successfully. We will be in touch shortly')
        
        return render(request, "contact.html", {"contact_form": contact_form})


    return render(request, "contact.html", {"contact_form": contact_form})