
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index"),
    path("abt",views.about, name="about"),
    path("cnt",views.Contact, name="contact"),
    path("chk",views.checkout, name="checkout"),
    path("log",views.login, name="login"),
    path("ind",views.index3929, name="index3929"),
    path("pay",views.payment, name="payment"),
    path("sgn/<int:bid>",views.sgpro, name="sgn"),
    path("atc",views.shop, name="shop"),
    path("single",views.single_product, name="single_product"),
    path("pro",views.profile, name="profile"),
    path("addbk",views.addbook, name="addbk"),
    path("regis",views.registration, name="registration"),
    path("footer",views.footer, name="footer"),
    path("footer1",views.footer1, name="footer1"),
    path("cart",views.Cart, name="cart"),
    path("change_quan",views.change_quan,name = "change_quan"),
    path("get_cart_data",views.get_cart_data,name = "get_cart_data"),
    path("process_payment",views.process_payment,name="process_payment"),
    path("payment_done",views.payment_done,name="payment_done"),
    path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
    path("feedback",views.Feedback, name="feedback"),
    path("search",views.search, name="ser"),
]