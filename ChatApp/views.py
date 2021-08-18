from django.core.checks import messages
from django.db.models import fields
from rest_framework.response import Response
from ChatApp.models import Message
from .serializers import MessageSerializer, CreateMessageSerializer
from rest_framework import generics
from rest_framework.response import Response



class MessageView(generics.ListAPIView):
    queryset = Message.objects.order_by('id')
    serializer_class = MessageSerializer
    

    def get(self, request, *args, **kwargs):
        messages_list = Message.objects.order_by('id')[self.kwargs['pk']*10:self.kwargs['pk']*10+10]
        serialezer = MessageSerializer(messages_list, many=True)
        return Response(serialezer.data)


class SingleMessageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CreateMessageView(generics.CreateAPIView):
    serializer_class = CreateMessageSerializer


