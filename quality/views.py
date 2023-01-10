from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime as dt
from .forms import ContactForm,ApplicationForm
from django.contrib import messages



# Create your views here.
def welcome(request):
    video=Video.objects.all()
    return render(request, 'welcome.html',{'video': video})



def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def thank(request):
    return render(request, 'thank.html')

def contact(request):
    if request.method == 'GET': 
        form = ContactForm()
    else:
       form = ContactForm(request.POST)
       if form.is_valid():
        form.save()
        messages.success(request,"Thank you for contacting us")
        return redirect('thank')
        

    return render(request, "contact.html",{'form': form})
    

def job(request):
    job = jobs.objects.all()
    return render(request, 'jobs.html', {"job":job})

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {
        'form': form
    })    

 

# Create your views here.
def my_photos(request):
    photos = Image.show_all_photos()
    locations = Location.objects.all()
    return render(request, 'all-photos/photos.html', {"photos":photos, "locations":locations})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_photos = Image.search_photo_by_category(category)
        locations = Location.objects.all()
        message = f"{category}"

        return render(request, 'all-photos/search.html', {"message":message, "photos":searched_photos, "locations":locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message":message})


def get_category(request, category):
    category_results = category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(category__category_name = category)
    return render(request,'all-photos/photos.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})

def get_location(request, location_name):
    category_results = category.objects.all()
    locations = Location.objects.all()
    location_result = Image.objects.filter(location__id= location_name)
    return render(request,'all-photos/locations.html',{'all_images':location_result,'category_results':category_results,'locations':locations})



def photos_today(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})   
def past_days_photos(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(photos_of_day)
    return render(request, 'all-photos/past-photos.html', {"date": date})
