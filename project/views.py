from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import ProjectCreationForm,ProjectTeam,TaskAssignForm
from .models import Project, Status, ProjectModule,Task, module,Bug
from .forms import ProjectTeamCreationForm,BookCreationForm, BugCreationForm,ProjectStatusCreationForm,ProjectModuleCreationForm, ProjectTaskCreationForm,UserTaskCreationForm
from .models import Books,User,UserTask,Task
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from .models import Project, ProjectModule, Task
from django.http import HttpResponseRedirect


# Create your views here.

class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'


def calendar_view(request):
    projects = Project.objects.all()
    events = []
    for project in projects:
        events.append({
            'title': project.name,
            'start': project.startDate.strftime('%Y-%m-%d'),
            'end': project.endDate.strftime('%Y-%m-%d'),
        })
    print(events)  # Print events to inspect its contents
    return render(request, 'calendar.html', {'events': events})

class ProjectListView(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'

class ProjectEditView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "project/edit.html"
    success_url = "/project/list"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/detail.html"
    context_object_name = "project"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/delete.html"
    success_url = "/project/list"

class ProjectTeamCreateView(CreateView):
    template_name = "project/create_team.html"
    model = ProjectTeam
    success_url = "/project/list/"
    form_class = ProjectTeamCreationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_id = self.request.GET.get('project_id')
        if project_id:
            project = get_object_or_404(Project, id=project_id)
            kwargs['initial']['project'] = project
        return kwargs
def project_team_view(request, id):
    project = ProjectTeam.objects.prefetch_related('user').filter(project_id=id)
    
    team_members = []
    for item in project:
        user = get_object_or_404(User, id=item.user_id)
        team_members.append({
            'username': user.username,
        })
        
    project = get_object_or_404(Project, id=id)
        
    return render(request, 'project/project_team.html', {'team_members': team_members, 'project' : project})

    
class ProjectStatusCreateView(CreateView):
    template_name = "project/status.html"
    model = Status
    success_url = "/project/list"
    form_class = ProjectStatusCreationForm
def taskStatusUpdateView(request,id):
    task = Task.objects.get(id=id)
    
    if task.status.status_name == "Not-started":
        task.status_id = 2
    elif task.status.status_name == "In-progress":
        task.status_id = 3
    elif task.status.status_name == "Testing":
        task.status_id = 4
        
    task.save()
    
    return redirect(reverse('developer_dashboard'))


class ProjectModuleCreateView(CreateView):
    template_name = "project/create_module.html"
    model = ProjectModule
    success_url = "/project/list"
    form_class = ProjectModuleCreationForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_id = self.request.GET.get('project_id')
        if project_id:
            project = get_object_or_404(Project, id=project_id)
            kwargs['initial']['project'] = project
        return kwargs
    
    

class ProjectModuleEditView(UpdateView):
    model = ProjectModule
    form_class = ProjectModuleCreationForm
    template_name = "project/edit_module.html"
    success_url = "/project/list"
class ProjectModuleListViews(ListView):
    template_name = 'project/list_project_modules.html'
    model =  ProjectModule
    context_object_name = 'modules'

class ProjectModuleDetailView(DetailView):
    model = ProjectModule
    template_name = "project/detail_module.html"
    context_object_name = "module"

class ProjectModuleDeleteView(DeleteView):
    model = ProjectModule
    template_name = "project/delete_module.html"
    success_url = "/project/list"

class ProjectTaskCreateView(CreateView):
    model = Task
    form_class = ProjectTaskCreationForm
    template_name = "project/create_task.html"
    success_url = "/project/list"

class ProjectTaskEditView(UpdateView):
    model = Task
    form_class = ProjectTaskCreationForm
    template_name = "project/edit_task.html"
    success_url = "/project/list"

class ProjectTaskDetailView(DetailView):
    model = Task
    template_name = "project/detail_task.html"
    context_object_name = "task"

class ProjectTaskDeleteView(DeleteView):
    model = Task
    template_name = "project/delete_task.html"
    success_url = "/project/list"

def pieChart(request):
    labels = []
    data = []
    
    module_queryset = module.objects.order_by('-id')[:5]  # Renaming the queryset variable
    print(module_queryset)
    for module_instance in module_queryset:  # Using a different name for the loop variable
        print(labels)
        data.append(module_instance.id)
    
    return render(request, 'project/pie_chart.html', {
        'labels': labels,
        'data': data
    })

class BookCreateView(CreateView):
    model = Books
    template_name = 'project/create_book.html'
    success_url = '/project/list/'
    form_class = BookCreationForm
        
class BookListView(ListView):
    template_name = 'project/book_list.html'
    success_url = '/project/list/'
    model = Books
    context_object_name = 'books' 
    
class AssignTaskView(CreateView):
    model = UserTask
    form_class = TaskAssignForm
    template_name = "project/task_assign.html"
    success_url = "/user/manager-dashboard"

class TaskListView(ListView):
    template_name = 'project/task_list.html'
    model = Task
    context_object_name = 'tasks'  
    
def task_list(request):
    tasks = Task.objects.all()  # Or filter based on your requirements
    context = {'tasks': tasks}
    return render(request, 'project/task_list.html', context)


class UserTaskCreationView(CreateView):
    model = UserTask
    form_class = UserTaskCreationForm
    template_name = 'project/user_task_create.html'
    success_url = '/project/list/'

class UserTaskListView(ListView):
    model = UserTask
    context_object_name = 'usertasks'
    template_name = 'project/user_task_list.html'
#-----------------------------------Report---------------------------

def ProjectReport(request, pk):
    # Retrieve the Project or return a 404 if it doesn't exist
    project = get_object_or_404(Project, pk=pk)
    
    # Count the number of modules for the project
    num_modules = project.projectmodule_set.count()
    
    # Count the total number of tasks for the project
    num_tasks = Task.objects.filter(project=project).count()
    
    # Fetch tasks done by developers for the project
    tasks_done_by_developers = UserTask.objects.filter(task__project=project)
    
    # Render the template with the project data
    return render(request, 'project/report.html', {
        'project': project,
        'num_modules': num_modules,
        'num_tasks': num_tasks,
        'tasks_done_by_developers': tasks_done_by_developers
    })

class BugListView(ListView):
    model = Bug
    template_name = "project/list_bug.html"
    context_object_name = "bug"
    

class BugCreationView(CreateView):
    model = Bug
    form_class = BugCreationForm
    template_name = "project/add_bug.html"
    success_url = "/project/list_bug"
    
class BugUpdateview(UpdateView):
    model = Bug
    form_class = BugCreationForm
    template_name = "project/update_bug.html"
    success_url = "/project/list_bug"
    
class BugDetailView(DetailView):
   model = Bug
   context_object_name = "bug"
   template_name = "project/detail_bug.html"
   
def delete_bug(request,id):
    bug = Bug.objects.get(id=id)
    
    bug.delete()
    
    return HttpResponseRedirect("/project/list_bug")
