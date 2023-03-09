from django.shortcuts import render
import random
# Create your views here.

def main(request):
    return render(request, 'index.html')

def password(request):
    charters =list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        charters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('specials'):
        charters.extend(list('!@#$%^&*()[]{}+-/'))
    if request.GET.get('numbers'):
        charters.extend(list('1234567890'))

    lenght=  int(request.GET.get('lenght'))
    thepassword =''

    for x in range(lenght):
        thepassword += random.choice(charters)
    return render(request, 'password.html', {'password' : thepassword})

def about(request):
    return render(request, 'about.html')