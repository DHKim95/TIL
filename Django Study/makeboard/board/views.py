from django.shortcuts import get_object_or_404, render, redirect
from .models import Question
from .forms import BoardForm

# Create your views here.
def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('board:detail', question.pk)
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'board/create.html', context)

def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'board/index.html', context)

def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    context = {
        'question':question
    }
    return render(request, 'board/detail.html', context)

def update(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('board:detail', question_pk)
    else:
        form = BoardForm(instance=question)
    context = {
        'form': form,
        'question':question,
    }
    return render(request, 'board/update.html', context)

def delete(request, question_pk):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_pk)
        question.delete()
    return redirect('board:index')