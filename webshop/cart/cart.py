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

    def add(self,product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'ár: ': str(product.ar) }
            self.cart[product_id] = int(product_qty)
        self.session.modified = True 

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #ID -k megszerzése a kosárból 
        product_ids = self.cart.keys()
        products = Termek.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        qantities = self.cart
        return qantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

		# Get cart
        ourcart = self.cart
		# Update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing