# a simple class file to contain our Beans class

from store.models import Product

class Cart:
    def __init__(self, request):  # request is required to get the current session
        self.session = request.session

        # get current session key if exists (for loged in user)
        cart = self.session.get('session_key')  # getting the session id

        # if the user is new, no session key exists; so create one !
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {} # set a session value
        
        # make sure that the cart is available on all pages of the site - help of Context Processor
        self.cart = cart

    #------------- add item to cart -------------
    def add(self, added_product, prod_qty):
        product_id = str(added_product.id)
        product_qnty = str(prod_qty)

        # if the product is already added
        if product_id in self.cart:
            pass    # don't do anything if already added
        else:
            # store item details in session
            # self.cart[product_id] = {'price' : str(added_product.p_price)}
            self.cart[product_id] = int(product_qnty)

            # Why don't we store the entire object??? => keep session light weight
        
        self.session.modified = True  #session object is modified due to addition of new data

    # ---- returns number of objects in cart ---
    def __len__(self):
        cartqty = self.cart
        quantities = 0
        for k in cartqty:
            quantities += cartqty[k]
        return quantities # len(self.cart)  gets count of particular item not exact quantity
    
    # ----- get the list of product objects -------
    def get_prod_list(self):
        # get the list of product ids
        prod_ids = self.cart.keys()  # product ids are stored as keys in the dict.

        products = Product.objects.filter(id__in = prod_ids)  # equivalent to "in (, , ) " in sql"

        return products
    
    # ---- getting all the quantities of items ------
    def get_prod_qntities(self):
        # cartqty = self.cart
        # quantities = 0
        # for k in cartqty:
        #     quantities += cartqty[k]

        quantities = self.cart   # gets the {'prod_id' : quantity}  list
        return quantities
    
   # ------ updating quantities in cart ----------
    def updateCartQty(self, product_id, prod_qty):
        product_id = str(product_id)
        prod_qty = int(prod_qty)

        # update dictionary
        self.cart[product_id] = prod_qty

        self.session.modified = True  # ???

    # ---- deleting an item from cart ------
    def deleteItem(self, product_id):
        product_id = str(product_id)

        # delete from cart using prodict id as key
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    # ----- getting total price of all items ----
    def totalPrice(self):
        prod_ids = self.cart.keys()  # product ids are stored as keys in the dict.

        # get products in cart
        products = Product.objects.filter(id__in = prod_ids)

        cost = 0
        for p in products:
            prc =  p.sale_price if p.is_on_sale else p.p_price
            cost += prc * self.cart[str(p.id)]
        
        return cost




