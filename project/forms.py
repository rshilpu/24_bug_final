from django import forms
from .models import Project,ProjectTeam,Status,Bug,ProjectModule,Task,Books,UserTask
from .models import User
class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'})
        }
       
class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_manager=True))
    class Meta:
        model = ProjectTeam
        fields = '__all__'
       
class ProjectModuleCreationForm(forms.ModelForm):
   
   class Meta:
        model = ProjectModule
        fields = ['project', 'moduleName', 'description', 'estimatedMinutes', 'status', 'startDate', 'totalUtilMinutes']
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'})
        }

class ProjectStatusCreationForm(forms.ModelForm):
    class Meta:
       model = Status
       fields = '__all__'

class ProjectTaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Books
        fields ='__all__' 


class TaskAssignForm(forms.ModelForm):
    developer = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))

    class Meta:
        model = Task
        fields = ['module', 'project', 'status', 'task_name', 'priority', 'description', 'estimatedMinutes', 'totalUtilMinutes', 'developer']

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
class UserTaskCreationForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = '__all__'
class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
class BugCreationForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = '__all__'
        