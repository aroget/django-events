from django.shortcuts import render
from events.models import Event
from events.forms import UserRegistrationForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User

def welcome(request):
  events = Event.current_events()
  selected_event = None

  if request.method == 'POST':
    event_id = request.POST.get('event_name')
    event = Event.objects.get(id=event_id)
    selected_event = event.name
    event.number_of_attendees += 1
    event.attendees.add(request.user.id)

    event.save()

    return HttpResponseRedirect('/')

  elif request.method == 'GET':
    pass

  return render(request, 'events/welcome.html',
                         {'events': events,
                          'selected_event': selected_event})

def register(request):
  if request.method == 'POST':
      user_form = UserRegistrationForm(request.POST)
      if user_form.is_valid():
          # Create a new user object but avoid saving it yet
          new_user = user_form.save(commit=False)
          # Set the chosen password
          new_user.set_password(
              user_form.cleaned_data['password'])
          # Save the User object
          new_user.save()
          return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
  else:
      user_form = UserRegistrationForm()
  return render(request,
                  'registration/register.html',
                  {'user_form': user_form})

def profile(request, id):
  try:
    user = User.objects.get(id=id)
  except User.DoesNotExist:
    raise Http404

  if request.user.id != int(id):
    return HttpResponseRedirect('/')

  events = Event.objects.filter(attendees__id=id)

  return render(request, 'events/profile.html',
                         {'user': user,
                         'events': events})

def event_detail(request, id):
  try:
    event = Event.objects.get(id=id)
  except Event.DoesNotExist:
    raise Http404

  return render(request, 'events/event-detail.html',
                          {'event': event})

