from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .forms import ValutazioneForm, RegistratiForm
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


def registrati(request):
    # if this is a POST request we need to process the form data
    template = 'sanremo/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistratiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username già utilizzato'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['conferma_password']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Le password inserite non coincidono'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    "",
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['nome']
                user.last_name = form.cleaned_data['cognome']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect(reverse('sanremo-brani'))

    # No post data availabe, let's just show the page.
    else:
        form = RegistratiForm()

    return render(request, template, {'form': form})
