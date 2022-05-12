from core.forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from core.models import Group, PendingGroup
from . import models
from . import forms
from user.models import UserProfile
from django.contrib.auth.models import User

def index(request):
    return render(request, "core/index.html")

@login_required(login_url='/login/')
def profile(request):
    if(request.method == "GET" and "delete" in request.GET):
        #id = request.GET["delete"]
        Group.objects.filter(id=id).delete()
        return redirect("core/profile.html")
    #print(request.user)
    groups = Group.objects.filter(game_master=request.user).values()
    pending_groups = PendingGroup.objects.filter(users=request.user)
    print(pending_groups)
    #print(groups)
    context = {'page_data' : groups,
               'pending_groups' : pending_groups}
    return render(request, "core/profile.html", context)

@login_required(login_url='/login/')
def profile_groupview(request, id):
    #print(request.user)
    group = list(Group.objects.filter(id=id).values())


    #print(groups)
    context = {'page_data' : group}
    return render(request, "component/groupview.html", context)

@login_required(login_url='/login/')
def profile_del(request, id):

    Group.objects.filter(id=id).delete()
    groups = Group.objects.filter(game_master=request.user).values()
    pending_groups = PendingGroup.objects.filter(users=request.user)
    context = {'page_data' : groups,
               'pending_groups' : pending_groups}
    return render(request, "core/profile.html", context)

def about_us(request):
    return render(request, "core/about.html")

@login_required(login_url='/login/')
def lfg(request):
    #if(request.method == "POST"):
        #return render(request, "component/request_group.html");
    groups = Group.objects.all().values()
    context = {'page_data' : groups}
    return render(request, "core/lfg.html", context)

@login_required(login_url='/login/')
def lfg_group(request, id):
    if(request.method == "POST"):
        #add to group here
        print("REQUESTER ID:" + str(request.user.id))
        print("Group id: " + str(id))
        pendinggroup = list(Group.objects.filter(id=id).values())
        gm = pendinggroup[0]['game_master']
        print(pendinggroup)
        cur_lead = User.objects.get(username=gm)
        group = Group.objects.get(id=id)

        pg_id = str(gm) + str(id)
        print(pg_id)
        pg = PendingGroup.objects.filter(pending_group_id=pg_id)
        if(pg.exists()):
            #add

            pg = PendingGroup.objects.get(pending_group_id=pg_id)
            print("it exists")
            #print(pg.values()[0]['id'])


            pg.users.add(User.objects.get(id=request.user.id))
            pg.save()
            #pgall = PendingGroup.objects.all()
            #print(pgall)
        else:
            #create
            print("doesn't exist")
            groupid= Group.objects.get(id=id)
            pg = PendingGroup.objects.create(pending_group_id=pg_id, group_leader=cur_lead, group=groupid)
            pg.save()
            pg.users.add(User.objects.get(id=request.user.id))
            pg.save()
            #print(pg.users)
            #print(pg)

        context = {'page_data' : pendinggroup}
        return render(request, "component/request_group.html", context);
    groups = Group.objects.all().values()
    context = {'page_data' : groups}
    return render(request, "core/lfg.html", context)

@login_required(login_url='/login/')
def sort_age(request, age):
    if(request.method == "POST"):
        return render(request, "component/request_group.html");
    if(age != "any"):
        groups = Group.objects.filter(age_minimum=age).values()
    else:
        groups = Group.objects.all().values()

    context = {'page_data' : groups}
    return render(request, "core/lfg.html", context)

@login_required(login_url='/login/')
def sort_exp(request, exp):
    if(request.method == "POST"):
        return render(request, "component/request_group.html");
    if(exp != "any"):
        groups = Group.objects.filter(experience_level=exp).values()
    else:
        groups = Group.objects.all().values()
    context = {'page_data' : groups}
    return render(request, "core/lfg.html", context)

@login_required(login_url='/login/')
def sort_players(request, players):
    if(request.method == "POST"):
        return render(request, "component/request_group.html");
    if(players != "any"):
        groups = Group.objects.filter(group_size=players).values()
    else:
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
            group_list = models.Group.objects.all()
            user_form.group_number = len(group_list) + 1
            user_form.save()
            return redirect("/lfg")
        else:
            # Form invalid, print errors to console
            page_data = { "group_form": group_form }
            return render(request, 'component/create_group.html', page_data)
    else:
        group_form = forms.CreateGroupForm()
        page_data = { "group_form": group_form }
        return render(request, 'component/create_group.html', page_data)

# room_name is the group ID
def group_page(request, pk):
    return render(request, 'core/group_page.html', {
        'room_name': pk
    })
