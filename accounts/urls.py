from django.urls import path
from . import views
from Tawassam.settings import DEBUG, STATIC_URL,  MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutPage, name="logout"),


]
