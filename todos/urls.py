from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name = 'index'),
    path('upload/', views.create, name = 'create'),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)

]