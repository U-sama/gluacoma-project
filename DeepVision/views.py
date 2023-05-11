from django.shortcuts import render
from django.views import View

from .models import Input_Images
from .forms import Input_ImagesForm
from .Deep_model import predict
# Create your views here.

test = True

class Starting_Page(View):
    
    def get(self, request):
        global test
        test = True
        form = Input_ImagesForm()
        return render(request, "DeepVision/index.html", {"form":form, "test":test})

    def post(self, request):
        form = Input_ImagesForm(request.POST, request.FILES)
        global test
        if form.is_valid():
            test = False
            form.save()
            image = Input_Images.objects.latest("date").image
            path = image.path
            label = predict(path)
            return render(request, "DeepVision/index.html", {"form":form, "test":test, "image":image, "label":label})
        test = True
        
        return render(request, "DeepVision/index.html", {"form":form, "test":test})
