from django.contrib import messages
from datetime import datetime

from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from mainapp.app_forms import EmployeeForm, LoginForm
from mainapp.models import Employee
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from mainapp.app_forms import EmployeeForm
from mainapp.models import Employee


# info, success, error, debug, warning
# Create your views here.

def home(request):
    return render(request, "home.html")



def member(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Employee was saved")
            return redirect("member")

    else:
        form = EmployeeForm()
    return render(request, "employees.html", {"form": form})


# Model View Template
@login_required()
# All employees
# One employee
@permission_required('main_app.view_employee', raise_exception=True)
def all_employees(request):
    employees = Employee.objects.all()  # SELECT * FROM employees
    # employees = Employee.objects.all().order_by("-salary")
    # employees = Employee.objects.filter(name__istartswith="La").order_by("dob")
    # employees = Employee.objects.filter(name__istartswith="La", salary__gt=45000).order_by("dob")
    # employees = Employee.objects.filter(Q(name__contains="la") | Q(salary__gt=70000))
    # employees = Employee.objects.filter(Q(name__contains="la") & Q(salary__gt=70000))
    # employees = Employee.objects.filter(Q(name__contains="la") & ~Q(salary__gt=70000)) # tilde
    # today = datetime.today()
    # day = today.day
    # month = today.month
    # employees = Employee.objects.filter(dob__day=day, dob__month=month)  # tilde
    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "all_employees.html", {"employees": data})


@login_required()
@permission_required('main_app.view_employee', raise_exception=True)
def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)  # SELECT * FROM employees WHERE id=1
    return render(request, "employee_details.html", {"employee": employee})


@login_required()
@permission_required('main_app.delete_employee', raise_exception=True)
# employees/delete/12000
def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    employee.delete()
    messages.warning(request, "This employee was deleted permanently")
    return redirect("all")


