
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.show_formdata),
    path('info/',views.student_view),
    path('signup/',views.signup_views),
    path('login/',views.user_login),
    path('profile/',views.profile_view),
    path('logout/',views.logout_view,name='logout')
]
