from django.shortcuts import render
from.models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.order_by('price')
    return render(request, 'order/menu_list.html', {'menu_items': menu_items})





