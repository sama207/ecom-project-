from .cart import Cart


# create context processor so the cart work on every page
def cart(request):
    # return defult data from cart
    return {"cart": Cart(request)}
