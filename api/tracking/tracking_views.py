from django.shortcuts import render


def tracking_views(request):
    template_name = "tracking.html"
    
    return render(request, template_name)