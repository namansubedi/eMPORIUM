from django.shortcuts import render, redirect
from home.models import profiles
from django.contrib.auth.models import User, auth
from .forms import productsform

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        phone_number = request.POST['phone_number']
        region = request.POST['region']
        city = request.POST['city']
        area = request.POST['area']
        locale = request.POST['locale']
        is_seller = request.POST['is_seller']
        gmap = request.POST['gmap']

        if password1 != password2:
            
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
            user.save()

            profile = profiles.objects.create(user_name=username, phone_number=phone_number, region=region, city=city, area=area, locale=locale, is_seller=False, gmap=gmap)
            profile.save()

            return redirect('/')
    else:
        return render(request, 'register.html')

def upload(request):
    
    form = productsform()

    if request.method == 'POST':
        form = productsform(request.POST, request.FILES)
  
        if form.is_valid():
            #form.seller_id=user.username
            form.save()
            '''
            name = form.cleaned_data['name']
            cat = form.cleaned_data['category']
            slug = form.cleaned_data['slug']
            brand = form.cleaned_data['brand']
            price = form.cleaned_data['price']
            seller_id = form.cleaned_data['seller_id']
            image = form.cleaned_data['image']
            desc = form.cleaned_data['description']
            stock = form.cleaned_data['stock']
            keywords = form.cleaned_data['keywords']
            detail = form.cleaned_data['detail']
            
            product = products.objects.create()
            product.save()
            '''

            return redirect('/')
        else:
            print("invalid input")
    form = productsform()
    return render(request, "upload.html", {"form": form})