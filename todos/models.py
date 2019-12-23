from django.db import models
#DataFlair Models
class Todo(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    def __str__(self):
       return self.title