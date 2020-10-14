from django.urls import path
from . import views

urlpatterns = [
            path('', views.about, name="about"),
            path('privacypolicy/', views.privacypolicy, name="privacypolicy"),
            path('termsofuse/', views.termsofuse, name="termsofuse")
        ]
