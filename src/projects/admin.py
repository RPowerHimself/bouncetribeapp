from django.contrib import admin

from .models import Project, ProjectMatch, MatchChatMessage



class ProjectAdmin(admin.ModelAdmin):
	class Meta:
		model = Project

class ProjectMatchAdmin(admin.ModelAdmin):
	class Meta:
		model = ProjectMatch

class MatchChatMessageAdmin(admin.ModelAdmin):
	class Meta:
		model = MatchChatMessage



admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMatch, ProjectMatchAdmin)
admin.site.register(MatchChatMessage, MatchChatMessageAdmin)