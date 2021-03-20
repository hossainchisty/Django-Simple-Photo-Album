from django.shortcuts import render,redirect
from .models import *
from .forms import GalleryForm
# Create your views here.

def home(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          print(form)
    form =  GalleryForm()

    handle_image = Gallery.objects.all()

    context = {'form':form, 'handle_image': handle_image}
    
    return render(request,  'index.html', context)
      
    

