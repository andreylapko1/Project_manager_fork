from urllib import request

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.tasks.models import Task
from apps.tasks.serializers.tasks_serializers import AllTasksSerializer, CreateUpdateTaskSerializer, \
    TaskDetailSerializer


class TasksListPaginator(PageNumberPagination):
    max_page_size = 30
    page_size = 5


class AllTasksListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    pagination_class = TasksListPaginator

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTasksSerializer
        elif self.request.method == 'POST':
            return CreateUpdateTaskSerializer

    def filter_queryset(self, queryset):
        project_name = self.request.query_params.get('project')
        employee_name = self.request.query_params.get('employee')
        if project_name:
            queryset = queryset.filter(project__name=project_name)
        if employee_name:
            queryset = queryset.filter(assignee__name=employee_name)
        return queryset


class TasksDetailAPIView(RetrieveAPIView):
    pagination_class = TasksListPaginator
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskDetailSerializer
        if self.request.method in ['UPDATE', 'DELETE', 'PUT']:
            return CreateUpdateTaskSerializer

