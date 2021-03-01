from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .forms import ValutazioneForm
from .models import Brano, Valutazione


class BranoListView(generic.ListView):
    model = Brano


class BranoDetailView(generic.DetailView):
    model = Brano

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            valutazioni = Valutazione.objects.filter(brano=context['brano']).filter(utente=self.request.user)
            context['valutazioni'] = valutazioni
            if valutazioni and valutazioni[0]:
                valutazione_form = ValutazioneForm(voto_brano=valutazioni[0].voto_brano,
                                                   voto_interpretazione=valutazioni[0].voto_interpretazione,
                                                   voto_outfit=valutazioni[0].voto_outfit)
            else:
                valutazione_form = ValutazioneForm()
            context['form'] = valutazione_form
        return context


def vota_brano(request, pk):
    if request.method == 'POST':
        form = ValutazioneForm(request.POST)

        if form.is_valid():
            brano = get_object_or_404(Brano, pk=pk)
            valutazione_query_set = Valutazione.objects.filter(brano=brano).filter(utente=request.user)
            if not valutazione_query_set:
                valutazione = Valutazione()
            else:
                valutazione = valutazione_query_set[0]
            valutazione.utente = request.user
            valutazione.brano = brano
            valutazione.voto_brano = form.cleaned_data['voto_brano']
            valutazione.voto_interpretazione = form.cleaned_data['voto_interpretazione']
            valutazione.voto_outfit = form.cleaned_data['voto_outfit']
            valutazione.save()

    return HttpResponseRedirect(reverse('sanremo-brano', args=[brano.id]))

