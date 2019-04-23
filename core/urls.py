from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<slug:slug>/', views.candidates, name='candidate'),
    path('candidates/', views.candidates, name='candidates'),
    path('candidate/<int:pk>/', views.candidate_detail_view,
         name='candidate_detail'),
    path('', views.tags, name='tags'),
    path('about/', views.about, name='about'),
    path('methodology/', views.methodology, name='methodology'),
]

# model - candidate needs "candidate-detail page"
