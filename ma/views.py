from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={'text': '', 'text1': '', 'text2': '', 'text3': '', 'text4': ''})


