from django.contrib import admin

from .models import TribeFeedItem, TribeAudioProject, TribeComment, TribeAudioInspiration




class TribeFeedItemAdmin(admin.ModelAdmin):
	class Meta:
		model = TribeFeedItem


class TribeAudioProjectAdmin(admin.ModelAdmin):
	class Meta:
		model = TribeAudioProject


class TribeCommentAdmin(admin.ModelAdmin):
	class Meta:
		model = TribeComment


class TribeAudioInspirationAdmin(admin.ModelAdmin):
	class Meta:
		model = TribeAudioInspiration




admin.site.register(TribeFeedItem, TribeFeedItemAdmin)
admin.site.register(TribeAudioProject, TribeAudioProjectAdmin)
admin.site.register(TribeComment, TribeCommentAdmin)
admin.site.register(TribeAudioInspiration, TribeAudioInspirationAdmin)




