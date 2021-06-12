from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('newr',views.newr,name='newr'),
    path('update/<int:pk>',views.update,name='update'),
]
