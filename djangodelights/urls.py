"""
URL configuration for djangodelights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from delights import views
from delights.views import IngredientsView, IngredientsDelete, MenuView, PurchaseView, ReportView, addmenu, addingredient, addreciperequirement, addpurchase, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ingredients/', IngredientsView.as_view(), name='ingredients'),
    path('<pk>/delete/', IngredientsDelete.as_view()),
    path('menu/', MenuView.as_view(), name='menu'),
    path('purchases/', PurchaseView.as_view(), name='purchases'),
    path('report/', ReportView.as_view(), name='report'),
    path('add_item/', addmenu.as_view(), name='add_item'),
    path('add_ingredient/', addingredient.as_view(), name='add_ingredient'),
    path('add_recipereq/', addreciperequirement.as_view(), name='add_recipereq'),
    path('add_purchase/', addpurchase.as_view(), name='add_purchase'),
    path('login/', auth_views.LoginView.as_view(template_name='delights/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='delights/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
