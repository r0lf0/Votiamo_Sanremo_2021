from django.shortcuts import render
from django.views import generic

from .models import Brano


class BranoListView(generic.ListView):
    model = Brano


class BranoDetailView(generic.DetailView):
    model = Brano


def about(request):
    return render(request, 'sanremo/about.html')
