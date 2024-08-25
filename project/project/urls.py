from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mymodel', MyModelAPI.as_view()),
    path('mymodel/<int:pk>', MyModelAPI.as_view()),
]
