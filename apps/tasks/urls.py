from django.urls import path
from apps.tasks.views.tag_view import TagView, TagDetailApiView
from apps.tasks.views.task_view import AllTasksListAPIView, TasksDetailAPIView

urlpatterns = [
    path('tags/', TagView.as_view(), name='tags'),
    path('tags/<int:pk>', TagDetailApiView.as_view(), name='tag'),
    path('', AllTasksListAPIView.as_view(), name='tasks'),
    path('<int:pk>/', TasksDetailAPIView.as_view(), name='tasks_detail'),


]
