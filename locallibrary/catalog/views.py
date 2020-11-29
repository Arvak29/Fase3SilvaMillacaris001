from django.shortcuts import render
from . models import Genre, Plataform, Developer, Game, GameInstance
from django.views import generic

#informacion para formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#librerias de imagenes
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static

#Forms
from .forms import GameForm

# Create your views here.
def index(request):
    num_Games = Game.objects.all().count()
    num_Instances = GameInstance.objects.all().count()
    num_instances_available=GameInstance.objects.filter(stock__exact='a').count()
    num_Developer = Developer.objects.count()

    return render(
        request,
        'index.html',
        context={'Num_Games': num_Games, 'Num_Instances': num_Instances, 'num_instances_available':num_instances_available, 'Num_Developer': num_Developer},
    )

def PlaystationStore(request):
    num_Games = Game.objects.all().count()
    num_Instances = GameInstance.objects.all().count()
    num_instances_available=GameInstance.objects.filter(stock__exact='a').count()
    num_Developer = Developer.objects.count()
    '''img = Game.img.objects.all() || , 'Image': img'''

    return render(
        request,
        'PlaystationStore.html',
        context={'Num_Games': num_Games, 'Num_Instances': num_Instances, 'num_instances_available':num_instances_available, 'Num_Developer': num_Developer},
    )

def Add_game(request):
    
    data = {
        'form': GameForm()
    }

    return render(
        request,
        'add_game.html',
        data,
    )


#StoreView

class PlataformGameView(generic.DetailView):
    model = Plataform

    
#Game CRUD

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'developer', 'description', 'genre', 'plataform', 'players', 'price', 'img']
    template_name = 'add_game.html'

class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'developer', 'description', 'genre', 'plataform', 'players', 'price']

class GameDelete(DeleteView):
    model = Game

class GameDetailView(generic.DetailView):
    model = Game
