from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from second.models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    context = {
        'items':Post.objects.all()
    }
    return render(request, 'second/list.html', context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/second/list/')
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid(): # 데이터가 유효한 지
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/second/create/')