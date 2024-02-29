from django.db import models

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    postedon = models.DateTimeField(auto_now_add = True)
    views = models.IntegerField(default = 0)
    author = models.ForeignKey("auth_manager.CustomUser", on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title