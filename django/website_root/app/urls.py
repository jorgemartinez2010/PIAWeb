from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('pagina2',views.pagina2, name="pagina2"),
    path('pagina3',views.pagina3, name="pagina3"),
    path('pagina4',views.pagina4, name="pagina4"),
    path('pagina5',views.pagina5, name="pagina5"),
]