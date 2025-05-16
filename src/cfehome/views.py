from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit



def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **Kwargs):
    qs = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs.count()
    }
    path = request.path
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)