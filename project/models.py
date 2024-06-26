from django.db import models
from user.models import User
from django.shortcuts import render


# Create your models here.
techChoices = (
("Python","Python"),
("Java","Java"),
("C++","C++"),
("C#","C#"),
)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=techChoices)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.name   

def calendar_view(request):
    projects = Project.objects.all()
    events = []
    for project in projects:
        events.append({
            'title': project.name,
            'start': project.startDate.strftime('%Y-%m-%d'),
            'end': project.endDate.strftime('%Y-%m-%d'),
        })
    return render(request, 'calendar.html', {'events': events}) 

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "projectteam"
    
    def __str__(self):
        return self.user.username
    
statusChoices = (
    ("Not-started","Not-started"),
    ("In-progress","In-progress"),
    ("Testing","Testing"),
    ("Completed","Completed"),
)
    
class Status(models.Model):
    status_name = models.CharField(max_length=100)

    class Meta:
        db_table = "status"
    
    def __str__(self):
        return self.status_name
    
    def update_status(self, new_status_name):
        self.status_name = new_status_name
        self.save()

class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=100)
    description = models.TextField()
    estimatedMinutes = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    startDate = models.DateField()
    totalUtilMinutes = models.IntegerField()
    class Meta:
        db_table = "projectmodule"

    def __str__(self) -> str:
        return self.moduleName
class Task(models.Model):
    module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    description = models.TextField()
    estimatedMinutes = models.IntegerField()
    totalUtilMinutes = models.IntegerField()

    class Meta:
        db_table = "task"

    class Meta:
        db_table = "project_module"

priorityChoices = (
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low"),
)

    
class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    class Meta:
        db_table="user_task"
        
    def __str__(self):
        # return self.user.username
        return self.task.task_name + " -> " + self.user.username
    # def __str__(self):
    #     #return self.user.username
    #     return self.task.title +" - "+ self.user.username


class module(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "module"
        
    def __str__(self):
        return self.name

class ptask(models.Model):
    task_name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        db_table = "ptask"
        
    def __str__(self):
        return self.task_name

class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    bookImage = models.ImageField(upload_to="uploads/")
    class Meta:
        db_table = "books"
    
    def __str__(self):
        return self.name
class Bug(models.Model):
    project_module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    bug_name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100, choices=priorityChoices)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    totalMinutes = models.PositiveIntegerField()
    is_assigned = models.BooleanField(default=False)

    class Meta:
        db_table = "bug"
        
    def __str__(self):
        return self.bug_name
    
