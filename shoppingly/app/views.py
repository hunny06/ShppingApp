from django.shortcuts import render, redirect
from django.views import View
from .models import Product,Customer,Cart,OrderPlace
from .forms import CreateUserForm, CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    context_data = {}
    def get(self,request):
        cartitem = 0
        lower_data = Product.objects.filter(category = "B")
        top_data = Product.objects.filter(category = "T")
        mobile_data = Product.objects.filter(category = "M")
        laptop_data = Product.objects.filter(category = "L")
        if request.user.is_authenticated:
            cartitem = len(Cart.objects.filter(user = request.user))
        self.context_data = {"lower_data":lower_data,"top_data":top_data,"mobile_data":mobile_data,"laptop_data":laptop_data,"cartitem":cartitem}
        return render(request, 'app/home.html',self.context_data)

class ProductDetailView(View):
    context_data = {}
    def get(self, request, pk):
        cartitem = 0
        product = Product.objects.get(id = pk)
        if request.user.is_authenticated:
            cartitem = len(Cart.objects.filter(user = request.user))
        self.context_data = {"product":product,"cartitem":cartitem}
        return render(request, 'app/productdetail.html',self.context_data)

@login_required
def add_to_cart(request):
    if(request.GET.get('prod_id')):
        user = request.user
        product_id = Product.objects.get(id = request.GET.get('prod_id'))
        c = Cart.objects.filter(user =user, product = product_id)
        if(not c):
            Cart(user =user, product = product_id).save()
    return redirect('/cart')
    
def edit_product(request):
    if request.method == "GET":
        id = request.GET['id']
        cart = Cart.objects.filter(user = request.user)
        if request.GET['action'] == "add":
            cart_query = Cart.objects.get(Q(product = id) & Q(user = request.user))
            # cart = Cart.objects.filter(user = request.user)
            cart_query.quantity+=1
            cart_query.save()
            # context_data = {"quantity":cart_query.quantity,"amount":amount,"total_amount":total_amount,"type":request.GET['action']}
        if request.GET['action'] == "minus":
            cart_query = Cart.objects.get(Q(product = id) & Q(user = request.user))
            if(cart_query.quantity >=2):
                cart_query.quantity-=1
                cart_query.save()
        if request.GET['action'] == "remove":
            cart_query = Cart.objects.get(Q(product = id) & Q(user = request.user))
            cart_query.delete()
            # cart = Cart.objects.filter(user = request.user)
            # cart_query.save()
        amount = 0.00
        total_amount = 0.00
        shipment = 70
        cartamount = [p for p in cart if p.user == request.user]
        for i in cartamount:
            tempdata = i.product.discount_price * i.quantity
            amount+=tempdata
            total_amount = amount + shipment
        if request.GET['action'] == "remove":
            context_data = {"amount":amount,"total_amount":total_amount,"type":request.GET['action']}
        else:
            context_data = {"quantity":cart_query.quantity,"amount":amount,"total_amount":total_amount,"type":request.GET['action']}
        return JsonResponse(context_data)
    # if request.GET == "minus":
    # if request.GET == "remove":


def show_to_cart(request):
    user = request.user
    cartitem = 0
    if request.user.is_authenticated:
        cartitem = len(Cart.objects.filter(user = request.user))
        
    cart = Cart.objects.filter(user = user)
    amount = 0.00
    total_amount = 0.00
    shipment = 70
    cartamount = [p for p in cart if p.user == user]
    for i in cartamount:
        tempdata = i.product.discount_price * i.quantity
        amount+=tempdata
        total_amount = amount + shipment

    return render(request, 'app/addtocart.html',{"cart":cart,"amount":amount,"total_amount":total_amount,"shipment":shipment,"cartitem":cartitem})

@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        cartitem = 0
        form = CustomerProfileForm()
        if request.user.is_authenticated:
            cartitem = len(Cart.objects.filter(user = request.user))
        
        context_data = {"form":form,"active":'btn-primary',"cartitem":cartitem}
        return render(request, 'app/profile.html',context_data)

    def post(self,request):
        cartitem = 0
        form = CustomerProfileForm(request.POST)
        if request.user.is_authenticated:
            cartitem = len(Cart.objects.filter(user = request.user))
        
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
        context_data = {"form":form,"active":'btn-primary',"cartitem":cartitem}
        messages.success(request,"Address Save Succesfully")
        return render(request, 'app/profile.html',context_data)

@login_required
def address(request):
    customer = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',{"customer":customer,"active":"btn-primary"})

@login_required
def orders(request):
    cartitem = 0
    user = request.user
    order_place = OrderPlace.objects.filter(user = user)
    if request.user.is_authenticated:
        cartitem = len(Cart.objects.filter(user = request.user))
    messages.info(request,"Order is Placed Status you can show below")
    context_data = {"order_place":order_place,"cartitem":cartitem}
    return render(request, 'app/orders.html',context_data)

def change_password(request):
 return render(request, 'app/change_password.html')

def all_product(request,data = None):
    cartitem = 0
    product = Product.objects.filter(category = data)
    brand = product.values('brand').distinct()
    if request.user.is_authenticated:
        cartitem = len(Cart.objects.filter(user = request.user))
        
    context_data = {"product":product,"brand":brand,"category":data,"cartitem":cartitem}
    return render(request, 'app/mobile.html',context_data)

def mobile(request,category,data=None):
    cartitem = 0
    if data == "None":
        product = Product.objects.filter(category = category)
        brand = product.values('brand').distinct()
    else:
        f_product = Product.objects.filter(category = category)
        product = f_product.filter(brand = data)
        brand = f_product.values('brand').distinct()
    if request.user.is_authenticated:
        cartitem = len(Cart.objects.filter(user = request.user))
        
    context_data = {"product":product,"brand":brand,"category":category,"cartitem":cartitem}
    return render(request, 'app/mobile.html',context_data)

# def login(request):
#  return render(request, 'app/login.html')

class UserRegistration(View):
    context_data = {}
    def get(self,request):
        form = CreateUserForm()
        self.context_data = {"form":form}
        return render(request, 'app/customer_registration.html',self.context_data)
    def post(self,request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations! You registered Successfully")
            form.save()
        self.context_data = {"form":form}
        return render(request, 'app/customer_registration.html',self.context_data)
        
@login_required
def checkout(request):
    user = request.user
    cartitem = 0
    cartitem = len(Cart.objects.filter(user=user))
    address = Customer.objects.filter(user=user)
    if(not address):
        messages.error(request,"Address Didn't Found Add Address")
        return redirect('profile')
    cart = Cart.objects.filter(user=user)
    amount = 0.00
    total_amount = 0.00
    shipment = 70
    cartamount = [p for p in cart if p.user == user]
    for i in cartamount:
        tempdata = i.product.discount_price * i.quantity
        amount+=tempdata
        total_amount = amount + shipment
    # if request.user.is_authenticated:
    #     cartitem = len(Cart.objects.filter(user = request.user))

    context_data ={"total_amount":total_amount,"address":address,"cart":cart,"cartitem":cartitem}
    return render(request, 'app/checkout.html',context_data)

@login_required
def paymentdone(request):
    user = request.user
    cust_id = request.GET.get('cust_id')
    cart = Cart.objects.filter(user = user)
    customer = Customer.objects.get(id = cust_id)
    for c in cart:
        OrderPlace(user = user,product=c.product,customer =customer,quantity = c.quantity,status = 'Accepted' ).save()
        c.delete()

    return redirect('orders')