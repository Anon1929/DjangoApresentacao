from django.contrib import admin
from projects.models import *

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

# Register your models here.
