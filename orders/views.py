from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from .models import Regular_Pizza_Price, Sicilian_Pizza_Price, toppings, PlaceOrder, Dinner_Platters_Price, Salad_Price, Pasta, Sub, Extra
import json
import datetime



def index(request):
    context = {
        "Regular_Pizza" : list(Regular_Pizza_Price.objects.all()),
        "Sicilian_Pizza" : list(Sicilian_Pizza_Price.objects.all()),
        "toppings" : list(toppings.objects.all()),
        "Dinner_Platters" : list(Dinner_Platters_Price.objects.all()),
        "Salad" : list(Salad_Price.objects.all()),
        "Pasta" : list(Pasta.objects.all()),
        "Sub" : list(Sub.objects.all()),
        "Extra": list(Extra.objects.all())
    }

    return render(request, "orders/index.html", context)

def order(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userprofile:index"))
    context = {
        "Regular_Pizza" : list(Regular_Pizza_Price.objects.all()),
        "Sicilian_Pizza" : list(Sicilian_Pizza_Price.objects.all()),
        "toppings" : list(toppings.objects.all()),
        "Dinner_Platters" : list(Dinner_Platters_Price.objects.all()),
        "Salad" : list(Salad_Price.objects.all()),
        "Pasta" : list(Pasta.objects.all()),
        "Sub" : list(Sub.objects.all()),
        "Extra": list(Extra.objects.all())
    }
    return render(request, "orders/cart.html", context)

def viewcart(request):
    """ Return the order save in cart """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userprofile:index"))
    try:
        price=0
        for item in request.session['cart']:
            price = price + float(item['price'])
        price = round(price, 2)
        return render(request, "orders/viewcart.html", {'cart': request.session['cart'], 'price':price})
    except KeyError:
        return render(request, "orders/viewcart.html")


def orderhistory(request):
    '''Return place order history'''
    print(request.session['buy'])
    return render(request, "orders/orderhistory.html", {"buy": request.session['buy']})
    

def ajax(request):
    """ Return the Price for Pizza Section"""

    if ((not request.is_ajax()) or (not request.method=="POST") or (not request.user.is_authenticated)):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))
    data = {}
    pizza = str(request.POST['pizza'])
    size = str(request.POST['size'])
    addition = str(request.POST['addition'])
    
    if addition == "Special":
        if pizza == "Regular_pizza":
            obj = Regular_Pizza_Price.objects.get(addition="Special")
        else:
            obj = Sicilian_Pizza_Price.objects.get(addition="Special")
        if size == "small":
            data["price"] = obj.small
        else:
            data["price"] = obj.large
        return HttpResponse(json.dumps(data))
    if addition == "3 toppings":
        toppings = request.POST.getlist('toppings[]')
        if pizza == "Regular_pizza":
            obj = Regular_Pizza_Price.objects.get(addition="3 toppings")
        else:
            obj = Sicilian_Pizza_Price.objects.get(addition="3 toppings")
        if size == "small":
            data["price"] = obj.small
        else:
            data["price"] = obj.large
        return HttpResponse(json.dumps(data))
    if addition == "2 toppings":
        toppings = request.POST.getlist('toppings[]')
        if pizza == "Regular_pizza":
            obj = Regular_Pizza_Price.objects.get(addition="2 toppings")
        else:
            obj = Sicilian_Pizza_Price.objects.get(addition="2 toppings")
        if size == "small":
            data["price"] = obj.small
        else:
            data["price"] = obj.large
        return HttpResponse(json.dumps(data))
    if addition == "Cheese":
        if pizza == "Regular_pizza":
            obj = Regular_Pizza_Price.objects.get(addition="Cheese")
        else:
            obj = Sicilian_Pizza_Price.objects.get(addition="Cheese")
        if size == "small":
            data["price"] = obj.small
        else:
            data["price"] = obj.large
        return HttpResponse(json.dumps(data))
    if addition == "1 topping":
        toppings = request.POST.getlist('toppings[]')
        if pizza == "Regular_pizza":
            obj = Regular_Pizza_Price.objects.get(addition="1 topping")
        else:
            obj = Sicilian_Pizza_Price.objects.get(addition="1 topping")
        if size == "small":
            data["price"] = obj.small
        else:
            data["price"] = obj.large
        return HttpResponse(json.dumps(data))



