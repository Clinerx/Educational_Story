from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingBase, name='landingBase'),
    path('backhome', views.landingBase, name='backhome'),
    path('deal/', views.deal, name='deal'),
    path('nationalCeleb/', views.n_celeb, name='nationalCeleb'),
]