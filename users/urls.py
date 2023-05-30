from django.urls import path
import users.views as views

urlpatterns = [
    path('create', views.UserCreate.as_view(), name="userCreate"),
    # path('list', views.UserListView.as_view(), name="userList"),
    # path('update', views.UserView.as_view(), name="userUpdate"),
    # path('delete/<int:id>', views.UserView.as_view(), name="userDelete"),
    # path('logout', views.LogoutView.as_view(), name="logout"),
    
  ]