from django.urls import path


from . import views


app_namae ='jikomap'
urlpatterns = [
    path('', views.index, name='index'),
]