from django.shortcuts import render

def contact_views(request):
    template_name = "contact.html"
    
    return render(request, template_name)
