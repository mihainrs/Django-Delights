from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import SignUpForm

# Create your views here.

class SignUpView(View):
    def get(self, request):
        form =SignUpForm()
        return render(request, 'delights/signup.html', {'form' : form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'delights/signup.html', {'form' : form})

def home(request):
    return render(request, "delights/home.html")

class IngredientsView(ListView):
    model = Ingredient
    template_name = "delights/ingredients.html"
    context_object_name = "ingredients"
    
class IngredientsDelete(DeleteView):
    model = Ingredient
    success_url = "/"
    template_url = "delights/confirm_delete.html"

class MenuView(ListView):
    model = MenuItem
    template_name = "delights/menu.html"
    context_object_name = "menu"
    
class PurchaseView(ListView):
    model = Purchase
    template_name = "delights/purchases.html"
    context_object_name = "purchases"
    
class ReportView(TemplateView):
    template_name = "delights/report.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculating total rev:
        # calculate the total revenue by 
        # summing up the price of all MenuItems associated with each Purchase.
        
        total_revenue = sum(purchase.menuitem.menprice for purchase in Purchase.objects.all())
    
        
        #taking every ingredient's price and adding them up to calc. total price
        ingredient_price = 0
        
        for ingredient in Ingredient.objects.all():
            ingredient_price += ingredient.price
            
        total_profit = total_revenue - ingredient_price    
        
        context["total_revenue"] = total_revenue
        context["total_profit"] = total_profit
        context["ingredient_price"] = ingredient_price
        
        
        #return context to use the variables in DTL
        return context
    
class addmenu(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'delights/add_item.html'
    success_url = reverse_lazy('menu')
    fields = ['menuitem', 'menprice']
    
class addingredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'delights/add_ingredient.html'
    success_url = reverse_lazy('ingredients')
    fields = ['name', 'quantity', 'price']
    
class addreciperequirement(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = 'delights/add_recipereq.html'
    success_url = reverse_lazy('menu')
    fields = ['quantity', 'ingredients', 'menuitem']
    
class addpurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = 'delights/add_purchases.html'
    success_url = reverse_lazy('purchases')
    fields = ['menuitem']