from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('registr', registr, name='registr'),
    path('/uspex_registr', uspex, name='uspex'),
    path('login/', user_login, name='login'),
    path('pig/', pig, name='pig'),
    path('kenguru/', kenguru, name='kenguru'),
    path('logout/', user_logout, name='logout'),
]
# path('exit/', views.LogoutView.as_view(), name='exit'),