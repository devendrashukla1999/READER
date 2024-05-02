from contextlib import redirect_stderr
from http.client import REQUEST_ENTITY_TOO_LARGE
from operator import itemgetter
from pickle import BINPERSID, FALSE
from django.shortcuts import render,get_object_or_404,reverse,redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.contrib import messages
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from. models import *
from Register.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def checkout(request):
    return render(request,"checkoutt.html")
def Contact(request):
    if request.method=="POST":
        sub=request.POST["sub"]
        msg=request.POST["msg"]
        con_num=request.POST["con_num"]
        usr=get_object_or_404(User,id=request.user.id)
        cn=contact(user=usr,contnum=con_num,subject=sub,message=msg)
        cn.save()
    return render(request,"contact.html")
def login(request):
    return render(request,"login.html")
def index3929(request):
    books=Books.objects.all()
    return render(request,"shop.html",{'bk':books})
def sgpro(request,bid):
    dic={}
    prs=Books.objects.get(id=bid)
    dic["prs"]=prs
    return render(request,"single_product.html",dic)
def payment(request):
    return render(request,"payment.html")
def shop(request):
    return render(request,"shop.html")
def single_product(request):
    return render(request,"single_product.html")
def profile(request):
    return render(request,"profile.html")

def registration(request):
    return render(request,"registration.html")
def footer(request):
    return render(request,"footer.html")
def footer1(request):
    return render(request,"footer1.html")
def cartn(request):
    pass
def Cart(request):
    dic={}
    item=cart.objects.filter(usr_id=request.user.id,status=False)
    dic['item']=item
    if request.user.is_authenticated:
        if request.method=='POST':
            cried=request.POST['sid']
            quan=request.POST['qty']
            is_exist=cart.objects.filter(cour_id=cried,usr_id=request.user.id,status=False)
            if len(is_exist)>0:
             dic["msg"]="item already in cart"
            else:
                cor=get_object_or_404(Books,id=cried)
                usr=get_object_or_404(User,id=request.user.id)
                crt=cart(cour=cor,usr=usr,quantity=quan)
                crt.save()
                dic["msg"]="{}Added in ur Cart"
        else:
            dic["status"]="please login first"
    return render(request,"cart.html",dic)

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)

def get_cart_data(request):
    items= cart.objects.filter(user__id=request.user.id, status=False)
    sale,quantity =0,0
    for i in items:
        sale += float(i.prod.price)*i.quantity

        quantity+= float(i.quantity)

    res = {
        "offer":sale,"quan":quantity,
    }
    return JsonResponse(res)


def process_payment(request):
    items = cart.objects.filter(usr_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.cour.Books_name)+"\n"
        p_ids += str(j.cour.id)+","
        amt += float(j.cour.price)
        inv +=  str(j.id)
        cart_ids += str(j.id)+","

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt/77),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()

        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")

def Feedback(request):
    if request.method=="POST":
        msg=request.POST['msg']
        rat=request.POST['rat']
        pro_id=request.POST['bid']
        prfd=Profile.objects.get(user__id=request.user.id)
        pro_name=get_object_or_404(Books,id=pro_id)
        usr=get_object_or_404(User,id=request.user.id)
        feeds=feedback(user=usr,prof=prfd,ratpro=pro_name,message=msg,rating=rat)
        feeds.save()
        return redirect(index)
    return render(request,"feedback.html")


def search(request):
    dic={}
    if request.method =="POST":
        sr=request.POST["ser"]
        prs=Books.objects.filter(Books_name__icontains=sr)
        dic["bk"]=prs
    return render(request,"shop.html",dic)
def addbook(request):
    dic={}
    cate=Category.objects.all()
    
    dic["ct"]=cate
    if request.method=="POST":
        book=request.POST['bk']
        cate=request.POST['ct']
        price=request.POST['pr']
        desc=request.POST['desc']
        
        
        cate=get_object_or_404(Category,id=cate)
        usr=get_object_or_404(User,id=request.user.id)
        bok=Books(usr=usr,Books_name=book,category=cate,price=price,Discription=desc)
        bok.save()
        if "img" in request.FILES:
            pic=request.FILES["img"]
            bok.image=pic
            bok.save()
        return redirect("index")
    
    
    return render(request,"addbk.html",dic)
    