from django.shortcuts import render, redirect
from .models import Question
from .forms import BoardForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
# 데이터를 제출할 html 제공
# def new(request):
#     form = BoardForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'board/new.html', context)

# 제출한 데이터 저장
@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('board:detail', question.pk)
    else:
        form = BoardForm()
    context = {
        'form':form,
    }
    return render(request, 'board/create.html', context)
    # question = Question()
    # question.title = request.POST.get('title')
    # question.category = request.POST.get('category')
    # question.content = request.POST.get('content')
    # question.save()
    # return redirect('board:detail', question.pk)


# 전체 질문 목록 조회
def index(request):
    questions = Question.objects.all()
    context = {
        'questions':questions
    }
    return render(request, 'board/index.html', context)

# 세부 목록 조회
def detail(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)
    context = {
        'question':question,
    }
    return render(request, 'board/detail.html', context)

# 데이터를 제출할 기존 내용이 있는 html 제공
# def edit(request, question_pk):
#     question = Question.objects.get(pk=question_pk)
#     context = {
#         'question': question,
#     }
#     return render(request, 'board/edit.html', context)

# 사용자가 제출한 데이터 수정
@login_required
@require_http_methods(['GET','POST'])
def update(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
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
    # question = Question.objects.get(pk=question_pk)
    # question.title = request.POST.get('title')
    # question.category = request.POST.get('category')
    # question.content = request.POST.get('content')
    # question.save()
    # return redirect('board:detail', question.pk)

# 데이터 삭제
@login_required
@require_POST
def delete(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    # question = get_object_or_404(Question, pk=question_pk)
    # if request.method == 'POST':
    #     question.delete()
    #     return redirect('board:index')
    # return redirect('board:detail', question.pk)
    
    # question = get_object_or_404(Question, pk=question_pk)
    # question.delete()

    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_pk)
        question.delete()
    return redirect('board:index')