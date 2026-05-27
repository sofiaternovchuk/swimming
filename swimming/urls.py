from django.urls import path
from . import views

app_name = 'swimming'  

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('benefits/', views.benefits_page, name='benefits'),
    path('styles/', views.styles_page, name='styles'),
    path('reasons/', views.reasons_page, name='reasons'),
    #path('task/', views.task, name='task'),
    path('education/', views.education, name='education'),
    path('calc_str_get/', views.calc_str_get, name='calc_str_get'),
    path('education_page/', views.education_page, name='education_page'),
    path('content/', views.content_list, name='content_list'),
]
