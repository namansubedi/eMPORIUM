from django.http import request
from django.shortcuts import render, redirect
from home.models import profiles, products
from django.contrib.auth.models import User, auth
from .forms import productsform, profilesform
from django.contrib import messages

# Create your views here.
def index(request):
    user = request.user
    showupload = False
    if user.is_authenticated:
        profile = profiles.objects.filter(user_name=user.username)
        for pro in profile:
            showupload = pro.is_seller 
        senditem = products.objects.all()
        return render(request, 'index.html', {"products": senditem,"showupload":showupload})
    else:
        senditem = products.objects.all()
        return render(request, 'index.html', {"products": senditem} )

def register(request):
    if request.method == 'POST':

        form = profilesform(request.POST)
        if form.is_valid():
            is_seller = form.cleaned_data['is_seller']
        else:
            messages.info(request,'Invalid Data Sent!')
        
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
        gmap = request.POST['gmap']

        if password1 != password2:
            messages.info(request,'Password Mismatch!')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already In Use!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Already In Use!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
            user.save()

            profile = profiles.objects.create(user_name=username, phone_number=phone_number, region=region, city=city, area=area, locale=locale, is_seller=is_seller, gmap=gmap)
            profile.save()

            return redirect('/')
    else:
        form = profilesform()
        return render(request, 'register.html', {"form": form})

def upload(request):
    
    form = productsform()
    user = request.user
    owneruser = user.username

    if request.method == 'POST':
        form = productsform(request.POST, request.FILES)
  
        if form.is_valid():
            #form.seller_id=user.username
            
            name = form.cleaned_data['name']
            cat = form.cleaned_data['category']
            brand = form.cleaned_data['brand']
            price = form.cleaned_data['price']
            seller_id = owneruser
            image = form.cleaned_data['image']
            desc = form.cleaned_data['description']
            stock = form.cleaned_data['stock']
            keywords = "this is only a temporary fix for search functionality"
            detail = form.cleaned_data['detail']
            
            product = products.objects.create(name= name, category=cat, brand=brand, price=price, seller_id=seller_id, image=image, description=desc, stock=stock, keywords=keywords, detail=detail)
            product.save()

            return redirect('/')
        else:
            print("invalid input")
    else:
        form = productsform()
        return render(request, "upload.html", {"form": form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong Values Entered!')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')