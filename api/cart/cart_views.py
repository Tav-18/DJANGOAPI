from django.shortcuts import render

def cart_views(request):
    template_name = "cart.html"
    
    return render(request, template_name)
