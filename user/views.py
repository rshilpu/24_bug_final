from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from project.models import Project
from django.contrib.auth import get_user_model
from project.models import Project,UserTask,Task,Bug,ProjectModule,Status
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Sum



# Create your views here.
class ManagerRegisterView(CreateView):
    template_name = 'user/manager_register.html'
    model = User
    form_class = ManagerRegistrationForm
    success_url = '/user/login/'
    def form_valid(self,form):
        email = form.cleaned_data.get("email")
        if sendMail(email):
            print("Mail Sent Successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)


class DeveloperRegisterView(CreateView):
    template_name = 'user/developer_register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/user/login/'


    def form_valid(self,form):
        email = form.cleaned_data.get("email")
        if sendMail(email):
            print("Mail Sent Successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)

def sendMail(to):
    subject = "Welcome to TimeTracking"
    message = "Hope You are enjoying your Django Tutorials"
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER

    send_mail(subject,message,EMAIL_FROM,recepientList)  # attach file # html - search
    return True
    # return HttpResponse('Email Sent')
    
class UserLoginView(LoginView):
    template_name = "user/login.html"
    model = User

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return "/user/manager-dashboard"
            elif self.request.user.is_developer:
                return "/user/developer-dashboard"

class ManagerDashboradView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        total_task = Task.objects.count()
        total_projects = Project.objects.count()
        total_module = ProjectModule.objects.count()
        total_developer = User.objects.filter(is_developer = True).count()
        project = Project.objects.all() #select * from project
        # project = ProjectModule.objects.all()
        project_module = ProjectModule.objects.all()
        task = Task.objects.all()
        usertask = UserTask.objects.all()
        bug = Bug.objects.all()
      
        
        tasks_with_developers = []
        tasks = Task.objects.all()
        for task in tasks:
            user_task = UserTask.objects.filter(task=task).first()
            developer_name = user_task.user.username if user_task else None
           
            tasks_with_developers.append({'task': task, 'developer_name': developer_name  })
        # status = Status.objects.all()
        return render(request,"user/manager_dashboard.html",{
            'total_task': total_task,
            'total_developer':total_developer,
            'total_module': total_module,
            'total_projects': total_projects,
            'project':project,
            'project_module': project_module,
            'task': task,
            'usertask':usertask,
            'tasks_with_developers': tasks_with_developers,
            'bug': bug,
            # 'status': status,
            
        })
        
    
    template_name = "user/manager_dashboard.html"
    # context_object_name = "tasks_with_users"
    
class DeveloperDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        user_tasks = UserTask.objects.filter(user=request.user)
        total_task = Task.objects.count()
        total_projects = Project.objects.count()
        total_module = ProjectModule.objects.count()
        total_developer = User.objects.filter(is_developer = True).count()
        project = Project.objects.all() #select * from project
        # project = ProjectModule.objects.all()
        project_module = ProjectModule.objects.all()
        task = Task.objects.all()#Filter task for the current developer
        bug = Bug.objects.all()
      
        return render(request,"user/developer_dashboard.html",{
            'user_tasks':user_tasks,
            'total_task': total_task,
            'total_developer':total_developer,
            'total_module': total_module,
            'total_projects': total_projects,
            'project':project,
            'project_module': project_module,
            'task': task,
            'bug': bug,
        })
    
    template_name = "user/developer_dashboard.html"
 
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("Email...",email)
        if sendMail(email):
            print("Mail sent successfully..")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
  
class UpdateStatusView(View):    
    def post(self,request,pk):
        print("Pk...",pk)          
        task = Task.objects.get(id=pk)
        print("Task....",task)          
        print("Task Updated..") 
        #task.status.statusName = "In-progress"   In-progress  Not-started Completed
        if task.status == "Not-started":
            print("not started")            
            task.status = "In-progress"            
        elif task.status == "In-progress":
            task.status = "Completed"
        
        task.save()
        return redirect(reverse('developer_dashboard')) #lazy reverse

#-----------------------------------Report---------------------------
def ProjectReport(request,pk):
    
    usertasks = UserTask.objects.get(pk=pk)
    projects = Project.objects.get(pk=pk)
    project_data = []
    
    modules = ProjectModule.objects.filter(project=projects)
    project_time = projects.estimatedHours
        
    module_data = []
    for module in modules:
            tasks  = Task.objects.filter(module=module)
            module_time = tasks.aggregate(Sum('totalMinutes'))['totalMinutes__sum'] or 0
            module_data.append({
                'module_name': module.moduleName,
                'module_status': module.status,                
                'module_time': module.estimatedHours,
                'tasks': tasks                
            })	
            project_time += module_time
        
    project_data.append({
            'project_name': projects.name,
            'project_time': project_time,
            'modules' :module_data
        })
    return render(request,'user/report.html',{'projects': project_data,'usertasks':usertasks})