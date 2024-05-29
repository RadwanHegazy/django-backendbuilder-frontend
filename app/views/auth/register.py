from django.views import View
from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from django.contrib import messages

class register_view (View) : 
    def get (self, request, **kwargs) : 
        return render(request,'register.html')
    
    def post (sef, request, **kwargs) : 
        data = {
            'full_name' : request.POST.get('full_name', None), 
            'email' : request.POST.get('email', None), 
            'password' : request.POST.get('password', None), 
        }
        action = Action(
            url = MAIN_URL + '/user/auth/register/',
            data = data
        )
        action.post()
        
        response = action.json_data()
        if action.is_valid() :
            res = redirect('profile')
            res.set_cookie('user', response['token'])
            return res
        
        messages.error(request, 'an error accoured when registeration')
        return redirect('register')