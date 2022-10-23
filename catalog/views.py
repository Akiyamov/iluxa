from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.models import ilaksa
from .forms import CreateFrom

def index(request):
    num_idea=ilaksa.objects.all().count()
    num_live_idea=ilaksa.objects.filter(status_idea='t').count()
    num_dead_idea=ilaksa.objects.filter(status_idea='z').count()

    return render(
        request,
        'index.html',
        context={'num_idea':num_idea,'num_live_idea':num_live_idea, 'num_dead_idea':num_dead_idea},
    )

from django.views import generic

class LiveIdeaListView(generic.ListView):
    model = ilaksa
    context_object_name = "ilaksa_list"
    template_name = "ilaksa_list.html"
    def get_queryset(self):
        return ilaksa.objects.filter(status_idea='t')

class DeadIdeaListView(generic.ListView):
    model = ilaksa
    template_name = "ilaksd_list.html"
    def get_queryset(self):
        return ilaksa.objects.filter(status_idea='z')

def ilaksa_new(request):
    if request.method == 'POST':
        form = CreateFrom(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse(index))
    else:
        form = CreateFrom()
    return render(
        request,
        'ilaksa_new.html',
        {'form': form}
    )