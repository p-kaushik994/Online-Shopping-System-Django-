from django.shortcuts import render, redirect
from .models import Product,speaker,printer,smartwatch,monitor,appliance,topdeal,fashiondeal,decorationitem,earbud
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profilehomepage.html') 

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('cart:signup')
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('cart:signup')
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use!")
            return redirect('cart:signup')
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('cart:loginuser')
    return render(request, 'signup.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('cart:profile')  # Redirect to a home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('cart:loginuser')
    return render(request,'login.html')

def headphones(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart
    
    return render(request,'headphones.html',{'products':products,'query': query, 'cart_count': cart_count})

def logout_view(request):
    logout(request)  # This will log out the user
    return redirect('cart:home')
 
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    # If the product is already in the cart, increase the quantity
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    # Save the updated cart in the session
    request.session['cart'] = cart
    # Mark the session as modified
    request.session.modified = True

    # Return the number of items in the cart
    cart_count = sum(cart.values())  # Total count of items in the cart
    return JsonResponse({'cart_count': cart_count})

def update_quantity(request, item_id):
    action = request.POST.get('action')
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if action == 'add':
            cart[str(item_id)] += 1
        elif action == 'subtract' and cart[str(item_id)] > 1:
            cart[str(item_id)] -= 1

    # Save the updated cart in the session
    request.session['cart'] = cart
    
    request.session.modified = True 

    return redirect('cart:cart')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        del cart[str(item_id)]
    # Save the updated cart in the session
    request.session['cart'] = cart
   
    request.session.modified = True
    cart_count = sum(cart.values()) 

    return redirect('cart:cart')


def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())  # Get products based on IDs in the cart
    cart_items = [
        {
            'product': product,
            'quantity': cart[str(product.id)]
        }
        for product in products
    ]
    total_price = sum(item['product'].price * item['quantity'] for item in cart_items)
    # Calculate the cart count
    cart_count = sum(cart.values()) 
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'cart_count':cart_count})

def get_cart_count(request):
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  
    return JsonResponse({'cart_count': cart_count})

def speakers(request):
    query = request.GET.get('query', '')
    if query:
        speakers = speaker.objects.filter(name__icontains=query)
    else:
        speakers = speaker.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'speakers.html', {'speakers':speakers,'query':query,'cart_count':cart_count})

def printers(request):
    query = request.GET.get('query', '')
    if query:
        printers = printer.objects.filter(name__icontains=query)
    else:
        printers = printer.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'printers.html', {'printers':printers,'query':query, 'cart_count':cart_count})

def smartwatches(request):
    query = request.GET.get('query', '')
    if query:
        smartwatches = smartwatch.objects.filter(name__icontains=query)
    else:
        smartwatches = smartwatch.objects.all()
    
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'smartwatches.html', {'smartwatches':smartwatches,'query':query, 'cart_count':cart_count})

def monitors(request):
    query = request.GET.get('query', '')
    if query:
        monitors = monitor.objects.filter(name__icontains=query)
    else:
        monitors = monitor.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'monitors.html', {'monitors':monitors,'query':query,'cart_count':cart_count})

def appliances(request):
    query = request.GET.get('query', '')
    if query:
        appliances = appliance.objects.filter(name__icontains=query)
    else:
        appliances = appliance.objects.all()
    
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'appliances.html', {'appliances':appliances,'query': query, 'cart_count':cart_count})

def topdeals(request):
    query = request.GET.get('query', '')
    if query:
        topdeals = topdeal.objects.filter(name__icontains=query)
    else:
        topdeals = topdeal.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'topdeals.html', {'topdeals':topdeals,'query':query, 'cart_count':cart_count})

def fashiondeals(request):
    query = request.GET.get('query', '')
    if query:
        fashiondeals = fashiondeal.objects.filter(name__icontains=query)
    else:
        fashiondeals = fashiondeal.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart

    return render(request, 'fashiondeals.html', {'fashiondeals':fashiondeals,'query':query, 'cart_count':cart_count})

def decorationitems(request):
    query = request.GET.get('query', '')
    if query:
        decorationitems = decorationitem.objects.filter(name__icontains=query)
    else:
        decorationitems = decorationitem.objects.all()
    
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart
    return render(request, 'decorationitems.html', {'decorationitems':decorationitems,'query':query, 'cart_count':cart_count})

def emptycart(request):
    return render(request,'emptycart.html')

def order_summary(request):
    cart = request.session.get('cart', {})
    products_in_cart = []
    total_price = Decimal('0.00')

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product_total_price = product.price * quantity
        if isinstance(product_total_price, float):
            product_total_price = Decimal(str(product_total_price))
        products_in_cart.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity
        })
        total_price += product_total_price
    return render(request, 'order_summary.html', {'products_in_cart': products_in_cart, 'total_price': total_price})

def payment_page(request):
    cart = request.session.get('cart', {})
    products_in_cart = []
    total_price = Decimal('0.00') 

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product_total_price = product.price * quantity
        if isinstance(product_total_price, float):
            product_total_price = Decimal(str(product_total_price))
        products_in_cart.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity
        })
        total_price += product_total_price

    if request.method == "POST":
        # Here, we assume the payment is successful.
        request.session['cart'] = {}  # Clear the cart after payment
        user = request.user  # Clear the cart after payment
        if user.is_authenticated:
            
            message = f"Dear {user.username},\n\nYour order is successfully placed,Your Transaction was successful,Thank you for your payment.\n\n Amount paid: ₹{total_price}\n\nYour order will be delivered within 7 days! \nThank you for shopping with us!\n\nBest Regards,\nOnline Shop"
           
            messages.success(request, "Payment was successful! A confirmation email has been sent.")
            return render(request, 'payment_success.html', {'total_price': total_price})

        else:
            # If the user is not authenticated, redirect to login page
            messages.error(request, "You must be logged in to complete the payment.")
            return redirect('cart:loginuser')
        # return render(request, 'payment_success.html')

    return render(request, 'payment.html', {'products_in_cart': products_in_cart, 'total_price': total_price})

def earbuds(request):
    query = request.GET.get('query', '')
    if query:
        earbuds = earbud.objects.filter(name__icontains=query)
    else:
        earbuds = earbud.objects.all()
    
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())  # Total count of items in the cart
    
    return render(request, 'earbuds.html', {'earbuds':earbuds,'query':query, 'cart_count':cart_count})
