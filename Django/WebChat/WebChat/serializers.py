from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url','name')

class MessageSerializer(serializers.Serializer):
  pk = serializers.IntegerField(read_only=True)
  creator = serializers.CharField(required=False)
  content = serializers.CharField(required=True, max_length=200)
  post_date = serializers.DateTimeField()

  def create(self, validated_data):
    """
    Create and return a new `Message` instance
    """
    return Message.objects.create(**validated_data)

