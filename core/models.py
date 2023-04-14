from django.db import models
from django.contrib import admin

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Settings(AbstractModel):
    logo = models.ImageField(upload_to='media/Settings/logo')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    contact_text = models.TextField()
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    def __str__(self):
        return "Site Settings"
    
    class Meta:
        verbose_name_plural = ("Settings")


class AboutMe(AbstractModel):
    profile_photo = models.ImageField(upload_to='media/AboutMe/profile_photo')
    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    p4 = models.TextField()


    def __str__(self):
        return "About Me"
    
    class Meta:
        verbose_name_plural = ("AboutMe")

class Services(AbstractModel):
    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()

    def __str__(self):
        return "Services"
    
    class Meta:
        verbose_name_plural = ("Services")


class Experience(AbstractModel):
    works = models.IntegerField()
    experience = models.IntegerField()
    clients = models.IntegerField()
    awards = models.IntegerField()

    def __str__(self):
        return "Experience"
    
    class Meta:
        verbose_name_plural = ("Experience")


class ProjectCategory(AbstractModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ("ProjectCategory")


class Project(AbstractModel):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    year = models.IntegerField()
    project_link = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Image(AbstractModel):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/Image/project')
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.projects.title
