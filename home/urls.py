from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>', views.project, name='project'),
    path('about/', views.about, name='about'),
]