from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        # get the current session key if it exist
        cart = self.session.get("session_key")

        # if the user in new , no session key , create one
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # MAKE SURE cart work on all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_quantity)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # acceccing the the keys (product_id) in the cart dictionary -> self.cart[product_id] in line 20
        product_id = self.cart.keys()

        # get all products that have the id -> product_id
        products = Product.objects.filter(id__in=product_id)

        return products

    def get_quants(self):
        # acceccing the the keys (product_id) in the cart dictionary -> self.cart[product_id] in line 20
        quantities = self.cart

        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)

        ourcart = self.cart

        ourcart[product_id] = product_quantity

        self.session.modified = True

        thing = self.cart

        return thing

    def delete(self, product):
        product_id = str(product)
        # delete from  dict/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
