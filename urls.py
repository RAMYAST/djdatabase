
from django.contrib import admin
from django.urls import path
from djapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std', views.std),
    path('view/',views.view),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
]