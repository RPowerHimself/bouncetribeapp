from django.contrib import admin


from .models import SessionFeedback

class SessionAdmin(admin.ModelAdmin):
	class Meta:
		model = SessionFeedback

admin.site.register(SessionFeedback, SessionAdmin)