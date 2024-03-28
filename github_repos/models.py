from django.db import models

class githubRepo(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.name