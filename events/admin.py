from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  list_display = ('name', 'date', 'number_of_attendees',)
  list_filter = ('language', 'date')
  search_fields = ['name']

admin.site.register(Event, EventAdmin)
