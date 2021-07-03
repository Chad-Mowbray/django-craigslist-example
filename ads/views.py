from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ad
from .forms import AdForm

def all_ads(request):
    ads = Ad.objects.all()
    my_data = {
        "ads": ads
    }
    return render(request, "ads/all.html" , my_data)

def new_ad(request):
    if request.method == "GET":
        form = AdForm()
        context = { 'my_form': form}
        return render(request, 'ads/new.html', context)
    if request.method == "POST":
        form = AdForm(request.POST)  
        if form.is_valid():
            
            ###### using Django's ModelForm
            # form.save()
            ###### using Django's ModelForm

            ###### using the basic Django Form class
            cleaned = form.cleaned_data
            title = cleaned["title"]
            content = cleaned["content"]
            Ad.objects.create(title=title, content=content)
            ##### using the basic Django Form class

            return redirect( reverse('all_ads'))