from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def landingBase(request):
    return render(request, 'landingBase.html')

def deal(request):
    return render(request, 'deal.html')

def n_celeb(request):
    return render(request, 'nationalCelebration.html')