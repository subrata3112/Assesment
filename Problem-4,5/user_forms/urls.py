from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('register',views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('solve1',views.solve1,name='solve1')

]