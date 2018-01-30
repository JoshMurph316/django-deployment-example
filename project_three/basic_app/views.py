from django.shortcuts import render
from basic_app import forms

def index(req):
    return render(req, 'basic_app/index.html')

def form_name_view(req):
    form = forms.FormName()

    if req.method == 'POST':
        form = forms.FormName(req.POST)

        if form.is_valid():
            print('Success: ')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(req, 'basic_app/form.html', context={'form': form})
