from django.shortcuts import render


def singleproduct_views(request):
    template_name = "single-product.html"
    
    return render(request, template_name)