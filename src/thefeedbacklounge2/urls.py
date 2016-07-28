"""thefeedbacklounge2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse
import notifications

from django.views.generic.base import TemplateView


urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
    url(r'^friendship/', include('friendship.urls')),
    url(r'^inbox/notifications/', include('notifications.urls', namespace='notifications')),
    url(r'^matches/$', 'profiles.views.home', name='home'),

    url(r'^tribe/find$', 'profiles.views.tribe_find', name='tribe_find'),
    url(r'^subtribe/create/$', 'tribe.views.subtribe_create', name='subtribe_create'),
    url(r'^subtribe/(?P<id>\d+)$', 'tribe.views.subtribe', name='subtribe'),
    url(r'^subtribe/(?P<id>\d+)/edit$', 'tribe.views.subtribe_edit', name='subtribe_edit'),
    url(r'^subtribe/(?P<id>\d+)/leave$', 'tribe.views.subtribe_leave', name='subtribe_leave'),
    url(r'^subtribe/(?P<id>\d+)/delete$', 'tribe.views.subtribe_delete', name='subtribe_delete'),
    url(r'^subtribe/(?P<id>\d+)/upload$', 'tribe.views.subtribe_upload_project', name='subtribe_upload_project'),

    url(r'^tribe/members$', 'profiles.views.friends', name='tribe'),
    url(r'^inspiration/share$', 'tribe.views.audio_inspiration_create', name='new_audio_inspiration'),
    url(r'^inspiration/(?P<id>\d+)/delete$', 'tribe.views.audio_inspiration_delete', name='audio_inspiration_delete'),
    url(r'^tribe/project/(?P<id>\d+)$', 'tribe.views.get_tribe_audio_project', name='get_tribe_audio_project'),
    url(r'^$', 'tribe.views.get_tribe_feed', name='tribe_feed'),

    url(r'^ajaxtest/$', 'session.views.ajax_test', name='ajax_test'),
    url(r'^upload/limit/$', 'projects.views.upload_project_limit', name='upload_project_limit'),
    # url(r'^feedback/tribe$', 'tribe.views.new_tribe_project', name='new_tribe_project'),
    # url(r'^feedback/$', 'projects.views.getfeedback', name='getfeedback'),

    url(r'^projects/$', 'projects.views.project_list', name='projects'),
    url(r'^project/upload$', 'projects.views.project_create', name='new_match_project'),
    url(r'^project/(?P<id>\d+)$', 'projects.views.project_detail', name='get_project'),
    url(r'^project/(?P<id>\d+)/delete$', 'projects.views.delete_project', name='delete_project'),
    url(r'^project/(?P<id>\d+)/edit$', 'projects.views.edit_project', name='edit_project'),
    url(r'^api/projects/', include("projects.api.urls", namespace='projects-api')),
    

    url(r'^session/(?P<id>\d+)$', 'session.views.get_session', name='get_session'),
    url(r'^session/(?P<id>\d+)/chat$', 'session.views.session_chat', name='session_chat'),
    url(r'^notification_session/(?P<id>\d+)$', 'profiles.views.get_session_notification', name='get_session_notification'),
    url(r'^notification_chat/(?P<id>\d+)$', 'profiles.views.get_chat_notification', name='get_chat_notification'),
    url(r'^notification_profile/(?P<id>\d+)$', 'profiles.views.get_profile_notification', name='get_profile_notification'),
    url(r'^notification_user_profile/(?P<id>\d+)$', 'profiles.views.get_user_profile_notification', name='get_user_profile_notification'),
    url(r'^notification_subtribe/(?P<id>\d+)$', 'profiles.views.get_subtribe_notification', name='get_subtribe_notification'),
    url(r'^notification_tribe_project/(?P<id>\d+)$', 'profiles.views.get_tribe_project_notification', name='get_tribe_project_notification'),
    url(r'^notifications/$', 'profiles.views.get_all_notifications', name='get_all_notifications'),

	# url(r'^session/', 'session.views.sessionfeedback', name='session'),
    url(r'^profile/edit/', 'profiles.views.profile_edit', name='settings'),
    url(r'^profile/photo/$', 'profiles.views.profile_photo', name='profile_photo'),
    url(r'^profile/sessions/$', 'profiles.views.get_previous_sessions', name='previous_sessions'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', 'profiles.views.profile_view', name='profile'),
    url(r'^profile/$', 'profiles.views.profile_user', name='profile_user'),
    




    

    # name='home' is linked to the home def in views.py

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



