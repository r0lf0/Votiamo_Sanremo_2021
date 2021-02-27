from django.urls import path
from . import views

urlpatterns = [
    path('', views.BranoListView.as_view(), name='sanremo-brani'),
    path('brani/<int:pk>', views.BranoDetailView.as_view(), name='sanremo-brano'),
    path('about/', views.about, name='sanremo-about'),
]
