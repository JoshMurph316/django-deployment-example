from django.shortcuts import render
from app_five.forms import UserForm, UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(req):
    return render(req, 'app_five/index.html')

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))

def register(req):

    registered = False

    if req.method == 'POST':
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileInfoForm(data=req.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context_dict = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered
                    }
    print('registered: ', registered)
    return render(req, 'app_five/registration.html', context=context_dict)

def user_login(req):

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(req, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Accout Inactive')
        else:
            print('Failed login: {}'.format(username))
            return HttpResponse('invalid login')

    else:
        return render(req, 'app_five/login.html', {})
