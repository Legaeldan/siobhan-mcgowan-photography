from django.shortcuts import render, redirect
from photos.models import Photo
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    """A view that displays the index page"""
    photos = Photo.objects.all()
    return render(request, "index.html", {"photos": photos})

def contact(request):
    """A simple contact page for users to contact the photographer"""
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
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['user_email']]
        send_mail(subject, message, from_email , recipient_list)
        messages.success(request, 'You message was sent successfully. We will be in touch shortly')
        
        return redirect(reverse('contact'))


    return render(request, "contact.html")