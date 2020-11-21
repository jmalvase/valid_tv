from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

## RENDER/REROUTE
def shows(request):
    context={
        'all_shows':Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new_show_page(request):
    return render(request, 'add_show.html')

##CREATE/EDIT/UPDATE
def create_show(request):
    if request.method=='POST':
        errors=Show.objects.show_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new')
        Show.objects.create(title=request.POST['show_title'], network=request.POST['network'],release_date=request.POST['release_date'], description=request.POST['description'])
        return redirect('/')
    return redirect('/')

def edit_show(request, show_id):
    edit_show=Show.objects.get(id=show_id)
    context={
        'show':edit_show
    }
    return render(request, 'edit.html', context)
def update_show(request, show_id):
    if request.method=='POST':
        errors=Show.objects.show_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/{show_id}/edit')
        to_update=Show.objects.get(id=show_id)
        to_update.title=request.POST['show_title']
        to_update.network=request.POST['network']
        to_update.release_date=request.POST['release_date']
        to_update.description=request.POST['description']
        to_update.save()
        return redirect('/')
    return redirect('/')
## READ
def read_show(request, show_id):
    one_show=Show.objects.get(id=show_id)
    context={
        'show':one_show
    }
    return render(request, 'one_show.html', context)

## DESTROY
def destroy(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/')


