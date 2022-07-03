import random

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse

from .forms import UploadSongForm, CustomLoginForm
from .models import Song


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
        else:
            messages.error(request, 'Username or password not correct')
            return redirect(reverse('login'))
    else:
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = CustomLoginForm()
    return render(request, 'music/loginView_form.html', {'form': form})


def index(request):
    return render(request, 'music/index.html')


def user(request):
    user_songs = Song.objects.all().filter(author=request.user)
    return render(request, 'music/user.html', {'user_songs': user_songs})


def logout_view(request):
    logout(request)
    return redirect('index')


def song_details(request, song_id):
    song = Song.objects.get(song_id=song_id)
    return render(request, 'music/song.html', {'song': song})


@login_required
def upload(request):
    song_id = random.randint(0, 100000000)
    if request.method == 'POST':
        form = UploadSongForm(request.POST or None, request.FILES or None, initial={'author': request.user, 'song_id': song_id})
        if form.is_valid():
            form.save()
            return redirect(f'/{song_id}')
    else:
        form = UploadSongForm(initial={'author': request.user, 'song_id': song_id})
    return render(request, 'music/upload.html', {'form': form})
