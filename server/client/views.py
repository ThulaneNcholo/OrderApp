from django.shortcuts import render
import random
from django.db.models import Q

# other models 
from menu.models import *

# Create your views here.
def IndexView(request):
    category = Categories.objects.all().order_by('date_created')
    items = MenuItems.objects.filter(special_status = 'No').order_by('date_created')
    specials = SpecialsModel.objects.all().order_by('date_created')
    quantity_input = 0
     # Retrieve the variable from the session
    loggedUser = request.session.get('userID')
    orderCount = OrderModel.objects.filter(currentUser = loggedUser).count()

    context = {
        "category" : category,
        "items" : items,
        "specials" : specials,
        "quantity_input" : quantity_input,
        "orderCount" : orderCount
    }

    return render(request,'client/index.html',context)

def IncreaseQuantityView(request,id):

    if request.method == 'POST':
        item = MenuItems.objects.get(id = id)
        ref_number = random.randrange(100, 10000)
        ref = 'ORD' + str(ref_number)

        createOrder = OrderModel()
        createOrder.currentUser = request.POST.get('orderUser')
        createOrder.table = request.POST.get('orderTable')
        createOrder.orderNumber = ref
        createOrder.item = item 
        createOrder.price = item.price
        createOrder.save()

        current_user = createOrder.currentUser
        # Retrieve the variable from the session
        loggedUser = request.session.get('userID')

        if current_user != loggedUser:
            updateCartItems = OrderModel.objects.filter(currentUser = loggedUser)
            updateCartItems.delete()
            # Save a variable to the session
            request.session['userID'] = current_user
        else:
            # Save a variable to the session
            request.session['userID'] = current_user

        quantity_input = OrderModel.objects.filter(item = item).count()

        context = {
            "quantity_input" : quantity_input
        }
        
        
        
    return render(request,'order/quantity.html',context)


def DecreaseQuantityView(request,id):
    if request.method == 'POST':
        item = MenuItems.objects.get(id = id)
        # Retrieve the variable from the session
        current_user = request.session.get('userID')

        if OrderModel.objects.filter(Q(item=item) & Q(currentUser=current_user)).exists():
            cartItem = OrderModel.objects.filter(Q(item=item) & Q(currentUser=current_user)).first()
            cartItem.delete()

        quantity_input = OrderModel.objects.filter(item = item).count()

        context = {
            "quantity_input" : quantity_input
        }

    return render(request,'order/quantity.html',context)

def UpdateCartView(request,id):
    item = MenuItems.objects.get(id = id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

        if OrderModel.objects.filter(item = item).exists():
            # Get a queryset for all items related to the 'item'
            items_to_delete = OrderModel.objects.filter(item=item)
            # Delete all items in the queryset
            items_to_delete.delete()

            # Create new queryset with new quantity items 
            for _ in range(quantity):
                ref_number = random.randrange(100, 10000)
                ref = 'ORD' + str(ref_number)
                createOrder = OrderModel()
                createOrder.orderNumber = ref
                createOrder.item = item 
                createOrder.price = item.price
                createOrder.save()

        else:
            for _ in range(quantity):
                ref_number = random.randrange(100, 10000)
                ref = 'ORD' + str(ref_number)
                createOrder = OrderModel()
                createOrder.orderNumber = ref
                createOrder.item = item 
                createOrder.price = item.price
                createOrder.save()

    itemsCount = OrderModel.objects.filter(item= item).count()

    context = {
        "itemsCount" : itemsCount
    }
        
    return render(request,'order/item_in_cart.html',context)


def DecreaseSpecialQuantityView(request,id):
    if request.method == 'POST':
        special = SpecialsModel.objects.get(id = id)
        item = special.item

        # Retrieve the variable from the session
        current_user = request.session.get('userID')

        if OrderModel.objects.filter(Q(item=item) & Q(currentUser=current_user)).exists():
            cartItem = OrderModel.objects.filter(Q(item=item) & Q(currentUser=current_user)).first()
            cartItem.delete()

        quantity_input = OrderModel.objects.filter(item = item).count()

        context = {
            "quantity_input" : quantity_input
        }

    return render(request,'order/quantity.html',context)

# Special Orders Cart 
def IncreaseSpecialQuantityView(request,id):
    if request.method == 'POST':
        specail = SpecialsModel.objects.get(id = id)
        item = specail.item
        ref_number = random.randrange(100, 10000)
        ref = 'ORD' + str(ref_number)

        createOrder = OrderModel()
        createOrder.currentUser = request.POST.get('orderUser')
        createOrder.table = request.POST.get('orderTable')
        createOrder.orderNumber = ref
        createOrder.item = item
        createOrder.price = specail.special_price
        createOrder.save()

        current_user = createOrder.currentUser
        # Retrieve the variable from the session
        loggedUser = request.session.get('userID')

        if current_user != loggedUser:
            updateCartItems = OrderModel.objects.filter(currentUser = loggedUser)
            updateCartItems.delete()
            # Save a variable to the session
            request.session['userID'] = current_user
        else:
            # Save a variable to the session
            request.session['userID'] = current_user


        quantity_input = OrderModel.objects.filter(item = item).count()

        context = {
            "quantity_input" : quantity_input,
        }

    return render(request,'order/quantity.html',context)