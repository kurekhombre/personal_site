from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=128, default="-")
    description = models.CharField(max_length=300)
    github_link = models.URLField(null=True, blank=True)
    live_link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/')
    technologies = models.ManyToManyField('Technology')
    added = models.DateTimeField(auto_created=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Technology(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


