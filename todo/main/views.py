from django.shortcuts import render, HttpResponse

def homepage(requests):
    return HttpResponse('hello world')

def test(requests):
    return render(request, 'test.html')

def second(request):
    return HttpResponse('test 2 page')