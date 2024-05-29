from django.views import View
from django.shortcuts import redirect, render
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class profile_view (View) : 
    
    @login_required
    def get (self, request, **kwargs):
        
        action = Action(
            url = MAIN_URL + '/endpoint/get/user/all/',
            headers=kwargs['headers']
        )

        action.get()

        print(action.json_data())
        
        context = {
            'endpoints' : action.json_data()
        }
        return render(request,'profile.html', context)
    
    @login_required
    def post (self, request, **kwargs) :
        data = {
            'name' : request.POST.get('name', None),
            'json' : request.POST.get('json', None),
            'tenant' : kwargs['user']['tenant']['id']
        }

        action = Action(
            url = MAIN_URL + '/endpoint/create/',
            data = data,
            headers=kwargs['headers']
        )

        action.post()

        messages.success(request, 'تم الانشاء بنجاح')
        return redirect('profile')