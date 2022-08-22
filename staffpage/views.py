from django.core.mail import send_mail
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Staff
from .forms import ContactForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):

    return render(request, 'staffpage/home.html')


def about(request):
    
    return render(request, 'staffpage/about.html',)

def staff(request):
    staff = Staff.objects.all()
    # p = Paginator(Staff.objects.all(), 2)
    # page = request.get('page')
    # staff = p.get_page(page)
    context = {
        'staff':staff
    }
    return render(request, 'staffpage/staff.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print("the form was valid")
            return redirect('contact')
    else:
        form = ContactForm()    
    return render(request, 'staffpage/contact.html', {'form':form})