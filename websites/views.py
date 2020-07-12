from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Site, UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import NewSiteForm,UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout





# Create your views here.
def site_today(request):
    date = dt.date.today()
    site = Site.todays_site()
    return render(request, 'all-sites/today-sites.html', {"date": date,"site":site})


def site_of_day(request):
    date = dt.date.today()
    return render(request, 'all-sites/today-sites.html', {"date": date})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_site(request,past_date):

        # Converts data from the string Url

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(site_today)

    site = Site.days_site(date)
    return render(request, 'all-sites/past-sites.html',{"date": date,"site":site})

def search_results(request):

    if 'site' in request.GET and request.GET["site"]:
        search_term = request.GET.get("site")
        searched_websites = Site.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-sites/search.html',{"message":message,"websites": searched_websites})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-sites/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def site(request,site_id):
    try:
        site= Site.objects.get(id = site_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-sites/site.html", {"site":site})


@login_required(login_url='/accounts/login/')
def new_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewSiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False)
            site.developer = current_user
            site.save()
        return HttpResponseRedirect('/')

    else:
        form = NewSiteForm()
    return render(request, 'new-site.html', {"form": form})

@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = UserProfile.objects.get(user_id=user)
    sites = Site.objects.filter(profile__id=id)[::-1]
    return render(request, "websites/profile.html", context={"user":user,
                                                             "profile":profile,
                                                             "sites":sites})


def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("siteToday"))
            else:
                return HttpResponseRedirect(reverse("user_login")) #raise error/ flash

        else:
            return HttpResponseRedirect(reverse("user_login")) #raise error/ flash
    else:
        return render(request, "auth/login.html", context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))


def register(request):
    registered = False
    

    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = UserProfile()
            user_profile.user = user
            # user_profile.save()
            user_profile.save()
            registered = True
            

            return HttpResponseRedirect(reverse("user_login"))

        else:
            pass

    else:
        user_form = UserForm()
        

    return render(request, "auth/register.html", context={"user_form":user_form,
                                                          "registered":registered})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect(my_profile)

    else:
        form = UserProfileForm()
    return render(request, 'create-profile.html', {"form": form})



@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    user_profile = UserProfile.objects.get(user=current_user)
    profile_pic = user_profile.profile_pic
    user_bio = user_profile.bio

    
    try:
        profile = UserProfile.objects.filter(user = current_user)
    except UserProfile.DoesNotExist:
        return redirect(create_profile)
    site = Site.objects.filter(developer=current_user)
    
       

    return render(request, 'my-profile.html', { "profile_pic":profile_pic,"site": site, "user_bio": user_bio},)

