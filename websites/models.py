from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt




# Create your models here.
class Dev(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name

    def save_dev(self):
        self.save()
    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Site(models.Model):
    title = models.CharField(max_length =60)
    image = CloudinaryField(default='screenshot')
    url = models.URLField(max_length=200, default='websiteurl')
    developer = models.ForeignKey(Dev, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def todays_site(cls):
        today = dt.date.today()
        site = cls.objects.filter(pub_date__date = today)
        return site

    @classmethod
    def days_site(cls,date):
        site = cls.objects.filter(pub_date__date = date)
        return site

    @classmethod
    def search_by_title(cls,search_term):
        site = cls.objects.filter(title__icontains=search_term)
        return site