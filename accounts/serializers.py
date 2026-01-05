from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "role",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
        }


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_repeat = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context.get("request").user
        if not user.check_password(value):
            raise serializers.ValidationError("رمز عبور فعلی نادرست است.")
        return value

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password_repeat = attrs.get("new_password_repeat")

        if new_password == attrs.get("old_password"):
            raise serializers.ValidationError(
                "رمز عبور جدید نمی‌تواند با رمز عبور قدیمی یکسان باشد."
            )
        if new_password != new_password_repeat:
            raise serializers.ValidationError("رمز عبور جدید و تکرار آن برابر نیستند!")
        return attrs
