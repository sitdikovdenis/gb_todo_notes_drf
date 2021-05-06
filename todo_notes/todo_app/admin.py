from django.contrib import admin

from .models import Project, TODO


class ProjectAdmin(admin.ModelAdmin):
    pass


class TODOAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(TODO, TODOAdmin)
