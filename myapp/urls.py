from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('signup/',views.signup,name='sign_up'),
    path('about/',views.about),
    path('department/',views.department),
    path('doctorview/',views.doctorview,name="dv"),
    path('viewpatients/',views.viewpatients),
    path('otp/',views.otp),
    path('contact/',views.contact),
    path('appointment/',views.appointment),
    path('forgetpassword/',views.forgetpassword),
    path('approve/<int:id>',views.approved),
    path('master/',views.master),
    path('userlogout/',views.userlogout),
    path('profile/',views.profile),
    path('updateprofile/',views.updateprofile),
    path('delete_acc/<int:id>',views.delete_acc),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('delete_ap/<int:id>',views.delete_ap),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)