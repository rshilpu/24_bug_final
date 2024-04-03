from django.contrib import admin
from django.urls import path,include
from . views import *
from django.contrib.auth.views import LogoutView
# from .views import ProjectReport
from .import views



urlpatterns = [
 
    path("create/",ProjectCreationView.as_view(),name="project_create"),
    path("list/",ProjectListView.as_view(),name="project_list"),
    path("edit/<int:pk>/",ProjectEditView.as_view(),name="project_edit"),
    path("detail/<int:pk>/",ProjectDetailView.as_view(),name="project_detail"),
    path("delete/<int:pk>/",ProjectDeleteView.as_view(),name="project_delete"),
    path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create") ,
    path("create_status/",ProjectStatusCreateView.as_view(),name="project_status_create"),
    path("create_module/",ProjectModuleCreateView.as_view(),name="module_create"),
    path("edit_module/<int:pk>",ProjectModuleEditView.as_view(),name="module_edit"),
    path("detail_module/<int:pk>/",ProjectModuleDetailView.as_view(),name="module_detail"),
    path("delete_module/<int:pk>/",ProjectModuleDeleteView.as_view(),name="module_delete"),
    path("create_task/",ProjectTaskCreateView.as_view(),name="task_create"),
    path("edit_task/<int:pk>",ProjectTaskEditView.as_view(),name="task_edit"),
    path("detail_task/<int:pk>/",ProjectTaskDetailView.as_view(),name="task_detail"),
    path("delete_task/<int:pk>/",ProjectTaskDeleteView.as_view(),name="task_delete"),
    path ("chart/",views.pieChart,name="chart"),
    path("usertask_create/",UserTaskCreationView.as_view(),name="UserTask"),
    path("usertask_list/",UserTaskListView.as_view(),name="UserTaskList"),
    
    path("list_modules/",ProjectModuleListViews.as_view(),name="ListModuleProjects"),
    
    path("book_create/",BookCreateView.as_view(),name="book_create"),
    path("book_list/",views.BookListView.as_view(),name="book_list"),
    path('assign-task/', AssignTaskView.as_view(), name='assign_task'),
    path("task_list/",views.TaskListView.as_view(),name="task_list"), 
   path('reports/<int:pk>/', views.ProjectReport, name='Report'),


 
]
    