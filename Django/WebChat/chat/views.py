from django.http import HttpResponse
import json
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins, generics
from django.views.decorators.csrf import csrf_exempt

from chat.models import Message
from chat.serializers import MessageSerializer, UserSerializer
from chat.permissions import IsOwnerOrReadOnly


# Create your views here.

@api_view(('GET',))
def api_root(request, format=None):
  return Response({
    'users': reverse('user-list', request=request, format=format),
    'messages': reverse('message-list',request=request,format=format)
  })


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

#class MessageList(generics.ListCreateAPIView):
class MessageList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  
  def get(self, request, *args, **kwargs):
    messagesCount = Message.objects.all().count()
    if messagesCount >= 30:
      Message.objects.all().delete()
    queryset = Message.objects.all()
    return self.list(request, *args, **kwargs)


  # def perform_create(self, serializer):
    # serializer.save(owner=self.request.user)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
  queryset = Message.objects.all()
  serializer_class = MessageSerializer


from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import parser_classes


@csrf_exempt
# @api_view(['POST'])
@parser_classes((JSONParser,))
def makemessage(request):

  #messagesCount = Message.objects.all().count()
  #if messagesCount >= 30:
   # Message.objects.all().delete()

  body_unicode = request.body.decode('utf-8')
  body = json.loads(body_unicode)
  content = body['content']
  creator = body['creator']

  msg = Message(content=content, creator=creator, post_date=timezone.now())
  msg.save()

  return HttpResponse(body)
