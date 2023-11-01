from django.shortcuts import render
from .models import *

# Create your views here.
def waterlevels_view(request):

    current_waterlevel = get_water_level( )
    return render(request, 'waterlevels.html', {'current_waterlevel': current_waterlevel}) 