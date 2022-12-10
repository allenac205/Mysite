
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from myapp.models import Product, Cart, OderHistory
from users.models import Profile
# Create your views here.

def index(request):
    li = ['allen','sam','savis']
    context = {'names':li}
    return render(request, 'myapp/index.html', context = context)

def new_one(request):
    return HttpResponse('this is new one')






@login_required
def products(request):
    p = Product.objects.all()
    # p1 = [Product.objects.get(id=2)]
    # p2 = Product.objects.filter(price__lt = 200000)

    # return HttpResponse(p[0].price)
    # return HttpResponse(p2)
    # print(p[0].image)
    # print(type(p[0]))

    context = {'products':p}
    return render(request, 'myapp/products.html', context = context)


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/products.html'
    context_object_name = 'products'







def product_details(request, id):
    p = Product.objects.get(id = id)
    context = {'p':p}
    return render(request, 'myapp/product_details.html', context = context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_details.html'
    context_object_name = 'p'








@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller = request.user   

        p = Product(name=name, price=price, description=desc, image=image, seller=seller)
        p.save()

        return redirect('/myapp/products')
    
    return render(request, 'myapp/add_product.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','description','image','seller']
    template_name = 'myapp/add_product.html'
    success_url = reverse_lazy('myapp:products')







def update_product(request,id):
    p = Product.objects.get(id = id)
    context = {'p':p}

    if request.method == 'POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.description = request.POST.get('desc')

        try:
            p.image = request.FILES['upload']
        except Exception as e:
            print(e)
            pass

        p.save()

        return redirect('/myapp/products')
    
    return render(request, 'myapp/update_product.html', context = context)



class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','description','image','seller']
    template_name = 'myapp/update_product.html'
    context_object_name = 'p'
    success_url = reverse_lazy('myapp:products')








def delete_product(request,id):
    p = Product.objects.get(id = id)
    context = {'p':p}

    if request.method == 'POST':
        p.delete()
        return redirect('/myapp/products')
    
    return render(request, 'myapp/delete_product.html', context = context)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'myapp/delete_product.html'
    context_object_name = 'p'
    success_url = reverse_lazy('myapp:products')






@login_required
def cart_view(request):
# To view the items in the cart

    current_user = request.user
# To get cart items of current user
    cart_items = Cart.objects.filter(user_id = current_user)
# To make a list of product class objects containing products in the cart of current user
    product_object_list = []
    for item in cart_items:
        product_object_list.append(Product.objects.get(id = item.product_id))
# To find the total cart items and update on profile table of current user
    total_cart_items = len(product_object_list)
    profile_object = Profile.objects.get(user_id = current_user)
    profile_object.total_cart_items = total_cart_items
    profile_object.save()

    context = {
        "products": product_object_list,
        }
# To find the input quantity by the current user for each item in the cart
    if request.method == "POST":
        for cart_item in cart_items:
            qty = request.POST.get(str(cart_item.product_id))
            c_obj = Cart.objects.get(product_id = cart_item.product_id, user_id = current_user)
            c_obj.quantity = qty
            c_obj.save()
            
        return redirect('myapp:oder_summary')
    
    return render(request, 'myapp/cart_details.html', context=context)




@login_required
def cart_add(request, id):
# To add items to the cart table
    current_user = request.user
# To avoid adding of similar items in the cart
    cart_item = Cart.objects.filter(user_id = current_user)
    flag = True
    for item in cart_item:
        if int(item.product_id) != id:
            flag = True
        else:
            flag = False
            break

    if flag:        
        p = Product.objects.get(id = id)

        product_id = p.id
        product_name = p.name
        current_user = current_user

        c_add = Cart(product_id = product_id, product_name = product_name, user = current_user)
        c_add.save()

    return redirect('myapp:cart_view')






def cart_remove(request, id):
# To remove induvitual items from cart    
    current_user = request.user
    c = Cart.objects.filter(product_id = id, user_id = current_user)
    c.delete()

    return redirect('myapp:cart_view')




def oder_summary(request):
# To view oder summary
    current_user = request.user

    cart_items = Cart.objects.filter(user_id = current_user)

    product_object_list = []
    for cart_item in cart_items:
        product_object_list.append(Product.objects.get(id = cart_item.product_id))
# To find total amount based on the quantity and price
    total_amount = 0
    for product_item in product_object_list:
        for cart_item in cart_items:
            if product_item.id == cart_item.product_id:
                total_amount = total_amount + (product_item.price * cart_item.quantity)

    context = {
        "products": product_object_list,
        "cart" : cart_items,
        "total_amount" : total_amount
        }

    return render(request, "myapp/oder_summary.html", context=context)



def payment_success(request):
# To perfome after payment     
    current_user = request.user
    cart_items = Cart.objects.filter(user_id = current_user)
# To write odered items to oderhistory table
    for item in cart_items:
        oder_object = OderHistory() 
        oder_object.product_id = item.product_id
        oder_object.product_name = item.product_name
        oder_object.user = current_user
        oder_object.quantity = item.quantity
        oder_object.save()
# after writing oderhistory table, deleteing all cart items of current user        
    cart_items.delete()

    profile_object = Profile.objects.get(user_id = current_user)
    profile_object.total_cart_items = 0
    profile_object.save()

    return render(request, "myapp/payment_success.html")




def oder_history(request):
# To view orderd items of current user
    current_user = request.user
    oder_items = OderHistory.objects.filter(user_id = current_user)

    product_object_list = []
    for item in oder_items:
        product_object_list.append(Product.objects.get(id = item.product_id))
    
    context = {
        "products" : product_object_list,
        "oder_items" : oder_items
        }

    return render(request, "myapp/oder_history.html", context = context)

















