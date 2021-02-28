from django.shortcuts import render
from django.views import generic

from .models import Brano, Valutazione


class BranoListView(generic.ListView):
    model = Brano


class BranoDetailView(generic.DetailView):
    model = Brano

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['valutazioni'] = Valutazione.objects.filter(brano=context['brano']).filter(utente=self.request.user)
        return context


def about(request):
    return render(request, 'sanremo/about.html')
