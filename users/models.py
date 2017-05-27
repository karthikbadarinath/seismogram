from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	firstName = models.CharField(max_length=30)
	lastName  = models.CharField(max_length=30)
	email     = models.EmailField(max_length=150)
	password  = models.CharField(max_length=150) # We are encrypting it!
	isActive  = models.BooleanField()
	address   = models.TextField()
	city      = models.CharField(max_length=100)
	state     = models.CharField(max_length=100)
	created   = models.DateTimeField()
	modified  = models.DateTimeField()

	def __str__(self):
		return self.firstName + ' ' + self.lastName
