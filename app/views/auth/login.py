from django.views import View
from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from django.contrib import messages

class login_view (View) : 
    def get (self, request, **kwargs) : 
        return render(request,'login.html')
    
    def post (sef, request, **kwargs) : 
        data = {
            'email' : request.POST.get('email', None), 
            'password' : request.POST.get('password', None), 
        }
        action = Action(
            url = MAIN_URL + '/user/auth/login/',
            data = data
        )
        action.post()
        
        response = action.json_data()
        if action.is_valid() :
            res = redirect('profile')
            res.set_cookie('user', response['token'])
            return res
        
        messages.error(request, response['message'][0])
        return redirect('login')
            