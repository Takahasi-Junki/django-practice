from django.contrib import admin
from django.urls import path, include
'''
from .views import helloworldfunc
from .views import HelloWorldClass
'''

urlpatterns = [
    path('hello/', admin.site.urls),
    path('', include('helloworldapp.urls')),
]