from django.shortcuts import render, HttpResponse
from .models import Product, Contact
from math import ceil


# Create your views here.
def index(request):
    items = []
    cat_prods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cat_prods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        items.append([prod, nslides, range(1, nslides)])

    param = {'Prods': items}

    return render(request, "shop/spage.html", param)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        message = request.POST.get('message', "")
        contact_n = Contact(name=name, email=email, phone=phone, message=message)
        contact_n.save()

    return render(request, "shop/contact.html")


def product_view(request, myid):
    prod = Product.objects.filter(id=myid)
    param = {"product": prod[0]}
    return render(request, "shop/product_view.html", param)


def check_out(request):
    params={'items':[1,2,3,4]}

    return render(request, "shop/check_out.html",params)
