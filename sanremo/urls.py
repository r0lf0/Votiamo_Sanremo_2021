from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BranoListView.as_view(), name='sanremo-brani'),
    path('brani/<int:pk>', views.BranoDetailView.as_view(), name='sanremo-brano'),
    path('about/', views.about, name='sanremo-about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
