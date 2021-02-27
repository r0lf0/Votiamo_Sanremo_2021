from django.contrib import admin
from .models import Brano, Artista, Valutazione

admin.site.register(Artista)
admin.site.register(Brano)
admin.site.register(Valutazione)
