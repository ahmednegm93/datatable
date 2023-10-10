from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.job_list,name='jobs list'),
    path ('<int:id>',views.),
]
