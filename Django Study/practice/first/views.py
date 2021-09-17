from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD

from datetime import datetime
import random

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)

def select(request):
    context = {}
    return render(request, 'first/select.html', context)

def result(request):
    chosen = int(request.GET['number'])

    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen!= i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results
    }
    return render(request, 'first/result.html', context)
=======
=======
>>>>>>> e12262d5cabc8886e6f807ec02ae348f328a1750
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def select(request):
    message = "숫자를 입력해주세요."
    return HttpResponse(message)

def result(request):
    message = "추첨 결과입니다."
<<<<<<< HEAD
    return HttpResponse(message)
>>>>>>> e12262d5cabc8886e6f807ec02ae348f328a1750
=======
    return HttpResponse(message)
>>>>>>> e12262d5cabc8886e6f807ec02ae348f328a1750
