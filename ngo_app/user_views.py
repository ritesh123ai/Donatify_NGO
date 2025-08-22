from django.shortcuts import render,redirect
from.models import User,Feedback,Donation
from django.contrib import messages

import qrcode
import base64
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only for testing, in production use proper CSRF token headers with fetch
def generate_qr(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if not amount:
            return JsonResponse({'error': 'Amount is required'}, status=400)

        # You can use your UPI format or just amount text
        qr_data = f"upi://pay?pa=9555243744@ybl&am={amount}&cu=INR"

        img = qrcode.make(qr_data)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return JsonResponse({'image': img_str})
def child_education(request):
    if  request.method=="GET":
        return render(request,'ngo_app/user/child.html')
def animal_shelter(request):
        if  request.method=="GET":
            return render(request,'ngo_app/user/animal.html')
def disaster_relief(request):
        return render(request,'ngo_app/user/disaster.html')
def women_employment(request):
    if  request.method=="GET":
        return render(request,'ngo_app/user/women.html')
def user_logout(request):
    request.session.flush()
    messages.success(request,'logged out')
    return redirect("user_login")


def user_home(request):
# fetching values = email  from session to identify the user
    if request.method=='GET':
        user_email=request.session["web_key"]
        user_Obj=User.objects.get(email=user_email)  #it will return a single object
        # sending data from view to html page
        #  create a dictionary and bind data with key
        # send that dictionary with render function
        user_dict={
            "user_key":user_Obj  
            }
        return render(request,"ngo_app/user/user_home.html",user_dict)

def user_login(request):
    if request.method=="GET":
        return render(request, "ngo_app/user/user_login.html")
    if request.method=="POST":
        user_email=request.POST["email"]
        user_pass=request.POST["password"]
        ##select * from user where email=useremail and password=userpass
        USer_list=User.objects.filter(email=user_email,password=user_pass)
        if len(USer_list)>0:
            request.session["web_key"]=user_email
            return redirect("user_home")
        else:
            messages.error(request,"INVALID Credential")
            return redirect("user_login")

def user_feedback(request):
    if request.method=="GET":
        return render(request,'ngo_app/user/user_feedback.html')
    if request.method=="POST":
        user_name=request.POST["name"]
        user_email=request.session["web_key"]
        user_rating=request.POST["rating"]
        user_remark=request.POST["remark"]
        user_obj=Feedback(name=user_name,email=user_email,rating=user_rating,remark=user_remark)
        user_obj.save()
        messages.success(request,"THank uh for ur time ⭐⭐")
        return redirect("user_feedback")
def user_registration(request):
    if request.method=="GET":
        return render(request,'ngo_app/user/user_registration.html')
    if request.method=="POST":
        user_email= request.POST["email"] #control name input
        user_password=request.POST["password"]
        user_name=request.POST["name"]
        user_phone=request.POST["phone"]
        user_pic=request.FILES["profile_pic"]
        ##or mapping framework
        ##CREATE object of USER Model
        ##set values isme hm log model.py pr sequence wise krenge 
        ##saves object -> automatically stores values in table
        user_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,profile_pic=user_pic)
        user_obj.save()
        messages.success(request,"THank uh for ur Registration ⭐⭐")
        return redirect("user_login")
    
def donation(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/Donation.html')
    if request.method=="POST":
       email = request.session["web_key"]
       amount = request.POST["amount"]
       aadhaar = request.FILES["aadhaar"]
       transaction_id = request.POST["transaction_id"]
       user=User.objects.get(email=email)
       donation = Donation(user=user,amount=amount,aadhaar=aadhaar,transaction_id=transaction_id)
       donation.save()
       messages.success(request,"Thank you for Donation")
       return redirect("donation")
def payment_history(request):
    if  request.method=="GET":
     u_email = request.session["web_key"]

     user_obj=User.objects.get(email=u_email)
     donation_list=Donation.objects.filter(user=user_obj)
     donation_dict={
         
         "donation_key":donation_list
     }


     return render(request,'ngo_app/user/payment_history.html',donation_dict)

def user_edit_profile(request):
    if request.method=="GET":
        user_email=request.session["web_key"]
        user_Obj=User.objects.get(email=user_email)
        user_dict={
        "user_key":user_Obj  
            }
    

        return render(request,"ngo_app/user/user_edit_profile.html",user_dict)
    if request.method=="POST":
        user_name=request.POST["name"]
        user_phone=request.POST["phone"]
        user_pic=request.FILES.get("pic")
        user_email=request.session["web_key"]
        user_Obj=User.objects.get(email=user_email)
        if user_pic is not None:
            user_Obj.profile_pic=user_pic
        user_Obj.name=user_name
        user_Obj.phone=user_phone
        user_Obj.save()
        messages.success(request,"Profile Updated")   
        return redirect("user_home")
        