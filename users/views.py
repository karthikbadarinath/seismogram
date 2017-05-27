from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello')

def login(request):
	return HttpResponse('Login screen!')

def logout(request):
	return HttpResponse('Logging out!')

def add(request):
	return HttpResponse('Add!')

def edit(request, id):
	return HttpResponse('Are you editing #%s?' % (id))

def view(request, id):
	return HttpResponse('Are you viewing #%s?' % (id))

def delete(request, id):
	return HttpResponse('Oh! No. Are you deleting #%s?' % (id))

def registration(request):
	return HttpResponse('Registration!')