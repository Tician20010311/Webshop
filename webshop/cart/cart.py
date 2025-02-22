class Cart():
    def __init__(self, request):
        self.session = request.session
        #megszerzi a jelenlegi session kulcsot ha létezik
        cart = self.session.get('session_key')
        # Ha a felhasználó új , akkor nincs session kulcs ! Készít egyet ...
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart