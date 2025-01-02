from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from .models import *
from ass_helths import settings
from django.core.mail import send_mail
# Create your views here.
def sign_in(request):
    if request.method=='POST':
        us=request.POST['email']
        pas=request.POST['password']
        rol=request.POST['role']
        print("role=",rol)
        if rol == 'doctor':
            user=doctor_tbl.objects.filter(email=us,password=pas)
            if user :
                request.session['cuser']=us
                request.session['rol']=rol
                return redirect('/')
            else:
                print("error")
        elif rol == 'patient':
            user=patient.objects.filter(email=us,password=pas)
            if user :
                request.session['cuser']=us
                request.session['rol']=rol
                return redirect('/')
            else:
                print("error")
        else:
            return redirect('sign_up')

    return render(request,'sign_in.html')

def signup(request):
    if request.method == 'POST':
        role=request.POST['role']
        if role == "doctor":
            nwreq = doctorform(request.POST, request.FILES)
            if nwreq.is_valid():
                nwreq.save()
                print("Doctor data successfully saved.")
                sub = "Welcome to Healthify - Patient Portal"
                msg = (
                    f"Hello,\n\n"
                    "Thank you for registering with Healthify! We are here to help you with your health journey.\n"
                    "You can now book appointments and view your health records through your account.\n\n"
                    "Thanks & Regards,\n"
                    "Healthify Team\n"
                    "Contact: 9106903090\n"
                    "Email: kevalkotadiya94@gmail.com"
                    )
                from_ID=settings.EMAIL_HOST_USER
                to_ID=request.POST['email']
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=[to_ID])

                return redirect('sign_in')
            else:
                print(nwreq.errors) 
        elif role == "patient":
            pnew = patientsform(request.POST)  
            if pnew.is_valid():
                pnew.save()
                print("Patient data successfully saved")
                sub = "Welcome to Healthify - Patient Portal"
                msg = (
                    f"Hello,\n\n"
                    "Thank you for registering with Healthify! We are here to help you with your health journey.\n"
                    "You can now book appointments and view your health records through your account.\n\n"
                    "Thanks & Regards,\n"
                    "Healthify Team\n"
                    "Contact: 9106903090\n"
                    "Email: kevalkotadiya94@gmail.com"
                )
                from_ID=settings.EMAIL_HOST_USER
                to_ID=request.POST['email']
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=[to_ID])

                return redirect('sign_in')
            else:
                print(pnew.errors) 

    return render(request, 'signup.html')


def home(request):
    user=request.session.get('cuser')
    return render(request,'home.html',{'user':user})

def about(request):
    user=request.session.get('cuser')
    return render(request,'about.html',{'user':user})

def  department(request):
    user=request.session.get('cuser')
    return render(request,'department.html',{'user':user})

def  doctorview(request):
    user = request.session.get('cuser')
    rol=request.session.get('rol')
    ddata = doctor_tbl.objects.all()
    pdata = appointmentabl.objects.all()
    
    
    return render(request, 'doctorview.html', {'ddata': ddata, 'pdata': pdata,'rol':rol,'user':user},)


    

def  otp(request):
    return render(request,'otp.html')

def  viewpatients(request):
    user=request.session.get('cuser')
    pdata=appointmentabl.objects.all()
    return render(request,'viewpatients.html',{'pdata':pdata,'user':user})

def  forgetpassword(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        user = (
            doctor_tbl.objects.filter(email=email).first() or 
            patient.objects.filter(email=email).first()
        )
        
        if user:
            request.session['email'] = email
            #send mail
            sub = "Healthify - Reset Your Password"
            msg = (
                f"Dear User,\n\n"
                "We received a request to reset your password. Please use the link below to set a new password:\n\n"
                "Reset Password Link: https://yourwebsite.com/reset-password?token=your_unique_token\n\n"
                "If you did not request this, please ignore this email or contact our support team for assistance.\n\n"
                "Thanks & Regards,\n"
                "Healthify Team\n"
                "Contact: 9106903090\n"
                "Email: kevalkotadiya94@gmail.com"
            )

            from_ID = settings.EMAIL_HOST_USER
            to_ID = request.POST['email']
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=[to_ID])

            print('done')
            return redirect('reset_password',)
        else:
            print('error')
            


    return render(request,'forgetpassword.html')

