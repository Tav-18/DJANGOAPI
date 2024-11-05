from django.shortcuts import render


def singleblog_views(request):
    template_name = "single-blog.html"
    
    return render(request, template_name)