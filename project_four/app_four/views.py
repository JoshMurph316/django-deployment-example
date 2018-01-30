from django.shortcuts import render

def index(req):
    context_dict = {
                    'text': 'hello world',
                    'number': 100
                    }

    return render(req, 'app_four/index.html', context_dict)

def other(req):
    return render(req, 'app_four/other.html')

def info(req):
    return render(req, 'app_four/url_info.html')
