from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse
from django.contrib import messages
from .forms import *
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def create(request):
    form = EditSuperHeroForm()
    if request.method == 'POST':
        form = EditSuperHeroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'SuperHero created')
        else:
            messages.info(request, 'ups, something went wrong')
        return HttpResponseRedirect(reverse('superheroes:index'))
    context= {
        'form':form
    }

    return render(request, 'superheroes/create.html',context)


def detail(request,id):
    if Superhero.objects.filter(id=id).exists():
        hero = get_object_or_404(Superhero,id=id)
        context = {
            'hero':hero
        }
        return render(request, 'superheroes/details.html',context)
    else:
        return redirect('superheroes:index')


def deleteSuperHero(request,id):
    if Superhero.objects.filter(id=id).exists():
        Superhero.objects.filter(id=id).delete()
        messages.info(request, 'SuperHero deleted')
        return redirect('superheroes:index')
    else:
        return redirect('superheroes:index')

def EditSuperHero(request,id):
    form = EditSuperHeroForm()
    context = {
        'form':form
    }
    if request.method == 'POST':
        name = request.POST['name']
        genre = request.POST['genre']
        runtime = request.POST['runtime']
        release_date = request.POST['release_date']
        if Superhero.objects.filter(id=id).exists():
            Superhero.objects.filter(id=id).update(name=name,genre=genre,runtime=runtime,release_date=release_date)
            messages.info(request, 'SuperHero information updated')
            return redirect('superheroes:index')

    return render(request, 'superheroes/edit_superhero.html',context)
