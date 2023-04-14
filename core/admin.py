from django.contrib import admin

from .models import Experience, Image, Project, ProjectCategory, Services, Settings, AboutMe

# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')

admin.site.register(AboutMe)
admin.site.register(Services)
admin.site.register(Experience)
admin.site.register(ProjectCategory)
admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 6

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline,]