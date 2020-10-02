from django.urls import path,include
from .import views
urlpatterns = [
    path('api',views.Apiclass.as_view(),name='api'),
]
