CART_SESSION_ID = 'cart'
from stuff.models import Product


class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def add(self,product,quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = int(item['price'])*item['quantity']
            yield item


    def get_total_price(self):
        return sum(int(item['price'])*item['quantity'] for item in self.cart.values())
        
    def get_total_count(self):
        return sum(item['quantity'] for item in self.cart.values())    
    
    def get_count(self):
        return sum(1 for item in self.cart.values())  


    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()
