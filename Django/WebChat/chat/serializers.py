from django.contrib.auth.models import User, Group
from rest_framework import serializers
from chat.models import Message

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    messages = serializers.HyperlinkedRelatedField(many=True, view_name='message-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url','username','messages')

# ViewSets define the view behavior.
class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url','name')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
  # owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Message
    fields = ('url','creator','content','post_date')