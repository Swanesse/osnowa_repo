from django.shortcuts import render
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
    if request.method == "POINT":
        form = PointForm(request.POINT)
        if form.is_valid():
            point = form.save(commit=False)
            point.author = request.user
            point.find_date = timezone.now()
            point.save()
            return redirect('point_detail', pk=point.pk)
    else:
        form = PointForm()
    return render(request, 'osnowa_app/point_edit.html', {'form': form})
