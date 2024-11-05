from django.shortcuts import render


def blog_views(request):
    template_name = "blog.html"
    
    return render(request, template_name)
