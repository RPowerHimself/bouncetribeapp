from django.db.models import Q

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	)



from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,

	)

from projects.models import MatchChatMessage, Project, ProjectMatch 

from .pagination import ProjectLimitOffsetPagination, ProjectPageNumberPagination
from .permissions import IsOwnerOrReadOnly

from .serializers import (
	MatchChatMessageCreateUpdateSerializer,
	MatchChatMessageSerializer,
	ProjectCreateUpdateSerializer,
	ProjectDetailSerializer,
	ProjectListSerializer,
	ProjectMatchSerializer,
	)



class MatchChatMessageCreateAPIView(CreateAPIView):
	queryset = MatchChatMessage.objects.all()
	serializer_class = MatchChatMessageCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class MatchChatMessageDetailAPIView(RetrieveAPIView):
	queryset = MatchChatMessage.objects.all()
	serializer_class = MatchChatMessageSerializer


class MatchChatMessageListAPIView(ListAPIView):
	serializer_class = MatchChatMessageSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['user', 'session', 'message']
	pagination_class = ProjectPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list = MatchChatMessage.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(user__icontains=query)|
				Q(session__icontains=query)|
				Q(message__icontains=query)
				).distinct()
		return queryset_list






class ProjectCreateAPIView(CreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)



class ProjectDetailAPIView(RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectDetailSerializer
	# lookup_field = 'slug'


class ProjectUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectCreateUpdateSerializer
	# lookup_field = 'slug'
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class ProjectDeleteAPIView(DestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectDetailSerializer
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
	# lookup_field = 'slug'


class ProjectListAPIView(ListAPIView):
	serializer_class = ProjectListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'user', 'genre']
	pagination_class = ProjectPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list = Project.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(genre__icontains=query)
				).distinct()
		return queryset_list




class ProjectMatchDetailAPIView(RetrieveAPIView):
	queryset = ProjectMatch.objects.all()
	serializer_class = ProjectMatchSerializer


class ProjectMatchListAPIView(ListAPIView):
	serializer_class = ProjectMatchSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['project_a', 'project_b']
	pagination_class = ProjectPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list = ProjectMatch.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(project_a__icontains=query)|
				Q(project_b__icontains=query)
				).distinct()
		return queryset_list







