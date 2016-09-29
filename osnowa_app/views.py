from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Point
from django.shortcuts import render, get_object_or_404
from .forms import PointForm

# Metoda ta zwraca metodę render, która składa w całość (renderuje) szablon
def point_list(request):
    points = Point.objects.filter(find_date__lte=timezone.now()).order_by('find_date')
    return render(request, 'osnowa_app/point_list.html', {'points': points})

def point_detail(request, pk): 
	point = get_object_or_404(Point, pk=pk)
	return render(request, 'osnowa_app/point_detail.html', {'point': point})

def point_new(request):
    if request.method == "POST":
        form = PointForm(request.POST)
	#czy formularz jest wypełniony poprawnie
        if form.is_valid():
            point = form.save(commit=False)
            point.author = request.user
            point.published_date = timezone.now()
            point.save()
            return redirect('point_detail', pk=point.pk)
    else:
        form = PointForm()
    return render(request, 'osnowa_app/point_edit.html', {'form': form})

def point_edit(request, pk):
    point = get_object_or_404(Point, pk=pk)
    if request.method == "POST":
        form = PointForm(request.POST, instance=post)
        if form.is_valid():
            point = form.save(commit=False)
            point.author = request.user
            point.published_date = timezone.now()
            point.save()
            return redirect('point_detail', pk=point.pk)
    else:
        form = PointForm(instance=post)
    return render(request, 'osnowa_app/point_edit.html', {'form': form})
