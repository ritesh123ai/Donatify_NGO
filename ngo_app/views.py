from django.shortcuts import render,redirect
from .models import Contact,Campaign,Feedback,User,Service
from django.contrib import messages
# Create your views here.
def view_campaign(request):
    camp_list=Campaign.objects.all()#select*from campaign
    context={
        "camp_key":camp_list
    }

    return render(request,'ngo_app/html/view_campaign.html',context)

def home(request):
    feedback=Feedback.objects.all()
    data=[]
    for f in feedback:
        data.append(
            {
                "rating":f.rating,
                "remark":f.remark,
                "name":f.name,
                "profile_pic":User.objects.filter(email=f.email)[0].profile_pic
            }
        )
    feedback_dict={
        "feedback_key":data
    }
    
    return render(request,'ngo_app/html/index.html',feedback_dict)
def contact(request):

    if request.method=="GET":
        return render(request,'ngo_app/html/contact_us.html')

    if request.method=="POST":
    #fetch value from all textfield
    #Create object of Contact model and save
        
    
        user_name=request.POST["name"]
        user_email=request.POST["email"]
        user_number=request.POST["phone"]
        user_phone=request.POST["phone"]
        user_comment=request.POST["comment"]
        user_obj=Contact(name=user_name,email=user_email,phone=user_phone,comment=user_comment)
        user_obj.save()
        messages.success(request,"THank uh for ur time ⭐⭐")
        return redirect("contact_us")


def about(request):
    return render(request,'ngo_app/html/about_us.html')


def Donation(request):
    return render(request,'ngo_app/user/Donation.html')


def Service(request):
    return render(request,'ngo_app/user/Service.html')

def child(request):
    return render(request,'ngo_app/user/child.html')


def womenempowerment(request):
    return render(request,'ngo_app/user/womenempowerment.html')

def education(request):
    return render(request,'ngo_app/user/education.html')

