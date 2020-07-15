from django.test import TestCase
from .models import Dev,Site,tags

# Create your tests here.
class DevTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new editor and saving it
        self.brian= Dev(first_name = 'brian', last_name ='Kiiru', email ='briankiiru@gmail.com')
        self.brian.save_dev()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_website= Site(title = 'Test Site',tags = 'This is a random test site',dev = self.brian)
        self.new_website.save()

        self.new_website.tags.add(self.new_tag)

    def tearDown(self):
        Dev.objects.all().delete()
        tags.objects.all().delete()
        Site.objects.all().delete()

    def test_get_site_today(self):
        today_site = Site.todays_site()
        self.assertTrue(len(today_site)>0)