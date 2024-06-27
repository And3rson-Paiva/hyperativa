from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cardhandler.views import CardCreateAPIView, CardCheckAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/cards/', CardCreateAPIView.as_view(), name='card-create'),
    path('api/cards/check/<str:card_number>/', CardCheckAPIView.as_view(), name='card-check'),
]
