from django.contrib import admin
from django.urls import path,include
from project_first_app import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_first_app.urls')),
]