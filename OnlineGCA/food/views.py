from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food
from .forms import ItemForm
from django.template import loader

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
    if form.is_valid():
        form.save()
        return redirect('food:TestItemView')
    return render(request,'food/AddItem.html', {'form':form})