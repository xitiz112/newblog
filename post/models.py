from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

STATUS = (
     (0,"draft"),
     (1,"publish")
     )

class Post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    image=models.ImageField(upload_to= 'uploads')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_post")
    content=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    status= models.IntegerField(choices=STATUS,default=0)
    category=models.ForeignKey('Category',blank=True,null=True,on_delete=models.CASCADE)




    class meta:
        ordering=['-created']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": int(self.pk)})


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)


    class meta:
        ordering=['-created']

    def __str__(self):
        return "Comment {} by {}".format(self.body,self.name)
    


    







