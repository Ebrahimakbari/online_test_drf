from rest_framework.routers import DefaultRouter
from .views import category_views

urlpatterns = [
    
]

router = DefaultRouter()
router.register(r'categories',category_views.CategoryViewSet,basename='categories')
router.register(r'favorite-categories',
                category_views.FavoriteCategoryViewSet,
                basename='favorite-categories')

urlpatterns += router.urls