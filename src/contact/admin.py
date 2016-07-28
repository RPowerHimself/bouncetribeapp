from django.contrib import admin

# Register your models here.
from .models import GetFeedbackProject

class GetFeedbackProjectAdmin(admin.ModelAdmin):
	class Meta:
		model = GetFeedbackProject

admin.site.register(GetFeedbackProject, GetFeedbackProjectAdmin)