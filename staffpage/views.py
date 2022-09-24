import email
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Staff
from .forms import ContactForm, UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'home.html')


def about(request):   
    return render(request, 'about.html',)

def staff(request):
    staff = Staff.objects.all()
    context = {
        'staff':staff
    }
    return render(request, 'staff.html', context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            new_name = "Sender's Name: "+ name
            new_email = "Sender's Email: "+ email
            new_content = "Message: "+ content
            

            body = {
                'name': new_name,           
                'email': new_email,
                'content':new_content,
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject,  message, ['site@nasmp.com'], ['admin@nasmp.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header foound')
            return redirect("success")
    return render(request, 'contact.html', {'form':form})



def success(request):
    
    return render(request, 'success.html',)


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect('home')
    else:
        form = UserForm()
        return render(request, 'login.html', {'form':form})


def signout(request):
    logout(request)
    return redirect('home')

    