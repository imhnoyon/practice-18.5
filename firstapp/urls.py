from django.urls import path
from .  import views
urlpatterns = [
   path('signup/',views.Signup,name='signup'),
   path('login/',views.Login,name='user_login'),
   path('logout/',views.Logout,name='user_logout'),
   path('passchange/',views.passWord_changes,name='passchange'),
   path('passchange2/',views.passWord_changes2,name='passchange2'),
   path('',views.Profile,name='profile'),
]