from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BranoListView.as_view(), name='sanremo-brani'),
    path('brani/<int:pk>', views.BranoDetailView.as_view(), name='sanremo-brano'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('brani/<int:pk>/vota/', views.vota_brano, name='vota-brano'),
]

urlpatterns += [
    path('register/', views.registrati, name='registrati')
]