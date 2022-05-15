from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import HSAdmissions
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    context = {'entry': ''}

    #if the form is submitted, take the high school and college name, and find the image
    if request.method == 'POST':
        highschool = request.POST['highschool']
        college = request.POST['college']
        try:
            results = HSAdmissions.objects.all()
            context = {
                'results': results,
            }
            print(context)
        except HSAdmissions.DoesNotExist:
            pass            

        return render(request, 'compare_hs/search.html', context)
 
    return render(request, 'compare_hs/search.html')

    #return HttpResponse("Hello, world. You're at the polls index.")

def upload(request):

    if request.method == 'POST':
        #get the uploaded image from the form
        image = request.FILES['image']

        highschool = request.POST['highschool']
        college = request.POST['college']
        HSAdmissions.objects.create(image=image, highschool=highschool, college=college)

    return render(request, 'compare_hs/upload.html')



            
