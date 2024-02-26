from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login_api'),
    path('logout', views.logout, name='logout_api'),
    path('signup', views.signup,name='signup_api'),
    path('createmedicine', views.CreateMedicine.as_view()),
    path('read', views.ReadMedicine.as_view()),
    path('update/<int:pk>', views.UpdateMedicine.as_view()),
    path('delete/<int:id>', views.delete),
    path('',views.search,name='search_api')
    
]                                                             
                                                                                                                 