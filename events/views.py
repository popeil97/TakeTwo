from django.shortcuts import render
from .models import Event
# Create your views here.

def event_list_view(request):
    events = Event.objects.all()
    context = {}
    
    if request.user.is_restaurant:
        context = {'events': events}

    return render(request,'events/event_list_view.html', context)
