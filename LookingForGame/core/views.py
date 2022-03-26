from core.forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from core.models import Group
from . import models
from . import forms
from user.models import UserProfile
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def home(request):
    if(request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Group.objects.filter(id=id).delete()
        return redirect("/")
    #print(request.user)
    groups = Group.objects.filter(game_master=request.user).values()
    #print(groups)
    context = {'page_data' : groups}
    return render(request, "core/home.html", context)

def about_us(request):
    return render(request, "core/about.html")

@login_required(login_url='/login/')
def lfg(request):
    if(request.method == "POST"):
        print("joining!")
        return render(request, "component/request_group.html");

    groups = Group.objects.all().values()
    context = {'page_data' : groups}
    return render(request, "core/lfg.html", context)

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'component/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'component/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'component/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'component/login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")

@login_required(login_url='/login/')
def create_group(request):
    if (request.method == "POST"):
        group_form = forms.CreateGroupForm(request.POST)
        if (group_form.is_valid()):

            # Save form data to DB
            user_form = group_form.save(commit=False)
            user = request.user
            user_form.game_master = user.username
            user_form.save()
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "group_form": group_form }
            return render(request, 'component/create_group.html', page_data)
    else:
        group_form = forms.CreateGroupForm()
        page_data = { "group_form": group_form }
        return render(request, 'component/create_group.html', page_data)
