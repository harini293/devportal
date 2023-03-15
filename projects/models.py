from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_desc = models.TextField(max_length=1000, default=project_name)
    published_on = models.DateTimeField('date published')
    taken_by = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    srn = models.CharField(max_length=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
