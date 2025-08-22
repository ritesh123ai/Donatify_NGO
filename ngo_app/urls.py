from django.urls import path,include
from . import views,user_views

urlpatterns = [
    path("",views.home,name="home"),
    path("contact/",views.contact,name="contact_us"),
    path("about/",views.about,name="about_us"),
    path("user_feedback/",user_views.user_feedback,name="user_feedback"),
    path("user-login/",user_views.user_login,name="user_login"),
    path("user_registration/",user_views.user_registration,name="user_registration"),
    path("user_home/",user_views.user_home,name='user_home'),
    path("user_logout/",user_views.user_logout,name='user_logout'),
    path("view_campaign/",views.view_campaign,name='view_campaign'),
    path("donation/",user_views.donation,name='donation'),
    path("women/",user_views.women_employment,name="women_empoyment"),
    path("child/",user_views.child_education,name="child_education"),
    path("animal/",user_views.animal_shelter,name="animal_shelter"),
    path("disaster/",user_views.disaster_relief,name="disaster"),
    path('generate_qr/', user_views.generate_qr, name='generate_qr'),
    path('payment_history/', user_views.payment_history, name='payment_history'),
    path("user_edit_profile/",user_views.user_edit_profile,name="user_edit_profile")


]