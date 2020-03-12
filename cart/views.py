from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a photo to the cart"""
    cart = request.session.get('cart', {})
    if id in cart:
        print("Item already in cart!")  
    else:
        cart[id] = cart.get(id) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount.
    """
    print(request.POST)
    cart = request.session.get('cart', {})
    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))