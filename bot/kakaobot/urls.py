from django.urls import path
from kakaobot import views

urlpatterns=[
	path('keyboard/',views.keyboard,name='keyboard'),
	path('message',views.message,name='message'),
]
