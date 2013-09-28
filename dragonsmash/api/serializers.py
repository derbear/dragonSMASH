from django.contrib.auth.models import User, Group
from api.models import Effect, Client
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        

class EffectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Effect
        fields = ('url', 'longitude', 'latitude', 'radius',
                  'time_initiated', 'time_countdown', 'client_source')
        

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('url', 'username', 'score')
        
