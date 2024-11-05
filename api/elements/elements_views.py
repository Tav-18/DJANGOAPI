from django.shortcuts import render

def elements_views(request):
    template_name = "elements.html"
    
    return render(request, template_name)