def addtocart(request):
    """ add item in cart for Pizza Section """

    if (not request.user.is_authenticated) or (not request.is_ajax()):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))

    item = {}
    item['pizza'] = request.POST['pizza']
    item['size'] = request.POST['size']
    item['price'] = request.POST['price']
    item['addition'] = request.POST['addition']
    if not request.POST.getlist('toppings[]') == []:
        item['toppings'] = request.POST.getlist('toppings[]')
    if 'cart' not in request.session:
        request.session['cart'] = []
        print("cart is created")
    print(request.session['cart'])
    request.session['cart'].append(item)
    request.session.modified = True
    print("after append")
    print(request.session['cart'])
    return HttpResponse("success")
    


def ajax2(request):
    """ Return the price for Dinner Section. """

    if ((not request.is_ajax()) or (not request.method=="POST") or (not request.user.is_authenticated)):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))
    data = {}
    dinner = str(request.POST['dinner'])
    size = str(request.POST['size'])
    obj = Dinner_Platters_Price.objects.get(item = dinner)
    if size == 'small':
        data["price"] = obj.small
    else:
        data["price"] = obj.large
    return HttpResponse(json.dumps(data))


def addtocart_dinner(request):

    """ add item in cart for dinner Section. """

    if (not request.user.is_authenticated) or (not request.is_ajax()):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))
    item = {}
    item['dinner'] = request.POST["dinner"]
    item['size'] = request.POST["size"]
    item['price'] = request.POST["price"]
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(item)
    request.session.modified = True
    return HttpResponse("success")


def addtocart_pasta_salad(request):

    """ add item in cart for dinner and pasta section. """

    if (not request.user.is_authenticated) or (not request.is_ajax()):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))

    item = request.POST["item"]
    item = json.loads(item)

    print(item)
    print(type(item))

    if 'cart' not in request.session:
        request.session['cart'] = []
        print("cart is created")
    request.session['cart'].append(item)
    request.session.modified = True
    return HttpResponse("success")

def addtocart_sub(request):
    """ add item in cart for sub section. """
    if (not request.user.is_authenticated) or (not request.is_ajax()):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))
    item = {}
    item["sub"] = request.POST["sub"]
    item["size"] = request.POST["size"]
    if not request.POST.getlist('extra[]') == []:
        item['extra'] = request.POST.getlist('extra[]')
    item["price"] = request.POST["price"]
    if 'cart' not in request.session:
        request.session['cart'] = []
        print("cart is created")
    request.session['cart'].append(item)
    request.session.modified = True
    return HttpResponse("success")


def buy(request):
    """ buy function for item in cart """
    if (not request.user.is_authenticated) or (not request.is_ajax()):
        data = {"error": "something went wrong"}
        return HttpResponse(json.dumps(data))
    user = request.user.username
    price = float(request.POST["price"])
    item = request.session['cart']

    p = PlaceOrder(user=user, item=item, price = price)
    p.save()

    request.session['buy'] = []
    request.session['buy'].append(request.session['cart'])
    request.session.modified = True
    
    request.session['buy'].append({"time":str(datetime.datetime.utcnow())})
    request.session.modified = True

    del request.session['cart']
    request.session.modified = True


    return HttpResponse("success")


def placeorder(request):
    """ return html page for owner of website to see orders """
    if not (request.user.is_superuser):
        raise Http404()
    orders = list(PlaceOrder.objects.all())
    return render(request, "orders/placeorder.html", {"orders": orders})
    


    


