from django.contrib import admin
from .models import Project,module,ptask,UserTask,Status,Task,ProjectTeam,ProjectModule

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTeam)
admin.site.register(ProjectModule)
admin.site.register(module)
admin.site.register(ptask)
admin.site.register(UserTask)
admin.site.register(Status)
admin.site.register(Task)