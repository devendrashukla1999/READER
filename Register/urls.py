from django.urls import path
from . import views
urlpatterns = [
    path("",views.register,name="reg"),
    path("login",views.login,name="log"),
    path("logout",views.logout,name="lgt"),
    path("profile",views.profile,name="pro"),
    path("upr",views.uppro,name="upr")
]