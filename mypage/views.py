from django.shortcuts import render
from .models import Page
from django.shortcuts import get_object_or_404, render,HttpResponse

# Create your views here.



def pageview(request,slug):
    page = get_object_or_404(Page, slug=slug)
    newpages=Page.objects.all()

    return render(request,'post/page.html',{'page':page,'newpages':newpages})