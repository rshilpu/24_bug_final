from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth.views import LoginView,LogoutView
from .views import UpdateStatusView,ProjectReport


urlpatterns = [
    
    path("manager-register/",views.ManagerRegisterView.as_view(),name="manager-register"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("manager-dashboard/",views.ManagerDashboradView.as_view(),name="manager-dashboard"),
    path("developer-register/",views.DeveloperRegisterView.as_view(),name="developer-register"),
    
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),
    path("sendmail/",views.sendMail,name="sendmail"),
    path("developer_dashboard/",views.DeveloperDashboardView.as_view(),name="developer_dashboard"),
    #----------------------------------Update status view-----------------------
    path("updatestatustask/<int:pk>/",views.UpdateStatusView.as_view(),name="update_status"),

    #----------------------------------Report-----------------------------------
    
    path("reports/<int:pk>/",views.ProjectReport,name="Report"),
    
]