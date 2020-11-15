from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .models import Quiz, CustomUser, QuizScore
from django.contrib.auth.forms import UserCreationForm


def dashboard(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            quiz_list = Quiz.objects.all()
            context = {"user": user.username, "quiz_list": quiz_list}

            return render(request, 'core_app/dashboard.html', context)
        else:
            return HttpResponse('<h1>Invalid Login</h1>')
    else:
        return render(request, 'core_app/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            CustomUser.objects.create(user=user)
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'core_app/register.html', {'form': form})


@login_required
def start_quiz(request, id):
    try:
        quiz = Quiz.objects.get(id=id)
    except Quiz.DoesNotExist:
        return HttpResponse('<h1>Invalid quiz</h1>')

    user = CustomUser.objects.get(user=request.user)
    quiz_score = QuizScore.objects.create(quiz_attended=quiz)
    user.quiz_selected = quiz_score
    user.save()
    context = {"quiz": quiz}
    return render(request, 'core_app/quiz.html', context)
