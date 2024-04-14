from django.urls import path
from . import views



urlpatterns = [
    path('list_Etudiant/', views.list_Etudiant, name='list_Etudiant'),
    path('list_Admin/', views.list_Admin, name='list_Admin'),
    path('list_Jury/', views.list_Jury, name='list_Jury'),
    path('list_Equipe/', views.list_Equipe, name='list_Equipe'),

    # path('auth', views.isUser, name='isUser'),  
    # path('verifEmail/', views.verification_Email, name='verification_Email'),  
    # path('resetPassword/', views.resetPassword, name='resetPassword'),  
]





