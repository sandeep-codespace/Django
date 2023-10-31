from django.shortcuts import render

# Create your views here.
def Home_Page(request):
    return render(request, "home.html")

def About_Page(request):
    return render(request, "about.html")

def ContactUs_Page(request):
    return render(request, "contact.html")

def Gallery_Page(request):
    return render(request, "gallery.html")

def Login_Page(request):
    return render(request, "login.html")