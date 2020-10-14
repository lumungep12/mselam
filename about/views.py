from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def termsofuse(request):
    return render(request, 'termsofuse.html')
