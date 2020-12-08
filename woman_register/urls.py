from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.paginaInicial),
    path('form/',views.woman_form, name='woman_insert'),
    path('<int:cpf>/',views.woman_form, name='woman_update'),
    path('delete/<int:cpf>/',views.woman_delete, name='woman_delete'),
    path('list/',views.woman_list, name='woman_list'),

]
