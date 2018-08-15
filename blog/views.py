from django.shortcuts import render, redirect
from django.http import HttpResponse

sess = None

# render(request, the webpage you want to render, dict of content)
def index(request):
    return render(request, 'blog/home.html', {'sess':sess})
    
def about(request):
    return render(request, 'blog/basic.html', {
    'contact_content':['If you would like to contact me, please email me:', 'soapwang@gmail.com'], 'sess':sess})
    
def signin(request):
    return render(request, 'blog/signin.html', {'sess':sess})
    
def signin_auth(request):
    request.session['user_id'] = 'admin'
    global sess
    sess = 'admin'
    return redirect('index') 