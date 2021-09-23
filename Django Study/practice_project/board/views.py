from django.shortcuts import render, redirect
from .models import Question
from .forms import ArticleForm

# Create your views here.
# 데이터를 제출할 html 제공
def new(request):
    form = ArticleForm()
    context = {
        'form':form,
    }

    return render(request, 'board/new.html', context)

# 제출한 데이터 저장
def create(request):
    question = Question()
    question.title = request.POST.get('title')
    question.category = request.POST.get('category')
    question.content = request.POST.get('content')
    question.save()
    return redirect('board:detail', question.pk)


# 전체 질문 목록 조회
def index(request):
    questions = Question.objects.all()
    context = {
        'questions':questions
    }
    return render(request, 'board/index.html', context)

# 세부 목록 조회
def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    context = {
        'question':question,
    }
    return render(request, 'board/detail.html', context)

# 데이터를 제출할 기존 내용이 있는 html 제공
def edit(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    context = {
        'question': question,
    }
    return render(request, 'board/edit.html', context)

# 사용자가 제출한 데이터 수정
def update(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    question.title = request.POST.get('title')
    question.category = request.POST.get('category')
    question.content = request.POST.get('content')
    question.save()
    return redirect('board:detail', question.pk)

# 데이터 삭제
def delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        question.delete()
        return redirect('board:index')
    else:
        return redirect('board:detail', question.pk)