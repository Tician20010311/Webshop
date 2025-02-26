from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

def totals(request):
    cart = Cart(request)  # Kosár inicializálása
    return {'totals': cart.cart_total()}