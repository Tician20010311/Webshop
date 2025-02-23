from webshop_app.models import Termek

class Cart():
    def __init__(self, request):
        self.session = request.session
        #megszerzi a jelenlegi session kulcsot ha létezik
        cart = self.session.get('session_key')
        # Ha a felhasználó új , akkor nincs session kulcs ! Készít egyet ...
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self,product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'ár: ': str(product.ar) }
        self.session.modified = True 

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #ID -k megszerzése a kosárból 
        product_ids = self.cart.keys()
        products = Termek.objects.filter(id__in=product_ids)
        return products