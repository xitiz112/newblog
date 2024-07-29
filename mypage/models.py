from django.db import models

# Create your models here.




class Page(models.Model):
    title=models.CharField(blank=True,null=True,max_length=200)
    content=models.TextField(blank=True,null=True)
    slug=models.SlugField(null=True,)




    def __str__(self):
        return self.title
    




