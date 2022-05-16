from django.dispatch import receiver
from django.shortcuts import render, redirect
from user.forms import UserPreferences, MessageForm, ThreadForm
from . import forms
from user.models import UserProfile, MessageModel, ThreadModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import View
from django.contrib.auth.models import User


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

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads
        }

        return render(request, 'user/inbox.html', context)

class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form' : form
        }

        return render(request, 'component/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        #try:
        receiver = User.objects.get(username=username)
        if ThreadModel.objects.filter(user=request.user,receiver=receiver).exists():
            thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
            return redirect('thread', pk=thread.pk)
        elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
            thread=ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
            return redirect('thread', pk=thread.pk)

        if form.is_valid():
            thread = ThreadModel(
                user=request.user,
                receiver=receiver
            )
            thread.save()

            return redirect('thread', pk=thread.pk)
    #except:
        return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list=MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread' : thread,
            'form' : form,
            'message_list' : message_list
        }

        return render(request, 'component/thread.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver
        
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )

        message.save()
        return redirect('thread', pk=pk)
