from django.shortcuts import render

def checkout_views(request):
    template_name = "checkout.html"
    
    return render(request, template_name)
