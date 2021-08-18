from django.http import request
from .models import Message
from rest_framework import serializers
import re
import datetime

class MessageSerializer(serializers.ModelSerializer):
    create_date = serializers.DateField(required=False, default=datetime.datetime.today().date())
    update_date = serializers.DateField(required=False, default=datetime.datetime.today().date())

    def validate(self, attrs):
        email_valid = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(attrs['email_field']))
        text_author_valid = re.findall(r'.', str(attrs['text_author']))
        if (email_valid) and (text_author_valid) and (len(text_author_valid) < 100):
            return super().validate(attrs)
        raise serializers.ValidationError()
    
    def update(self, instance, validated_data):
        instance.email_field = validated_data['email_field']
        instance.text_author = validated_data['text_author']
        instance.create_date  = validated_data['create_date']
        instance.update_date = datetime.datetime.today().date()
        instance.save()      
        return instance

    class Meta:
        model = Message
        fields = ('id', 'email_field', 'text_author', 'create_date', 'update_date')

class CreateMessageSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        email_valid = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(attrs['email_field']))
        text_author_valid = re.findall(r'.', str(attrs['text_author']))
        if (email_valid) and (text_author_valid) and (len(text_author_valid) < 100):
            return super().validate(attrs)
        raise serializers.ValidationError()
    
    class Meta:
        model = Message
        fields = ('email_field', 'text_author')


