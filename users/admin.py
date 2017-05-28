from __future__ import unicode_literals
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	empty_value_display = 'Not Available'

	list_display  = ["id", "firstName", "lastName", "email", "city", "state", "isActive", "created", "modified"]
	list_filter   = ["city", "state", "isActive"]
	search_fields = ["id", "firstName", "lastName", "email", "city", "state"]

	class Meta:
		model = User

admin.site.register(User, UserAdmin)
