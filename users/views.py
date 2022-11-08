from django.shortcuts import render, redirect

from users.forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    print('ooooooooooooooooooooooooooooooooooooooooooooooooooooo')
    form = NewUserForm(request.POST)

    if request.method == 'POST':
        print(f'form valid : {form.is_valid()}')
        if form.is_valid():
            form.save()
        return redirect('/myapp/products')

    context = {
        'form' : form,
    }

    return render(request, 'users/register.html', context=context) 



@login_required
def profile(request):
    pro = Profile.objects.get(user=request.user)

    context = {'profile' : pro}
    
    return render(request, 'users/profile.html', context=context)



@login_required
def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        pro = Profile()
        pro.contact_number = contact_number
        pro.image = image
        pro.user = request.user

        pro.save()

        return redirect('/users/profile')
        

    return render(request, 'users/createprofile.html')      




def seller_profile(request, id):

    seller = User.objects.get(id=id)

    profile = Profile.objects.get(user_id__exact = id)

    context = {
        'seller' : seller,
        'profile' : profile
        }


    return render(request, 'users/seller_profile.html', context=context)



      