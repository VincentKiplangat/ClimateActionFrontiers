"""
URL configuration for ClimateActionFrontier_EmobilisProjectShowcasing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from mainapp import views
from ClimateActionFrontier_EmobilisProjectShowcasing import settings

urlpatterns = [
                  path('', views.home, name="home"),
                  path('member', views.member, name="member"),
                  path('employees', views.all_employees, name="all"),
                  path('search', views.search_employees, name="search"),
                  path('employees/<int:emp_id>', views.employee_details, name="details"),
                  path('employees/delete/<int:emp_id>', views.employee_delete, name="delete"),
                  path('employees/update/<int:emp_id>', views.employee_update, name="update"),
# # **********************************************************************
# path('subscribe', views.subscribe, name='subscribe'),
# # *********************************************************************************
                  path('about', views.about, name="about"),
                  path('blog_details_no_sidebar', views.blog_details_no_sidebar,
                       name="blog-details-no-sidebar"),
                  path('blog_no_sidebar', views.blog_no_sidebar, name="blog-no-sidebar"),
                  path('contact/', views.contact, name="contact"),
                  path('donation', views.initiate_payment, name="donation"),
                  path('error_404', views.error_404, name="error-404"),
                  path('event_details', views.event_details, name="event-details"),
                  path('faq', views.faq, name="faq"),
                  path('event', views.event, name="event"),

                  path('signin', views.signin, name="signin"),
                  path('signout', views.signout, name="signout"),


                  path('login', views.login, name="login"),
                  path('post_by_author', views.posts_by_author, name="posts-by-author"),
                  path('post_by_date', views.posts_by_date, name="posts-by-date"),

                  path('privacy_policy', views.privacy_policy, name="privacy-policy"),
                  path('project_details', views.project_details, name="project-details"),
                  path('project_two', views.project_two, name="project-two"),
                  path('recover_password', views.recover_password, name="recover-password"),
                  path('register', views.register, name="register"),
                  path('team', views.team, name="team"),
                  path('team_details', views.team_details, name="team-details"),
                  path('terms_of_service', views.terms_of_service, name="terms-of-service"),
                  path('admin/', admin.site.urls),

                  # path('users/', views.UserList.as_view()),
                  # path('users/<int:pk>/', views.UserDetail.as_view()),
                  # path('posts/', views.PostList.as_view()),
                  # path('posts/<int:pk>/', views.PostDetail.as_view()),
                  # path('api-auth/', include('rest_framework.urls')),
                  #
                  # path('comments/', views.CommentList.as_view()),
                  # path('comments/<int:pk>/', views.CommentDetail.as_view()),
                  # path('categories/', views.CategoryList.as_view()),
                  # path('categories/<int:pk>/', views.CategoryDetail.as_view()),

                  # path('', views.initiate_payment, name='initiate'),
                  path('callback', views.callback, name='callback'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)