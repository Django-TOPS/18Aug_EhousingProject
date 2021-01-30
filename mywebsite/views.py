from django.shortcuts import render,HttpResponse,redirect
# for signup model
from .models import signup
from .forms import signupForm

#for Complain model
from .models import complain
from .forms import complainForm

#for contact form
from .models import contact
from .forms import contactForm

# for send mail 
from django.core.mail import send_mail
from django.conf import settings

#for sending OTP Massage
import os  
from twilio.rest import Client # IMPORT Client for used massage
import random # import random is used for otp
#for logout 
from django.contrib.auth import logout
# for update profile


# Create your views here.
#if signup in single page
'''def index(request):
    if request.method=='POST':
        myfrm=signupForm(request.POST)
        if myfrm.is_valid():
            myfrm.save()
            print("signup successfully!")
            return redirect('/')
        else:
            print("Error,Please Try again")
    else:
        myfrm=signupForm()           

    return render(request,'index.html',{'myfrm':myfrm})'''
#signup and login same page
def index(request):
    if request.method=='POST':
        myfrm = signupForm(request.POST)
        if request.POST.get('signup')=='signup':
            if myfrm.is_valid():
                myfrm.save()

                """
                #sending confirm mail when signup
                subject='signup success! welcome'
                msg='Hello user,Your Account has been created successfully with us! Enjoy our Service.'
                mail_from=settings.EMAIL_HOST_USER
                mail_to=['jigneshpatel.ec.er@gmail.com','ashapatel3893@gmail.com']
                send_mail(subject,msg,mail_from,mail_to)
                print('Mail Send Successfully')
                """

                """
                #(SMS)SEND 
                otp=random.randint(1111,9999)
                client = Client('ACd8e6df33dc5a3452449aca0d631e83d6', '67ab20a19e679ce8042c505fe664675b')
                messege = client.messages.create( 
                     body=f"Hello User,Your Account Successfully Created! and your OTP is {otp}",
                     from_="+18086701446",
                     to='+919898536464')
                
                print(message.sid)
                """
                print("signup successfully!")
                return redirect('profile')
            else:
                print("error")
        elif request.POST.get('login')=='login':
            print("login calling")
            email=request.POST['email']
            password=request.POST['password']

            

            user=signup.objects.filter(email=email,password=password)
            if user:
                #sending confirm mail when login
                """
                subject='You have successfuuly login!'
                msg='You have successfuuly login!'
                mail_from=settings.EMAIL_HOST_USER
                mail_to=['jigneshpatel.ec.er@gmail.com','ashapatel3893@gmail.com']
                send_mail(subject,msg,mail_from,mail_to)
                print('Mail Send Successfully')
                """
              
               #for update profile
                uid=signup.objects.get(email=email) 
               #login
                request.session['userid']=email

                #for update
                request.session['uid']=uid.id
                print("login successfully")
                print(uid.id)
                return redirect('profile')
            else:
                print("Login Field try again")              
    else:
        myfrm = signupForm()           
    return render(request,'index.html',{'myfrm':myfrm})


def home(request):
    return render(request,'home.html') 

def about(request):
    return render(request,'about.html')  

def Configuration(request):
    return render(request,'Configuration.html')    

def facilites(request):
    return render(request,'facilites.html')      

def profile(request):
    user=request.session.get('userid')
    #for complain model call
    if request.method=='POST':
        #add bcz one page two method used
        if request.POST.get('complain')=='complain':
            cmfrm=complainForm(request.POST)
            if cmfrm.is_valid():
                cmfrm.save()
                print("complain done successfully!")
                return redirect('index')
            else:
                print("Error,Please Try again")
        #for Login navbar from direct profile    
        elif request.POST.get('login')=='login':
            print("login calling")
            email=request.POST['email']
            password=request.POST['password']
            uid=signup.objects.get(email=email)
            user=signup.objects.filter(email=email,password=password)

            if user:
                request.session['userid']=email
                request.session['uid']=uid.id
                print("login successfully")
                print("userID:",uid.id)
                return redirect('profile')
            else:
                print('login failed')        
    else:
        cmfrm=complainForm() 

    return render(request,'profile.html',{'user':user,'cmfrm':cmfrm})   

def contact(request):
    if request.method=='POST':
        cnt=contactForm(request.POST)
        if cnt.is_valid():
            cnt.save()
            print("contacted form submitted")
            return redirect('profile')
        else:
            print("error try again")
    else:
        cnt=contactForm()

    return render(request,'contact.html',{'cnt':cnt}) 

def updateprofile(request):
# for simple updatefrofile
    user=request.session.get('userid') 
# for update form model
    stid=request.session.get('uid')
    if request.method=='POST':
        myfrm=signupForm(request.POST)
        id=signup.objects.get(id=stid)
        if myfrm.is_valid():
            myfrm=signupForm(request.POST, instance=id)
            myfrm.save()
            print("Your Profile has been updated Successfully")
            return redirect('profile')
        else:
            print("errors")
    else:
        myfrm=signupForm()

   # return render(request,'updateprofile.html',{'user':user})   only for simple
    return render(request,'updateprofile.html',{'myfrm':myfrm,'user':user,'stdata':signup.objects.get(id=stid)})



    

def user_logout(request):
    logout(request)
    return redirect('/')

def notice(request):
    return render(request,'notice.html')

