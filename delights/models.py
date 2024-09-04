from django.db import models

# Create your models here.
class MenuItem(models.Model):
    #items, price set for each
    menuitem = models.CharField(max_length=100, verbose_name= 'Menu Item')
    menprice = models.FloatField(verbose_name= 'Menu Price')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['menuitem'], name='unique_menuitem')
        ]
        
    def __str__(self):
        return self.menuitem

class Ingredient(models.Model):
    #name, quantity, price per unit
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_ingredient_name')
        ]
    
    def __str__(self):
        return self.name
        
class RecipeRequirement(models.Model):
    #ingredients each menu item requires
    quantity = models.FloatField()
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ingredients', 'menuitem'], name='unique_recipe_requirement')
        ]
     
class Purchase(models.Model):
    #log of purchases made
    date = models.DateTimeField(auto_now_add=True)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name= 'Menu Item')
    
    def __str__(self):
        return f'{self.menuitem} ordered at {self.date}'
    
class Report(models.Model):
        money = models.FloatField(max_length=999999)