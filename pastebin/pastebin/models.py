from django.db import models

class Paste(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
