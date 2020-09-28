from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('setcookie',views.setCookie),
    path('getcookie',views.getCookie),
    path('fileupload',views.fileupload),
          
]
