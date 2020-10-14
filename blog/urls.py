from django.urls import path
from . import views

urlpatterns = [
            path("", views.blogIndex, name="blogIndex"),
            path("<int:pk>/", views.blogDetails, name="blogDetails"),
            path("<category>/", views.blogCategory, name="blogCategory")
        ]
