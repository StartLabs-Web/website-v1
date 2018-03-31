from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def bootcamp(request):
    return redirect('https://www.youtube.com/user/StartupBootcamp/videos') 
