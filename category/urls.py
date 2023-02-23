from django.urls import path, include
from category.views import CategoryList, CategoryCreate, CategoryCRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryCRUD)

urlpatterns = [
    path('', include(router.urls))
    # path('', CategoryList.as_view()),
    # path('create/', CategoryCreate.as_view()),
    
]