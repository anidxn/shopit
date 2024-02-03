from django.shortcuts import redirect, render
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserRegisterForm

# Create your views here.

def home(request):
    prod_list = Product.objects.all()
    #pcat_list = Category.objects.all()
    return render(request, 'index.html', {'products': prod_list})

def product_detail(request, pk):
    selected_prod = Product.objects.get(id = pk)
    return render(request, 'product_detail.html', {'sel_product': selected_prod})

def product_by_cat(request, catname):
    # replace - with space '' to match with table data
    catname = catname.replace('-', ' ')

    # grab category by name
    print(Category.objects.all())
    try:
        catg = Category.objects.get(cat_name = catname)
        #print(catg)
        prod_list = Product.objects.filter(p_cat = catg)
        return render(request, 'product_by_category.html', {'products': prod_list, 'sel_category' : catname})
    except:
        messages.warning(request, 'That category '+ catname +' does not exist.')
        return redirect('home')

def aboutpage(request):
    return render(request, 'about.html')

#---------------------------------------------------
#           Authentication section
#---------------------------------------------------
def login_user(request):
    if request.method == "POST":
        uname = request.POST['txtUName']
        passwd = request.POST['txtPass']
        print(uname, ' == ', passwd )

        myuser = authenticate(request, username = uname, password = passwd) # model / table has columns named username & password

        if myuser is not None: # credentials found
            login(request, myuser)
            messages.success(request, 'Welcoome back - ' + myuser.username)
            return redirect('home')
            #return render(request, 'dashboard.html', {'emp_name': ename})
        else:
            messages.warning(request, "Bad credentials")
            return redirect('home')

    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully.")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        myform = UserRegisterForm(request.POST) 
        if myform.is_valid():  # validate the form
            myform.save()

            messages.success(request, "Registration successfull")
            # registration complete ..now sign in
            return redirect('login')
        else:
            #  * * * * * * * * error message handling * * * * * * * * * *
            for error in list(myform.errors.values()):
                messages.warning(request, error)
            return redirect('sign-up')
    # else:
    myform = UserRegisterForm()
    return render(request, 'register.html', {'form' : myform})


