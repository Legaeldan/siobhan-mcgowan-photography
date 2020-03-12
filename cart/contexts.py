from django.shortcuts import get_object_or_404
from photos.models import Photo


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    print(total)
    for id, quantity in cart.items():
        photo = get_object_or_404(Photo, pk=id)
        total += photo.price
        cart_items.append({'id': id, 'photo': photo})
    
    return {'cart_items': cart_items, 'total': total}