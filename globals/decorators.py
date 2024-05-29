from django.http import Http404
from django.shortcuts import redirect
from .request_manager import Action
from frontend.settings import MAIN_URL

def login_required (function) : 

    def wrapper (self, request, **kwargs) : 

        user = request.COOKIES.get('user',None)

        if user is None :
            return redirect('login')
        
        action = Action(
            url = MAIN_URL + '/user/profile/',
            headers = {'Authorization':f"Bearer {user}"}
        )

        action.get()

        if not action.is_valid() : 
            return redirect('login')

        kwargs['headers'] = {'Authorization':f"Bearer {user}"}
        kwargs['user'] = action.json_data()
        
        func = function(self,request,**kwargs)
        return func
    
    return wrapper


def tenant_parser_or_404 (function) : 
    def wrapper (self, request, **kwargs) :
        host:str = request.get_host()
        split_host = host.split('.')
        has_tenant = (len(split_host) > 1)
        
        if not has_tenant:
            raise Http404(request)
        
        tenant_name = split_host[0]
        kwargs.setdefault('tenant', tenant_name)
        fn = function(self, request, **kwargs)
        return fn
    
    return wrapper
