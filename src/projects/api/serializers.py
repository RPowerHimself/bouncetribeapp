from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	)


from projects.models import MatchChatMessage, Project, ProjectMatch





class MatchChatMessageCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = MatchChatMessage
		fields = [
			'user',
			'to_user',
			'message',
			'session',

		]



class MatchChatMessageSerializer(ModelSerializer):
	user = SerializerMethodField()
	to_user = SerializerMethodField()
	class Meta:
		model = MatchChatMessage
		fields = [
			'id',
			'user',
			'to_user',
			'message',
			'session',

		]

	def get_user(self, obj):
		return str(obj.user.username)

	def get_to_user(self, obj):
		return str(obj.to_user.username)









class ProjectCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = [
			'title',
			'genre',
			'short_description',

		]


post_detail_url = HyperlinkedIdentityField(
		view_name='projects-api:project-detail',
		lookup_field='pk'
		)



class ProjectDetailSerializer(ModelSerializer):
	url = post_detail_url
	user = SerializerMethodField()
	audio_file = SerializerMethodField()
	class Meta:
		model = Project
		fields = [
			'url',
			'id',
			'user',
			'title',
			'genre',
			'short_description',
			'audio_file',
		]

	def get_user(self, obj):
		return str(obj.user.username)


	def get_audio_file(self, obj):
		try:
			audio_file = obj.audio_file.url
		except:
			audio_file = None

		return audio_file


class ProjectListSerializer(ModelSerializer):
	url = post_detail_url
	user = SerializerMethodField()
	class Meta:
		model = Project
		fields = [
			'url',
			'id',
			'user',
			'title',
			'genre',
			'short_description',


		]

	def get_user(self, obj):
		return str(obj.user.username)




class ProjectMatchSerializer(ModelSerializer):
	user_a = SerializerMethodField()
	user_b = SerializerMethodField()
	class Meta:
		model = ProjectMatch
		fields = [
			'id',
			'user_a',
			'user_b',
			'project_a',
			'project_b',
			'user_a_positive_feedback',
			'user_a_negative_feedback',
			'user_a_like',
			'user_b_positive_feedback',
			'user_b_negative_feedback',
			'user_b_like',
			'active',
			'timestamp',

		]

	def get_user_a(self, obj):
		return str(obj.user_a.username)

	def get_user_b(self, obj):
		return str(obj.user_b.username)



