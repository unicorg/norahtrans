from django.conf.urls import url
from . import views

app_name = 'stockapplication'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^StockCreate/$', views.StockCreate, name='StockCreate'),
    
]
