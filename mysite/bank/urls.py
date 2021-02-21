from django.urls import path

from . import views
app_name='bank'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/', views.user.as_view(), name='user'),
    path('transfernow/',views.transfernow.as_view(), name='transfernow'),
    path('sucess/',views.sucess,name="sucess"),
    
    
    #path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.transferprocess.as_view(), name='transferprocess'),#transaction page
    path('<int:account_id>/transfer/', views.transfer, name='transfer'),
    path('transactions/',views.transactions.as_view(),name='transactions'),#history
]