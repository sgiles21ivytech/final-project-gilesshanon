from django.shortcuts import render, get_object_or_404
from.models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.order_by('price')
    return render(request, 'order/menu_list.html', {'menu_items': menu_items})


def menu_detail(request, pk):
    menu = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'order/menu_detail.html', {'menu': menu})



