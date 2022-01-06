from django.contrib import admin
from django.urls import include,path
from .views import *

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
    path('redirect/', data_flair),
    path('dataflair/', index), 
    path('setcookie', setcookie),
    path('getcookie', showcookie),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
    path('create/', create_session),
    path('access', access_session),
    path('subscribe/', include('subscribe.urls')),
    path('registration/', include('registration.urls')),
    path('', include('home.urls')),
    path('upload/', include('profile_maker.urls')),
    path('ajax/', include('post.urls')),
]
