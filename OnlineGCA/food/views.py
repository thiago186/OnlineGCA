from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food
from .forms import ItemForm
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
def TestHomeView(request):
    return HttpResponse('Hello World')

def TestItem(request):
    items = Food.objects.all()
    template = loader.get_template('food/TestItem.html')
    context = {
        'item_list': items,
    }
    return HttpResponse(template.render(context, request))

def TestDetailView(request, item_id): 
    item = Food.objects.get(pk = item_id)
    context = {
            'item': item,
    }
    return render(request, 'food/TestDetail.html', context)

def TestAddItem(request):
    form = ItemForm(request.POST or None)
    if form.is_valid(form):
        form.instance.username = request.user
        form.save()
        return redirect('food:TestItemView')
    return render(request,'food/AddItem.html', {'form':form})

def TestUpdateItem(request, item_id):
    item = Food.objects.get(id = item_id)
    form = ItemForm(request.POST or None, instance= item)
    if form.is_valid():
        form.save()
        return redirect('food:TestItemView')
    return render(request, 'food/AddItem.html', {'form':form, 'item': item})

def DeleteItem(request, item_id):
    item = Food.objects.get(id = item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:TestItemView')
    return render(request, 'food/DeleteConfirmation.html', {'item': item})


