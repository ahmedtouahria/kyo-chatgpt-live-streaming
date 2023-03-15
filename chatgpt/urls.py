from django.urls import path
from .views import ChatGptResponseView
urlpatterns = [
    path("response/",ChatGptResponseView.as_view())
]
