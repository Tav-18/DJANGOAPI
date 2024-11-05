from django.shortcuts import render


def category_views(request):
    template_name = "category.html"
    
    return render(request, template_name)