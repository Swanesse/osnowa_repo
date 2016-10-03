from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Point
from django.shortcuts import render, get_object_or_404
from .forms import PointForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import views
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from .forms import *



# Metoda ta zwraca metodę render, która składa w całość (renderuje) szablon - łączy HTMLe w całość, bo wcześniej je rozbiłam żeby nie przepisywać
def point_list(request):
    points = Point.objects.filter(find_date__lte=timezone.now()).order_by('find_date')
    return render(request, 'osnowa_app/point_list.html', {'points': points})


def point_detail(request, pk):
    point = get_object_or_404(Point, pk=pk)
    return render(request, 'osnowa_app/point_detail.html', {'point': point})


def point_new(request):
    if not request.user.is_authenticated():
        return views.login(request, template_name='osnowa_app/login.html')
    else:
        if request.method == "POST":
            form = PointForm(request.POST)
            # czy formularz jest wypełniony poprawnie
            if form.is_valid():
                point = form.save(commit=False)
                point.autor = request.user
                point.created_date = timezone.now()
                point.save()
                return redirect('point_detail', pk=point.pk)
        else:
            form = PointForm()
        return render(request, 'osnowa_app/point_edit.html', {'form': form})


def point_edit(request, pk):
    point = get_object_or_404(Point, pk=pk)
    if request.method == "POST":
        form = PointForm(request.POST, instance=point)
        if form.is_valid():
            point = form.save(commit=False)
            point.author = request.user
            point.created_date = timezone.now()
            point.save()
            return redirect('point_detail', pk=point.pk)
    else:
        form = PointForm(instance=point)
    return render(request, 'osnowa_app/point_edit.html', {'form': form})


def login_user(request):
    """
    django.contrib.auth.views.login login view
    """
    # jeśli użytkownik nie jest zalogowany (uwierzytelniony)
    if not request.user.is_authenticated():
        return views.login(request, template_name='osnowa_app/login.html')
    else:
        return HttpResponseRedirect("/user/")

def user(request):
    """
    django.contrib.auth.views.login login view
    """
    # jeśli użytkownik nie jest zalogowany (uwierzytelniony)
    if not request.user.is_authenticated():
        return views.login(request, template_name='osnowa_app/login.html')
    else:
        return render(request, 'osnowa_app/user.html')

def register(request):
    """
    rejestracja użytkownika
    """

    if request.method == 'POST':
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            user.last_name = form.cleaned_data['phone']
            user.save()
            if form.cleaned_data['log_on']:
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                template = get_template("osnowa_app/point_list.html")
                variables = RequestContext(request, {'user': user})
                output = template.render(variables)
                return HttpResponseRedirect("/")
            else:
                template = get_template("osnowa_app/register_success.html")
                variables = RequestContext(request, {'username': form.cleaned_data['username']})
                output = template.render(variables)
                return HttpResponse(output)

    else:
        form = FormularzRejestracji()
    template = get_template("osnowa_app/register.html")
    form = FormularzRejestracji()
    variables = RequestContext(request, {'form': form})
    output = template.render(variables)
    return HttpResponse(output)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")



