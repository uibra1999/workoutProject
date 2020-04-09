from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password  # This is to allow encryption of the passwords.


# Create your views here.

def index(request):
	context_dict = {'bold_message': 'Arnold works out here'}
	return render(request, 'workout/index.html', context_dict)