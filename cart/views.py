from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants

    return render(
        request,
        "cart_summary.html",
        {"cart_products": cart_products, "quantities": quantities},
    )


def cart_add(request):
    # get the car
    cart = Cart(request)
    # test for post
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product, quantity=product_quantity)

        # Get cart quantity
        cart_quantity = cart.__len__()

        # retrun response
        response = JsonResponse({"qty": cart_quantity})
        return response


def cart_delete(request):
    cart=Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))

        # delete func in cart 
        cart.delete(product=product_id)

        response=JsonResponse({'product':product_id})

        return response



def cart_update(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

    cart.update(product=product_id, quantity=product_quantity)
    
    response = JsonResponse({"qty": product_quantity})
    
    return response
