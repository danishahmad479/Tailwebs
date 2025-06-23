from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .models import *
import re
from django.core.paginator import Paginator

# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if len(password) < 7:
            messages.error(request, "Password must be at least 7 characters long.")
            return render(request, "register.html")

        if not re.search(r"\d", password):
            messages.error(request, "Password must contain at least one number.")
            return render(request, "register.html")

        if not re.search(r"[^\w\s]", password): 
            messages.error(request, "Password must contain at least one symbol.")
            return render(request, "register.html")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.Please enter new Email")
            return render(request, "register.html")

       
        username = email.split("@")[0]  
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful!")
        return redirect("login") 

    return render(request, "register.html")


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Email doesn't exist.Please register")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    return render(request, 'login.html')

@login_required
def index(request):
    records_list = StudentRecord.objects.all().order_by('-id')  
    paginator = Paginator(records_list, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})



def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

@login_required
def add_record(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name").strip()
            subject = request.POST.get("subject").strip()
            mark = int(request.POST.get("mark"))

            existing_record = StudentRecord.objects.filter(name__iexact=name, subject__iexact=subject).first()
            if existing_record:
                existing_record.mark += mark
                existing_record.save()
                messages.success(request, "Record updated with new marks.")

            else:
                # Create new record
                StudentRecord.objects.create(name=name, subject=subject, mark=mark)
                messages.success(request, "Record added successfully.")
                return redirect('index')
        except Exception as e:
            messages.error(request, f"An error occurred while adding the record: {str(e)}")

    return redirect('index')
    



@login_required
def delete_record(request, record_id):
    try:
        record = StudentRecord.objects.get(id=record_id)
        record.delete()
        messages.success(request, "Record deleted successfully.")
    except StudentRecord.DoesNotExist:
        messages.error(request, "Record not found.")
    
    return redirect('index') 



@login_required
def edit_record(request, record_id):
    try:
        record = StudentRecord.objects.get(id=record_id)
    except StudentRecord.DoesNotExist:
        messages.error(request, "Record not found.")
        return redirect('index')

    if request.method == 'POST':
        name = request.POST.get('name').strip()
        subject = request.POST.get('subject').strip()
        mark = request.POST.get('mark')

        # Check for duplicates excluding the current record
        if StudentRecord.objects.filter(name__iexact=name, subject__iexact=subject).exclude(id=record_id).exists():
            messages.error(request, "This name and subject already exist.")
            return redirect('index')

        record.name = name
        record.subject = subject
        record.mark = mark
        record.save()

        messages.success(request, "Record updated successfully.")
        return redirect('index')

    return render(request, 'edit_record.html', {'record': record})
