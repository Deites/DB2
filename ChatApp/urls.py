from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'chatapp'
urlpatterns = [
    path('api/messages/list/<int:pk>', views.MessageView.as_view(), name='appimes'),
    path('api/messages/single/<int:pk>', views.SingleMessageView.as_view(), name='appimessingle'),
    path('api/messages/create', views.CreateMessageView.as_view(), name='appimescreate'),
]
