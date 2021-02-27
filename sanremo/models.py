from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Artista(models.Model):
    nome_completo = models.CharField(max_length=40,
                                     help_text="Inserisci il nome completo dell'artista (niente se è un gruppo o se "
                                               "coincide con il nome d'arte)")
    nome_darte = models.CharField(max_length=40,
                                  help_text="Inserisci il nome d'arte dell'artista")
    is_Gruppo = models.BooleanField(default=False, help_text="Inserisci vero se è un gruppo, falso altrimenti")
    wiki_url = models.TextField(null=True, blank=True, help_text="Inserisci l'URL di wikipedia, se esiste")

    def __str__(self):
        artista = self.nome_breve
        if self.nome_completo is not None:
            artista += " (" + self.nome_completo + ")"
        return artista

    def nome_breve(self):
        return self.nome_darte


class Brano(models.Model):
    titolo = models.CharField(max_length=40)
    testo = ArrayField(models.TextField())
    interpreti = models.ManyToManyField(Artista,
                                        help_text="Seleziona l'interprete o gli interpreti",
                                        related_name="interpreti")
    autori = models.ManyToManyField(Artista,
                                    help_text="Seleziona l'autore o gli autori",
                                    related_name="autori")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('sanremo-brano', args=[str(self.id)])


CATEGORIA = (
    ('i', 'Interpretazione'),
    ('b', 'Brano'),
    ('o', 'Outfit'),
)


class Valutazione(models.Model):
    utente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    brano = models.ForeignKey(Brano, help_text="Seleziona il brano",
                              on_delete=models.PROTECT)
    voto = models.FloatField()
    categoria = models.CharField(
        max_length=1,
        choices=CATEGORIA,
        help_text='Scegli la categoria da votare',
    )

    def __str__(self):
        return self.utente.__str__() \
               + " ha valutato " + self.voto.__str__() \
               + " il brano " + self.brano.__str__() \
               + " nella categoria " + self.categoria.__str__()

