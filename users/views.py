from django.shortcuts import render, redirect

from users.forms import NewUserForm

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