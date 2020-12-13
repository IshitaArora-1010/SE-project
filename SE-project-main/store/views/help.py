from django.shortcuts import render

def Help(request):
    return render(request, 'help.html')