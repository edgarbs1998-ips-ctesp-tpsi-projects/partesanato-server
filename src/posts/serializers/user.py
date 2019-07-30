# posts/serializers/user.py

from django.contrib import auth
from libgravatar import Gravatar
from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from rest_framework.validators import UniqueValidator


class AdminUserSerializer(HyperlinkedModelSerializer):
    gravatar = SerializerMethodField()

    class Meta:
        model = auth.get_user_model()
        fields = (
            'url',
            'id',
            'username',
            'gravatar',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
        )
        read_only_fields = (
            'username',
        )
        extra_kwargs = {
            'email': {
                'allow_blank': False,
                'required': True,
                'validators': [UniqueValidator(queryset=auth.get_user_model().objects.all())],
            },
        }

    def get_gravatar(self, obj):
        gravatar = Gravatar(obj.email)
        return gravatar.get_image(size=240, default='identicon')


class UserSerializer(AdminUserSerializer):
    class Meta(AdminUserSerializer.Meta):
        read_only_fields = AdminUserSerializer.Meta.read_only_fields + (
            'is_active',
            'is_staff',
            'is_superuser',
        )
