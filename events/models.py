import datetime
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Event(models.Model):
  ENGLISH = 'EN'
  FRENCH = 'FR'

  LANGUAGE_CHOICES = (
    (ENGLISH, 'ENGLISH'),
    (FRENCH, 'FRENCH'),
  )
  name = models.CharField(max_length = 130)
  description = models.TextField(blank = False)
  date = models.DateField(auto_now = False)
  slug = models.SlugField(max_length = 140)
  number_of_participants = models.IntegerField()
  number_of_attendees = models.IntegerField(default = 0, editable=False)
  created_on = models.DateField(auto_now = True, editable=False)
  language = models.CharField(max_length = 2, choices = LANGUAGE_CHOICES, default = ENGLISH)
  attendees = models.ManyToManyField(User, related_name='attendees', blank = True)

  def __str__(self):
    return self.name

  def spots_available(self):
    return self.number_of_participants - self.number_of_attendees

  @classmethod
  def current_events(cls):
    return Event.objects.filter(number_of_attendees__lt = F('number_of_participants')).filter(date__gte=datetime.date.today())

  class Meta:
    ordering = ['-date']



