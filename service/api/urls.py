from django.urls import path
from .views import index,urls,image,userlogin,userlogout,userresign,updatepassword,modifypassword,privateresourcesclass,privateresources

urlpatterns = [
    path('index/',index),
    path('urls/',urls),
    path('image/<file>/',image),
    path('login/',userlogin),
    path('logout/',userlogout),
    path('resign/',userresign),
    path('updatepassword/',updatepassword),
    path('modifypassword/',modifypassword),
    path('privateresourcesclass/',privateresourcesclass),
    path('privateresources/',privateresources)
]