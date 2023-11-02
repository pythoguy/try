from django.urls import path
from app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path("loginn",views.loginn,name="loginn"),
    path("savedata",views.savedata),
    path("logoutuser",views.logoutuser),
    path("contactus",views.contactus, name="ContactUs"),
    path("showdata",views.showdata, name="showdata"),
    path("loggedin",views.loggedin),
    path("saveinfo",views.saveinfo),
    path("paid",views.products),

    path("updatedata/<int:x>", views.updatedata, name = "updatedata"),

    path("updatenow/<int:x>", views.update, name = "updatenow"),

    path("delete/<int:x>", views.detethis),

    path("search", views.search),
    
]