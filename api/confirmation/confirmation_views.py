from django.shortcuts import render

def confirmation_views(request):
    template_name = "confirmation.html"
    
    return render(request, template_name)
