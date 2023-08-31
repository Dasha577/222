from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
	return render(request, 'app_auth/profile.html')

def login_view(request):
	if request.method == 'GET':
		if request.user.is_authenticated:
			return redirect(reverse('profile'))
		return render(request, 'app_auth/login.html')
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect(reverse('profile'))
	return render(request, 'app_auth/login.html', {'error': "Пользователь не найден"})

def logout_view(request):
	logout(request)
	return redirect(reverse('login'))

def register_view(request):
	return render(request, 'app_auth/register.html')


# Create your views here.