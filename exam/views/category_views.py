from rest_framework import viewsets,mixins
from authentication.permissions import IsStudent
from ..serializers import category_serializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS, AllowAny,IsAdminUser,IsAuthenticated
from ..models import Category,FavoriteCategory

User = get_user_model()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = category_serializer.CategorySerializer
    queryset = Category.objects.all()
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser(),IsAuthenticated()]

class FavoriteCategoryViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
    ,viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,IsStudent]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return category_serializer.FavoriteListCreateSerializer
        return category_serializer.FavoriteListRetrieveSerializer
    
    def get_queryset(self):
        return (
            FavoriteCategory.objects.select_related('category')
            .filter(student_id=self.request.user.id)
            .all()
        )
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}