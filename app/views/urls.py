from django.urls import path
from .auth import login, register, logout
from .home import profile, endpoint

urlpatterns = [
    path('login/', login.login_view.as_view(),name='login'),
    path('register/', register.register_view.as_view(),name='register'),
    path('logout/', logout.logout_view.as_view(),name='logout'),
    path('', profile.profile_view.as_view(), name='profile'),
    path('endpoint/<str:endpoint_name>/', endpoint.endpoint_view.as_view(), name='endpoint'),
]