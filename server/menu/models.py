from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class IngredientsModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, on_delete=models.CASCADE,
                              blank=True, default=None, related_name='category')
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True)
    ingredients = models.ManyToManyField(
        IngredientsModel, blank=True, default=None, related_name='ingredients')
    image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    special_status = models.CharField(max_length=200, null=True, blank=True,default='No')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class SpecialsModel(models.Model):
    item = models.ForeignKey(MenuItems, null=True, on_delete=models.CASCADE,
                              blank=True, default=None, related_name='item')
    special_price = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.item.name
    

# Order Models start 
class RemovedIngredientsModel(models.Model):
    ingredients = models.ForeignKey(IngredientsModel, null=True, on_delete=models.CASCADE,
                              blank=True, default=None, related_name='removed_ingredient')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ingredients.name
    

class OrderModel(models.Model):
    currentUser = models.CharField(max_length=200, null=True, blank=True)
    table = models.CharField(max_length=200, null=True, blank=True)
    orderNumber = models.CharField(max_length=200, null=True, blank=True)
    item = models.ForeignKey(MenuItems, null=True, on_delete=models.CASCADE,
                              blank=True, default=None, related_name='item_order')
    speacial = models.ForeignKey(SpecialsModel, null=True, on_delete=models.CASCADE,
                              blank=True, default=None, related_name='special_order')
    price = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True)
    removed_ingredient = models.ManyToManyField(
        RemovedIngredientsModel, blank=True, default=None, related_name='removed_ingredients')
    status = models.CharField(max_length=200, null=True, blank=True,default='Pending')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.orderNumber
    
    
class TableOrderModel(models.Model):
    table = models.CharField(max_length=200, null=True, blank=True)
    orders = models.ManyToManyField(
        OrderModel, blank=True, default=None, related_name='orders')
    total_price = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True,default='Pending')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.table