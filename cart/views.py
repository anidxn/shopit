from django.shortcuts import render
from django.shortcuts import get_object_or_404  # Get data from db

from .cart import Cart
from store.models import Product

from django.http import JsonResponse

# --------show cart summary.---------
def cart_summary(request):
    # Grab exiusting cart
    cart = Cart(request)
    cart_products = cart.get_prod_list
    cart_qnty = cart.get_prod_qntities   # prts {prodid : qnty} dictionary
    cart_total = cart.totalPrice()
    return render(request, 'cart_summary.html', {"cart_products" : cart_products, 'cart_qnty' : cart_qnty, 'cart_total' : cart_total})

# --------- add item to cart -------------
def cart_add(request):
    # a blank cart or get an existing cart
    mycart = Cart(request)

    #if request.POST.get('action') == 'post':
    if request.method == "POST":
        prodid  = int(request.POST['product_id'])
        qnty    = int(request.POST['product_qty'])

        # lookup for product..can't we use Product.objects.get(id =) ?? yes u can, but here its an ajax call so status code is required , so we are using this method
        sel_prod = get_object_or_404(Product, id = prodid)
        
        # save to session; here entire object is passed so that you may add whichever fields u want. not just product id
        mycart.add(added_product = sel_prod, prod_qty= qnty)

        # get the cart quantity...just to update the cart value in navbar
        cart_quantity = len(mycart)

        # return a JSON response
        response = JsonResponse({'qty' : cart_quantity})
        #response = JsonResponse({'Product name' : sel_prod.p_name})
        return response  # either this json response is returned or an error code is returned



def cart_update(request):
    # get the existing cart
    mycart = Cart(request)

    if request.method == "POST":
        prodid  = int(request.POST['product_id'])
        qnty    = int(request.POST['product_qty'])

        # update the quantity of the product id selected.
        mycart.updateCartQty(product_id = prodid, prod_qty= qnty)

        # -- calculate updated price & return --
        cart_total = mycart.totalPrice()
        
        cart_quantity = len(mycart)
        response = JsonResponse({'qty' : cart_quantity, 'cart_total' : cart_total})

        return response

    

def cart_delete(request):
    # get the existing cart
    mycart = Cart(request)

    #if request.POST.get('action') == 'post':
    if request.method == "POST":
        prodid  = int(request.POST['product_id'])

        # delete the item entry from session
        mycart.deleteItem(product_id = prodid)

        # -- calculate updated price & return --
        cart_total = mycart.totalPrice()

        #--- for now ----
        cart_quantity = len(mycart)

        response = JsonResponse({'qty' : cart_quantity, 'cart_total' : cart_total})

        return response


