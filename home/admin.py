from django.contrib import admin
from .models import User, Project, Skill, CompletedCourse, UncompletedCourse
# Register your models here.


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(CompletedCourse)
admin.site.register(UncompletedCourse)
