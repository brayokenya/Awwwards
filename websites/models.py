from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    phone_number = models.CharField(max_length = 10,blank =True)
    bio = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.first_name

    def save_userprofile(self):
        self.save()  

    def delete_userprofile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()



class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    

class Site(models.Model):
    title = models.CharField(max_length =60)
    image = CloudinaryField(default='screenshot')
    url = models.URLField(max_length=200, default='websiteurl')
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    creativity = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)
    

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
    
    def __str__(self):
        return (self.title)


    def save_site(self):
        self.save()  

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='likes', null=True)
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    creativity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    average = models.IntegerField(default=0)

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    class Meta:
        db_table = 'ratings'

