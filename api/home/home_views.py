from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_conts import LOGIN_URL



# Create your views here.
@login_required(login_url= LOGIN_URL)
def home_views(request):
    template_name = "index.html"
    
    return render(request, template_name)

def blog_views(request):
    template_name = "blog.html"
    
    return render(request, template_name)

def cart_views(request):
    template_name = "cart.html"
    
    return render(request, template_name)

def category_views(request):
    template_name = "category.html"
    
    return render(request, template_name)

def checkout_views(request):
    template_name = "checkout.html"
    
    return render(request, template_name)

def confirmation_views(request):
    template_name = "confirmation.html"
    
    return render(request, template_name)

def contact_views(request):
    template_name = "contact.html"
    
    return render(request, template_name)

def elements_views(request):
    template_name = "elements.html"
    
    return render(request, template_name)

def singleblog_views(request):
    template_name = "single-blog.html"
    
    return render(request, template_name)

def singleproduct_views(request):
    template_name = "single-product.html"
    
    return render(request, template_name)

def tracking_views(request):
    template_name = "tracking.html"
    
    return render(request, template_name)