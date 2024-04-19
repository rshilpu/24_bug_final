from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth.views import LoginView,LogoutView,ManagerRegisterView
from .views import UpdateStatusView,UserLogoutView,ManagerDashboardView,DeveloperDashboardView,ProjectReport,ManagerDashboardView,DeveloperRegisterView,ManagerRegisterView


urlpatterns = [
    
    path("manager_register/",views.ManagerRegisterView.as_view(),name="manager_register"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    
    path("developer_register/",DeveloperRegisterView.as_view(),name="developer_register"),
    path("manager_dashboard/",views.ManagerDashboradView.as_view(),name="manager_dashboard"),
    path("developer_dashboard/",DeveloperDashboardView.as_view(),name="developer_dashboard"),
    
    
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),
    path("sendmail/",views.sendMail,name="sendmail"),
    path("developer_dashboard/",views.DeveloperDashboardView.as_view(),name="developer_dashboard"),
    #----------------------------------Update status view-----------------------
    path("updatestatustask/<int:pk>/",views.UpdateStatusView.as_view(),name="update_status"),

    #----------------------------------Report-----------------------------------
    
    path("reports/<int:pk>/",views.ProjectReport,name="Report"),
    
]