def  contact(request):
    user=request.session.get('cuser')
    if request.method == 'POST':
        new_req =contactfrom(request.POST)
        if new_req.is_valid():
            new_req.save()
            print('your contact from is succ...')
            return redirect('/')
        else:
            print(new_req.errors)
    return render(request,'contact.html',{'user':user})


    

def  appointment(request):
    user=request.session.get('cuser')
    
    if request.method == 'POST':
        new_req =appintmentfrom(request.POST)
        if new_req.is_valid():
            new_req.save()
            print('your contact from is succ...')
            return redirect('/')
        else:
            print(new_req.errors)
    return render(request,'appointment.html',{'user':user})


def approved(request,id):
    user=request.session.get('cuser')
    pdata = appointmentabl.objects.get(id=id)

    if request.method=='POST':
        upreq=apform(request.POST,instance=pdata)
        if upreq.is_valid():
            upreq.save()
            print("Patient appontment successfully saved")

            #send mail

            sub = "Welcome to Healthify - Patient Portal"
            msg = (
                f"Hello,\n\n"
                "Your appointment has been successfully approved!\n"
                "We are excited to assist you on your health journey. Please ensure you arrive on time for your scheduled appointment.\n\n"
                "If you have any questions or need assistance, feel free to contact us.\n\n"
                "Thanks & Regards,\n"
                "Healthify Team\n"
                "Contact: 9106903090\n"
                "Email: kevalkotadiya94@gmail.com"
            )

            from_ID=settings.EMAIL_HOST_USER
            to_ID=request.POST.get('email')
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=[to_ID])

            return redirect('dv')
        else:
            print("not save")
    return render(request,'approve.html',{'data':pdata},)

def userlogout(request):
    logout(request)
    return redirect('sign_in')

def master(request):
    user = request.session.get('cuser')
    return render(request, 'master.html', {'cuser': user})


def profile(request):
    rol=request.session.get('rol')
    user=request.session.get('cuser')
    if rol == 'doctor':
        f_data=doctor_tbl.objects.get(email=user)
    else:
        f_data=patient.objects.get(email=user)
    return render(request,'profile.html',{'user':user,'f_data':f_data,'rol':rol})

def updateprofile(request):
    user=request.session.get('cuser')
    rol=request.session.get('rol')
    if rol == 'doctor':
        cu=doctor_tbl.objects.get(email=user)
    else:
        cu=patient.objects.get(email=user)

    if request.method=='POST':
        update_re=doctorform,patient(request.POST,instance=cu)
        if update_re.is_valid():
            update_re.save()
            print("Your profile has been updated!")
            
            return redirect('/')
        else:
            print(update_re.errors)

    return render(request,'updateprofile.html',{'user':user,'cu':cu,'rol':rol})

def delete_acc(request,id):
    rol=request.session.get('rol')
    if rol == 'doctor':
        T_id = doctor_tbl.objects.get(id=id)
        doctor_tbl.delete(T_id)
    else :
        T_id = patient.objects.get(id=id)
        patient.delete(T_id)
    print("Delete id sucessfully")
    return redirect("sign_in")

def reset_password(request):
    em = request.session.get('email')
    
    if request.method == 'POST':
        newpass = pass_form(request.POST)
        email = request.session.get('email')
        user = (
            doctor_tbl.objects.filter(email=email).first() or 
            patient.objects.filter(email=email).first()
        )
        

        if newpass.is_valid():
            newpass = pass_form(request.POST,instance=user)
            newpass.save()
            print('Password updated successfully')
            request.session.flush()
            return redirect('sign_in')
        else:
            print(newpass.errors)
    
    
    return render(request,'reset_password.html')
            

def delete_ap(request, id):
    ap = appointmentabl.objects.get( id=id)
    ap.delete()
    print(f"Deleted appointment with id: {id} successfully")
    return redirect("/")
        
       
