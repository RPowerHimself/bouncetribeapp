from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	MatchChatMessageCreateAPIView,
	MatchChatMessageDetailAPIView,
	MatchChatMessageListAPIView,
	ProjectCreateAPIView,
	ProjectDeleteAPIView,
	ProjectDetailAPIView,
	ProjectListAPIView,
	ProjectUpdateAPIView,
	ProjectMatchDetailAPIView,
	ProjectMatchListAPIView

	)

urlpatterns = [
	url(r'^$', ProjectListAPIView.as_view(), name='project-list'),
	url(r'^create/$', ProjectCreateAPIView.as_view(), name='project-create'),
	url(r'^(?P<pk>\d+)/$', ProjectDetailAPIView.as_view(), name='project-detail'),
	url(r'^(?P<pk>\d+)/edit/$', ProjectUpdateAPIView.as_view(), name='project-update'),
	url(r'^(?P<pk>\d+)/delete/$', ProjectDeleteAPIView.as_view(), name='project-delete'),

	url(r'^chat/$', MatchChatMessageListAPIView.as_view(), name='chat-list'),
	url(r'^chat/create/$', MatchChatMessageCreateAPIView.as_view(), name='chat-create'),
	url(r'^chat/(?P<pk>\d+)/$', MatchChatMessageDetailAPIView.as_view(), name='chat-detail'),


	url(r'^match/$', ProjectMatchListAPIView.as_view(), name='match-list'),
	url(r'^match/(?P<pk>\d+)/$', ProjectMatchDetailAPIView.as_view(), name='match-detail'),

]



