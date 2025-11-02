from django.urls import path
from .views import DivinationAPIView

urlpatterns = [
    # APIのエンドポイント: /api/v1/divination/
    path('divination/', DivinationAPIView.as_view(), name='divination_api'),
]