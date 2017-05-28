from .models import SeismicEvent
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
	return HttpResponse('Hello')

def add(request):
	csvObj       = open(os.path.join(settings.BASE_DIR, 'SEISMOGRAM_RTHQ.csv'))
	seismicData  = csvObj.read()
	seismicEvent = seismicData.strip().split('\n')
	headers      = seismicEvent[0].split(',')

	for event in seismicEvent[1:]:
		index           = 0
		row             = event.split(',')
		seismicEventObj = SeismicEvent()
		for record in row:
			setattr(seismicEventObj, headers[index].strip(), record.strip())
			index+=1

		seismicEventObj.save()

	return HttpResponse('Done')

def edit(request, id):
	return HttpResponse('Are you editing #%s?' % (id))

def view(request, id):
	return HttpResponse('Are you viewing #%s?' % (id))

def delete(request, id):
	return HttpResponse('Oh! No. Are you deleting #%s?' % (id))
