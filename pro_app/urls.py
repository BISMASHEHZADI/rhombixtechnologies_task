from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.Commant_view,name='Commant_view'),
    path('project/',views.project,name='project'),
]
