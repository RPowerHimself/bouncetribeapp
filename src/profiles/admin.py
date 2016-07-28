from django.contrib import admin
from image_cropping import ImageCroppingMixin


# Register your models here.
from .models import Profile, Notification, Influence, MySubTribe, MySubTribeProject

class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
	class Meta:
		model = Profile

class NotificationAdmin(admin.ModelAdmin):
	class Meta:
		model = Notification


class InfluenceAdmin(admin.ModelAdmin):
	class Meta:
		model = Influence


class MySubTribeAdmin(admin.ModelAdmin):
	class Meta:
		model = MySubTribe


class MySubTribeProjectAdmin(admin.ModelAdmin):
	class Meta:
		model = MySubTribeProject


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Influence, InfluenceAdmin)
admin.site.register(MySubTribe, MySubTribeAdmin)
admin.site.register(MySubTribeProject, MySubTribeProjectAdmin)

