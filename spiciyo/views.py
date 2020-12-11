from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import cards, slider_card, call_request, newsletter
import spiciyo
# Create your views here.


def call_request(request):
    name = request.POST['Name']
    email = request.POST['Email']
    phone = request.POST['Phone']
    message = request.POST['Message']
    info = spiciyo.models.call_request(name= name, email= email, phone= phone, message= message)
    info.save()
    print('info saved')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def subscribe(request):
    email_subscription = request.POST['Your_email']
    email_info = newsletter(email = email_subscription)
    email_info.save()
    print("Subscribed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home(request):
    foods = cards.objects.all()
    foods_card = slider_card.objects.all()
    return render(request, 'index.html', {'foods':foods, 'foods_card':foods_card})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    foods = cards.objects.all()
    return render(request, 'blog.html',  {'foods':foods})

def about(request):
    return render(request, 'about.html')


def recipe(request):
    foods_card = slider_card.objects.all()
    return render(request, 'recipe.html', {'foods_card':foods_card})



