from django.db import models

# Here we deal with Database and Tables

# Here is a table called Post with its attriutes
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title