@login_required()
@permission_required('main_app.view_employee', raise_exception=True)
def search_employees(request):
    search_word = request.GET["search_word"]
    employees = Employee.objects.filter(
        Q(name__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # Elastic search
    return render(request, "all_employees.html", {"employees": data})


@login_required()
@permission_required('main_app.change_employee', raise_exception=True)
def employee_update(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)  # SELECT * FROM employees WHERE id=1
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully")
            return redirect('details', emp_id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "update.html", {"form": form})


def about(request):
    return render(request, "about.html")


def blog_details_no_sidebar(request):
    return render(request, "blog-details-no-sidebar.html")


def blog_no_sidebar(request):
    return render(request, "blog-no-sidebar.html")


# def contact(request):
#     # if request.method == 'POST':
#     #     message_name = request.POST('message_name')
#     #     email = request.POST.get('email')
#     #     phone = request.POST.get('phone')
#     #     subject = request.POST.get('subject')
#     #     message = request.POST.get('message')
#     #     gridCheck = request.POST.get('gridCheck')
#     #
#     #     data = {
#     #         "message_name": message_name,
#     #         'email': email,
#     #         'phone': phone,
#     #         'subject': subject,
#     #         'message': message,
#     #         "gridCheck": gridCheck,
#     #              }
#     # # send_mail(
#     # #     message_name,
#     # #     message,
#     # #     email,
#     # #     ['vkorir.143@gmail.com']
#     # #
#     # # )
#     #
#     #     message = '''
#     #         New message: {}
#     #
#     #         From: {}
#     #         Phone: {}
#     #         '''.format(data['message'], data['email'], data['phone'])
#     # send_mail(data['subject'], message, '', ['vkorir.vkk@gmail.com'])
#     # return HttpResponse('Thank you for submitting the form, we will get back to you shorty')
#
#
#     if request.method == 'POST':
#
#     return render(request, "contact.html")

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        email = request.POST['email']  # Fix: Use square brackets for dictionary access
        phone = request.POST['phone']  # Fix: Use square brackets for dictionary access
        subject = request.POST['msg_subject']
        message = request.POST['message']
        grid_check = request.POST.get('gridCheck', False)  # Use .get() to handle checkbox not being checked
        # Assuming you want to redirect to the same page after form submission
        send_mail(
            message_name,
            message,
            email,
            ['vkorir.143@gmail.com']
        )

        return render(request, "contact.html", {"message_name": message_name, "phone": phone})
    else:
        return render(request, "contact.html", {})


def donation(request):
    return render(request, "donation.html")


def error_404(request):
    return render(request, "404.html")


def event_details(request):
    return render(request, "event-details.html")


def faq(request):
    return render(request, "faq.html")


def event(request):
    return render(request, "event.html")


def posts_by_author(request):
    return render(request, "posts-by-author.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def project_details(request):
    return render(request, "project-details.html")


def project_two(request):
    return render(request, "project-two.html")


def recover_password(request):
    return render(request, "recover-password.html")


def register(request):
    return render(request, "register.html")


def team(request):
    return render(request, "team.html")


def team_details(request):
    return render(request, "team-details.html")


def terms_of_service(request):
    return render(request, "terms-of-service.html")


def login(request):
    return render(request, "login1.html")


#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#
#
# from Climate_Action.models import Post
#
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#
#
# class CommentList(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#
#
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.CategorySerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#

def posts_by_date(request):
    return render(request, "posts-by-date.html")


# # ******************************************************************
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
# from .models import SubscribedUsers
# from django.contrib.auth import get_user_model
#
# ...
# def subscribe(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', None)
#         email = request.POST.get('email', None)
#
#         if not name or not email:
#             messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
#             return redirect("/")
#
#         if get_user_model().objects.filter(email=email).first():
#             messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
#             return redirect(request.META.get("HTTP_REFERER", "/"))
#
#         subscribe_user = SubscribedUsers.objects.filter(email=email).first()
#         if subscribe_user:
#             messages.error(request, f"{email} email address is already subscriber.")
#             return redirect(request.META.get("HTTP_REFERER", "/"))
#
#         try:
#             validate_email(email)
#         except ValidationError as e:
#             messages.error(request, e.messages[0])
#             return redirect("/")
#
#         subscribe_model_instance = SubscribedUsers()
#         subscribe_model_instance.name = name
#         subscribe_model_instance.email = email
#         subscribe_model_instance.save()
#         messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
#         return redirect(request.META.get("HTTP_REFERER", "/"))
# # ******************************************************************


# from django.shortcuts import render

def handler404(request, *args, **kwargs):
    response = render(request, '4041.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **kwargs):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response


# ********************************************************************************
# MPESA CODE
import json
import logging

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mainapp import mpesa

logger = logging.getLogger(__name__)


def initiate_payment(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        logger.info(f"{phone} {amount}")

        data = {
            "BusinessShortCode": mpesa.get_business_shortcode(),
            "Password": mpesa.generate_password(),
            "Timestamp": mpesa.get_current_timestamp(),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": mpesa.get_business_shortcode(),
            "PhoneNumber": phone,
            "CallBackURL": mpesa.get_callback_url(),
            "AccountReference": "123456",
            "TransactionDesc": "payment For Merchandise"
        }
        headers = mpesa.generate_request_headers()

        resp = requests.post(mpesa.get_payment_url(), json=data, headers=headers)
        print(resp.json())
        logger.debug(resp.json())

        json_resp = resp.json()
        code = json_resp['ResponseCode']
        if code == '0':
            mid = json_resp['MerchantRequestID']


        else:
            logger.error(f"Error when initiating stk{code}")

    return render(request, "donation.html")


@csrf_exempt
def callback(request):
    result = json.loads(request.data)
    mid = result["Body"]["stkCallback"]["MerchantRequestID"]
    cid = result["Body"]["stkCallback"]["CheckoutRequestID"]
    code = result["Body"]["stkCallback"]["ResultCode"]

    logger.info(f"From callBack Result {mid} {cid} {code}")
    return HttpResponse({'message': "Successfully received"})


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                dj_login(request, user)
                return redirect('home')
        messages.error(request, "Wrong username or password")
        return render(request, "login.html", {"form": form})


# python manage.py createsuperuser
# python manage.py changepassword admin

@login_required
def signout(request):
    logout(request)
    return redirect('signin')
