from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path,include
from chatgpt.views import ChatGptResponseView
urlpatterns = [
  path('admin/', admin.site.urls),
  path("chatgpt/",include("chatgpt.urls")),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
