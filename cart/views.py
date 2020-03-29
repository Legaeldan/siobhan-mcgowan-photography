from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from checkout.models import OrderLineItem
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@xframe_options_exempt
def add_to_cart(request, id):
    """Add a photo to the cart"""
    cart = request.session.get('cart', {})
    if id in cart:
        messages.error(request, "No Good! Item is already in cart!")
    else:
        cart[id] = cart.get(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

@xframe_options_exempt
def remove_from_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount.
    """
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))