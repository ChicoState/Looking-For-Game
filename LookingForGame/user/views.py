from django.shortcuts import render, redirect
from user.forms import UserPreferences
from . import forms
from user.models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
def user(request):
    print(request.user)
    a = UserProfile.objects.all().__dict__
    #print(a)
    #print("Printed a \n")
    page_data = a #{'a': '1', 'b' : '2', 'c': '3'}#
    return render(request, "user/preferences.html", page_data)

#@login_required(login_url='/login/')
def preferences(request):
    if request.method == 'POST':
        user_form = UserPreferences(request.POST)

        if user_form.is_valid():

            if request.user.is_authenticated:
                a = UserProfile.objects.get(id=request.user)
                user = UserPreferences(request.POST, instance=a)
                user.save()
            else:
                user_form.save()
            #user.save()
            return redirect("/")
        else:
            page_data = {'user_form' : user_form}
            return render(request, 'user/update_preferences.html', page_data)

    else:
        user_form = forms.UserPreferences()
        page_data = {'user_form': user_form}
        return render(request, 'user/update_preferences.html', page_data)

    #eturn render(request, 'user/index.html', {'user_form':user_form}, page_data)
