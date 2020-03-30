from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from checkout.models import OrderLineItem, Order
from django.db.models import Q
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.

def logout(request):
    """
    A view that logs the user out and redirects back to the index page
    Add success message once logged out.
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """
    A view that manages the login form
    Returns a message to user on error or once logged in.
    """
    if request.user.is_authenticated():
        return redirect(reverse('profile'))
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()
        user_form.auto_id = False

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """
    A view that displays the profile page of a logged in user
    Displays all items pruchased by the user.
    """
    orders_line = OrderLineItem.objects.filter(Q(order__user_name__icontains=request.user))
    return render(request, 'profile.html', {"lines": orders_line})


def register(request):
    """
    A view that manages the registration form
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
        return redirect(reverse('index'))
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
