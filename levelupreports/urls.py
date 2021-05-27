from django.urls import path
from .views import usergame_list
from django.conf.urls import include

urlpatterns = [
    path('reports/usergames', usergame_list),
    
]
