from django.views import View
from django.shortcuts import redirect, render
from globals.decorators import login_required, tenant_parser_or_404
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.http import JsonResponse, Http404

class endpoint_view (View) : 

    @tenant_parser_or_404
    def get(self, request, endpoint_name, **kwargs) :
        print(endpoint_name)
        tenant = kwargs['tenant']
        
        action = Action(
            url = MAIN_URL + f'/endpoint/get/user/{tenant}/{endpoint_name}',
        )

        action.get()

        if not action.is_valid() :
            raise Http404(request)

        response = action.json_data()
        print(response)

        return JsonResponse(response,safe=False)