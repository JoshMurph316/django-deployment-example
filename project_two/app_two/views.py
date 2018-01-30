from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User
from app_two.forms import UserForm

def index(req):
    return HttpResponse('<h1>App Two</h1> <a href="/users">Users</a> <br> <a href="/help">Help</a>')

def help(req):
    help_dict = {'help_text': 'this is some helpful text'}
    return render(req, 'app_two/index.html', context=help_dict)

def users(req):
    user_list = User.objects.order_by('last_name')
    form = UserForm()
    users_dict = {'users': user_list, 'form': form}

    if req.method == 'POST':
        form = UserForm(req.POST)
        new_user = form.save()

    return render(req, 'app_two/users.html', context=users_dict)
