from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
from.models import*
from.models import Profile
def register(request):
    if request.method=="POST":
        fn=request.POST["fn"]
        ln=request.POST["ln"]
        un=request.POST["un"]
        em=request.POST["email"]
        pwdd=request.POST["pwdd"]
        cpw=request.POST["cpw"]
        cn=request.POST["cno"]
        adr=request.POST["add"]
        if(pwdd==cpw):
            usr=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=pwdd)
            usr.save()
            prousr=Profile(user=usr,cnum=cn,address=adr)
            prousr.save()
            return redirect("log")
        else:
            return redirect("about")
        
    return render(request,"registration.html")
        
def login(request):
    if request.method=='POST':
        un=request.POST['unm']
        pw=request.POST['pwd'] 
        log=auth.authenticate(username=un,password=pw)#for authentication
        if log!=None:
            auth.login(request,log)   
            messages.success(request,'congratulations!you are in.')
            return redirect('index')
            
        else:
            messages.warning(request,'wrong password or username')
            return redirect('reg')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("index")

def profile(request):
    display={}
    pro=Profile.objects.filter(user__id=request.user.id)
    if len(pro)>0:
        prof=Profile.objects.get(user__id=request.user.id)
        display["dis"]=prof
    return render(request,"profile.html",display)

def uppro(request):
    display={}
    prof=Profile.objects.filter(user__id=request.user.id)
    if len(prof)>0:
        dis=Profile.objects.get(user__id=request.user.id)
        display["data"]=dis
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST['email']
            ph_pro=request.POST['cn']
            state=request.POST['add']
            

            up_user=User.objects.get(id=request.user.id)
            up_user.first_name=fname
            up_user.last_name=lname
            up_user.email=email
            up_user.save()
            dis.cnum=ph_pro
            dis.address=state
            
            dis.save()
            if "img" in request.FILES:
                imgs=request.FILES["img"]
                dis.pimg=imgs
                dis.save()
                messages.info(request,"Image uploaded successfully")
                return redirect("upr")
            messages.info(request,"profile uploaded successfully")
            return redirect("pro")
    return render(request,"uprofile.html",display)