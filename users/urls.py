
from django.urls import path

from . import views

from django.contrib.auth.models import User, Group, Permission
from rest_framework.serializers import ModelSerializer


from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField

class GroupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'groups')


#http://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield



class UserSerializer(ModelSerializer):
    # groups = PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    groups = SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        slug_field='name',
        required = False
    )

    user_permissions = SlugRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        slug_field='codename',
        required=False
    )


    class Meta:
        model = User
        fields = ('email', 'username', 'groups', 'user_permissions')


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (,)


class UserDetails(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetails.as_view(), name='user-details'),
]