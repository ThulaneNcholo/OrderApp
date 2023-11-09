from django.shortcuts import render
from .models import *

# Create your views here.
def ListMenuItemsView(request):
    return render(request,'menu/list_items.html')

def CartItemsView(request):
    # Retrieve the variable from the session
    loggedUser = request.session.get('userID')
    orderCount = OrderModel.objects.filter(currentUser = loggedUser).count()

    # Retrieve the variable from the session
    userID = request.session.get('userID')

    orders = OrderModel.objects.filter(currentUser = userID).order_by('-date_created')


    total = 0
    for i in orders:
        total = total + i.price

    context = {
        "orders" : orders,
        "total" : total,
        "orderCount" : orderCount,
        "userID" : userID
    }

    return render(request,'menu/cart_items.html',context)

def RemoveOrderView(request,id):
    if request.method == 'POST':
        removeOrder = OrderModel.objects.get(id = id)
        removeOrder.delete()
        # Retrieve the variable from the session
        userID = request.session.get('userID')

        orders = OrderModel.objects.filter(currentUser = userID).order_by('-date_created')

        context = {
            "orders" : orders,
        }


    return render(request,'partials/orders.html',context)

def PlaceOrderView(request):
    if request.method == 'POST':
        currentUser = request.POST.get('currentUser')
        orders = OrderModel.objects.filter(currentUser = currentUser)
        for i in orders:
            updateOrder = OrderModel.objects.get(id = i.id)
            updateOrder.status = 'Confirmed'
            updateOrder.save()

        context = {
            "orders" : orders,
        }
        

    return render(request,'partials/orders.html',context)
