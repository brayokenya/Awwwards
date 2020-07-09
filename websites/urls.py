from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.site_of_day,name='siteToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_site,name = 'pastSite')

]

