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



# Metoda ta zwraca metodę render, która składa w całość (renderuje) szablon - łączy HTMLe w całość, bo wcześniej je rozbiłam żeby nie przepisywać. Może też przesyłać do szablonu .html zmienne
def point_list(request):
    # Do zmiennej points przypisywana zostaje lista z obiektami klasy Point - wyciągana jest z bazy danych
    points = Point.objects.all()


    return render(request, 'osnowa_app/point_list.html', {'points': points})

def informacje(request):

    return render(request, 'osnowa_app/informacje.html')

def kontakt(request):

    return render(request, 'osnowa_app/kontakt.html')


def search(request):
    # Do zmiennej points przypisywana zostaje lista z obiektami klasy Point - wyciągana jest z bazy danych
    points = Point.objects.all()
    # porównać, który punkt z bazy danych ma taką nazwę jaka została wpisana i zwrócić pk tego obiektu
    primary_key = -1
    for point in points:
        if request.GET["q"] == point.numer_katalogowy:
            primary_key=point.pk

    return HttpResponseRedirect("/point/" + str(primary_key) + "/")

def point_detail(request, pk):
    point = get_object_or_404(Point, pk=pk)

    # print ("Tutaj znajduje sie" + str(request.POST["uszkodzony"]) + "A tu jest koniec")

    print(str(request.POST))

    if request.method == "POST" and 'odnaleziony' in request.POST:

        print (str(request.POST))
        point.odnaleziony += 1
        point.save()
        return redirect('point_detail', pk=point.pk)

    if request.method == "POST" and 'uszkodzony' in request.POST:

        print (str(request.POST))
        point.uszkodzony +=1
        point.save()
        return redirect('point_detail', pk=point.pk)




                                                             # przesłanie zmiennej do szablonu 'nazwa zmiennej' :
    return render(request, 'osnowa_app/point_detail.html', {'point': point})

# Zrobić tak żeby drugi przycisk też działał

def point_new(request):
    if not request.user.is_authenticated():
        return views.login(request, template_name='osnowa_app/login.html')
    else:
        if request.method == "POST":
            form = PointForm(request.POST, request.FILES)
            # czy formularz jest wypełniony poprawnie
            if form.is_valid():
                point = form.save(commit=False)
                point.autor = request.user
                point.created_date = timezone.now()
                # zapisanie punktu w bazie danych
                point.save()
                return redirect('point_detail', pk=point.pk)
        else:
            form = PointForm()
        return render(request, 'osnowa_app/point_edit.html', {'form': form})


def point_edit(request, pk):
    point = get_object_or_404(Point, pk=pk)
    if request.method == "POST":
        # to jest wywołanie konstruktora klasy PointForm
        form = PointForm(request.POST, request.FILES, instance=point)
        if form.is_valid():
            # save zwraca egzemplarz modelu związanego z klasą PointForm
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

    template = get_template("osnowa_app/register.html")
    form = FormularzRejestracji()
    variables = {'form': form}
    output = template.render(variables, request)
    return HttpResponse(output)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")



