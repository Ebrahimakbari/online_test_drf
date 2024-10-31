from djoser.serializers import UserCreateSerializer as BaseUserCreationSerializer

class UserCreationSerializer(BaseUserCreationSerializer):
    class Meta(BaseUserCreationSerializer.Meta):
        fields = BaseUserCreationSerializer.Meta.fields + ('role',)