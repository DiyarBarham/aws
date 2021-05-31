from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0

    #if request.method == 'POST':


    return render(request, 'index.html')

def process(request):
    if request.POST['Farm'] == 'Farm':
        request.session['gold'] += random.randint(10, 20)
    elif request.POST['Farm'] == 'Cave':
        request.session['gold'] += random.randint(5, 10)
    elif request.POST['Farm'] == 'House':
        request.session['gold'] += random.randint(2, 5)
    elif request.POST['Farm'] == 'Casino':
        request.session['gold'] += random.randint(-50, 50)

    return redirect('/')