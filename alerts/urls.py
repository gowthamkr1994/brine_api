from django.urls import path
import alerts.views as views

urlpatterns = [
    path('create', views.AlertView.as_view(), name="alertCreate"),
    path('list', views.AlertList.as_view(), name="AlertList"),
    # path('update', views.UserView.as_view(), name="userUpdate"),
    path('delete/<int:id>', views.AlertView.as_view(), name="alertDelete"),
    # path('logout', views.LogoutView.as_view(), name="logout"),
    
  ]