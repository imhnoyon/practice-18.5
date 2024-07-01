from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def Signup(request):
     if not request.user.is_authenticated:
        if request.method=='POST':
                data=forms.RegisterForm(request.POST)
                if data.is_valid():
                    messages.success(request,'Account created successfully')
                    data.save()
                    print(data.cleaned_data)
        else:
            data=forms.RegisterForm()      
        return render(request,'signup.html',{'form':data,'type':'Signup'})
     else:
         return redirect('login')



def Login(request):
     if not request.user.is_authenticated:
        if request.method=='POST':
            data=AuthenticationForm(request=request,data=request.POST)
            if data.is_valid():
                user_name=data.cleaned_data['username']
                user_Pass=data.cleaned_data['password']
                user=authenticate(username=user_name,password=user_Pass)
                if user is not None:
                        messages.success(request,'Loggin successfully')
                        login(request,user)
                        return redirect('profile')
            else:
                return redirect('login')
        else:
            data=AuthenticationForm()
        return render(request,'signup.html',{'form':data,'type':'Login'})
     
     else:
         return redirect('login')
          
@login_required(login_url="/login/")
def Profile(request):
     if request.user.is_authenticated:
        return render(request,'profile.html')
     else:
         return redirect('login')


def Logout(request):
     messages.success(request,'Logout successfully')
     logout(request)
     return redirect('user_login')
          

def passWord_changes(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                user=form.save()
                update_session_auth_hash(request,user)
                return redirect('profile')        
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passChanges.html',{'form':form,'type':'Password changes1'})
    else:
        return redirect('login')
    

def passWord_changes2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                user=form.save()
                update_session_auth_hash(request,user)
                return redirect('profile')        
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passChanges.html',{'form':form,'type':'Password changes2'})
    else:
        return redirect('login')