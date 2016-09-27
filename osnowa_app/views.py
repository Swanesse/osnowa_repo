from django.shortcuts import render
from django.utils import timezone
from .models import Point

# Metoda ta zwraca metodę render, która składa w całość (renderuje) szablon
def point_list(request):
    points = Point.objects.filter(find_date__lte=timezone.now()).order_by('find_date')
    return render(request, 'osnowa_app/point_list.html', {'points': points})
