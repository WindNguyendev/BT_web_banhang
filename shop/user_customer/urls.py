
from django.urls import path, include
from user_customer .views import SiteLoginView, EditProfileView, SiteRegisterOkView,SiteRegisterView,SiteLogoutView



urlpatterns = [
  
   path('logout', SiteLogoutView.as_view(), name='logout'),
   path('login', SiteLoginView.as_view(), name='login'),
   path('profile', EditProfileView.as_view(), name='profile'),
   path('register', SiteRegisterView.as_view(), name='register'),
   path('register/ok/', SiteRegisterOkView.as_view(), name='register_ok'),
    

]
