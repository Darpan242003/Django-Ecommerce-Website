from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from base.models import CartModel

# Create your views here.

def login_(request):
    if request.method == 'POST':
        username=request.POST.get('username', 'dummy_value')
        password=request.POST.get('password', 'dummy_value')
        u=authenticate(username=username, password=password)
        if u:
            login(request, u)
            return redirect('home')

    return render(request, 'login.html', {'login':True})


def register(request):

    if request.method == 'POST':
        u = User.objects.create(
            first_name=request.POST.get('first_name','dummy_value'),
            last_name=request.POST.get('last_name','dummy_value'),
            email=request.POST.get('email','dummy_value'),
            username=request.POST.get('username','dummy_value')
        )
        u.set_password(request.POST.get('password'))
        u.save()
        return redirect('login')
       

    return render(request, 'register.html', {'login':True})

@login_required
def logout_(request):

    logout(request)

    return redirect('login')


@login_required
def profile(request):
    cart_products = CartModel.objects.filter(host=request.user)
    cart_count = cart_products.count()
    
    return render(request, 'profile.html', {'profile':True, 'cart_count':cart_count}) 