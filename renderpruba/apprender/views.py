from django.shortcuts import render

# Create your views here.

def helloWord(request):
    return render(request, 'apprender/index.html')
