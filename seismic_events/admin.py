from __future__ import unicode_literals
from django.contrib import admin
from .models import SeismicEvent

class SeismicEventAdmin(admin.ModelAdmin):
	empty_value_display = 'Not Available'

	list_display  = ["id", "event_date", "strike", "depth", "lat", "lon", "q_1", "q_2", "unc", "unc_1"]
	list_filter   = ["event_date"]
	search_fields = ["id", "strike", "depth"]

	class Meta:
		model = SeismicEvent

admin.site.register(SeismicEvent, SeismicEventAdmin)
