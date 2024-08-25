from .models import Shop
from django.shortcuts import render, redirect
from .forms import OrderForm
from rest_framework import generics
from .serializers import OrderSerializer


#
# class OrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = OrderSerializer

def home(request):
    products = Shop.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'index.html', context)


def detail_featured(request):
    productss = Shop.objects.all()
    context = {
        'productss': productss,
    }

    return render(request, 'detail.html', context)


def shop(request):
    products = Shop.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'shop.html', context)


def detail(request, id):
    product = Shop.objects.get(id=id)
    return render(request, 'detail.html', {'product': product})


def order_create_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or wherever you want
    else:
        form = OrderForm()
    return render(request, 'detail.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')
