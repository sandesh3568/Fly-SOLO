from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"homepage.htm")
def about(request):
    return render(request,"about.htm")
def login(request):
    return render(request,"login.htm")
def tracker(request):
    return render(request,"tracker.htm")

