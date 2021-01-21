from django.shortcuts import render, HttpResponse

def homepage(requests):
    return render(request, 'index.html')

def test(requests):
    return render(request, 'test.html')

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("test 3 page")
