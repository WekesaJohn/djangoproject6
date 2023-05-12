
from django.contrib import admin
from django.urls import path
from texton import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('il/', views.TEXTON, name='TEXTON'),
    path('', views.makepurchase,name='make'),
    path('c/', views.cat,name='cat'),
    path('J/', views.Jacaranda,name='Jacaranda'),
    path('m/', views.members),
    path('student/', views.student),
    path('emp/', views.Employee),
    path('session/', views.setsession),
    path('form/', views.form),
    path('p/', views.power),
]
