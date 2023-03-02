from django.db import models
from django.utils.text import slugify

class post(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    date=models.DateTimeField(auto_now=True)
    imgUrl=models.CharField(max_length=50)
    isactive=models.BooleanField()
    slug=models.SlugField(unique=True,db_index=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(args,kwargs)

    def __str__(self):
        return f"{self.title}"
class catogories(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField()
