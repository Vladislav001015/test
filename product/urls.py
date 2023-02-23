from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('world', ProductModelViewSet)

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view()),
    path('read/', ProductListAPIView.as_view()),
    path('read/<int:pk>/', ProductDetailAPIView.as_view()),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view()),
    path('hello/', include(router.urls))
]