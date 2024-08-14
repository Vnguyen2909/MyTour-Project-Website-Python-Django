from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User


from .models import Tour, Type_Of_Tour, Photo, Cart, Profile, Order, OrderItem
from .forms import TourForm, Type_Tour, ProfileForm


# Create your views here.
def index(request):
    data = {"tours": Tour.objects.all(), "types": Type_Of_Tour.objects.all()}
    return render(request, "index.html", data)


@login_required(login_url="members/login_user")
def create_tour(request):
    submitted = False

    if request.method == "POST":
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create_tour?submitted=True")
    else:
        form = TourForm()
        if "submitted" in request.GET:
            submitted = True
    return render(request, "create_tour.html", {"form": form, "submitted": submitted})


def detail_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)

    data = {
        "tour": Tour.objects.get(pk=tour_id),
        "photos": tour.photo_set.all(),
    }
    return render(request, "detail_tour.html", data)


def update_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    form = TourForm(request.POST or None, request.FILES or None, instance=tour)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "update_tour.html", {"venue": tour, "form": form})


def delete_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    tour.delete()
    return redirect("/")


def type_tour(request, type_id):
    type_tour = Type_Of_Tour.objects.get(pk=type_id)
    data = {"tours": type_tour.tour_set.all(), "types": Type_Of_Tour.objects.all()}
    print("data:", type_tour.tour_set.all())
    # tours = type_tour.tour_set.all()

    return render(
        request,
        "type_tour.html",
        data,
    )


@login_required(login_url="members/login_user")
def all_type_tour(request):
    data = {"types": Type_Of_Tour.objects.all()}

    return render(
        request,
        "all_type_tour.html",
        data,
    )


def create_type_tour(request):
    submitted = False

    if request.method == "POST":
        form = Type_Tour(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create_type_tour?submitted=True")
    else:
        form = Type_Tour()
        if "submitted" in request.GET:
            submitted = True

    return render(
        request, "create_type_tour.html", {"form": form, "submitted": submitted}
    )


def delete_type_tour(request, type_tour_id):
    type = Type_Of_Tour.objects.get(pk=type_tour_id)
    type.delete()
    return redirect("/all_type_tour")


def create_profile(request):
    submitted = False
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect("/create_profile?submitted=True")
    else:
        form = ProfileForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "create_profile.html", {"form": form, "submitted": submitted}
    )


# def update_profile(request):
#     profile = Profile.objects.get(user=request.user)

#     form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     return render(request, "update_profile.html", {"form": form})


def update_profile(request):
    if not Profile.objects.filter(user=request.user):
        profile = Profile()
        profile.user = request.user
        profile.save()

    if request.method == "POST":
        request.user.first_name = request.POST["first_name"]
        request.user.last_name = request.POST["last_name"]
        request.user.email = request.POST["email"]
        User.save(request.user)

        profile = Profile.objects.get(user=request.user)
        profile.user = request.user
        profile.phone = request.POST["phone"]
        profile.city = request.POST["city"]
        profile.email = request.POST["city"]

        if "profile_pic" in request.FILES:
            profile.profile_pic = request.FILES["profile_pic"]
        else:
            profile.profile_pic = None

        profile.save()
    data = {"profile": Profile.objects.get(user=request.user)}
    return render(request, "update_profile.html", data)


def add_photo(request):
    user = request.user

    tours = Tour.objects.all()

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist("images")

        if data["tour"] != "none":
            tour = Tour.objects.get(id=data["tour"])
        else:
            tour = None

        for image in images:
            photo = Photo.objects.create(
                tour=tour,
                images=image,
            )

        return redirect("/")

    context = {"tours": tours}
    return render(request, "add_photo.html", context)


@login_required(login_url="members/login_user")
def add_to_cart(request):
    if request.method == "POST":
        tour_id = int(request.POST.get("tour_id"))
        tour_check = Tour.objects.get(id=tour_id)
        if tour_check:
            if Cart.objects.filter(user=request.user.id, tour=tour_id):
                return JsonResponse({"status": "Tour already in cart!"})
            else:
                Cart.objects.create(
                    user=request.user,
                    tour_id=tour_id,
                )
                return JsonResponse({"status": "Tour added successfully"})
        else:
            return JsonResponse({"status": "Tout not found!"})

    return redirect("/")


def all_my_cart(request):
    data = {"carts": Cart.objects.filter(user=request.user)}

    return render(request, "all_my_cart.html", data)


def all_my_orders(request):
    data = {
        "orders": Order.objects.filter(user=request.user),
        "orders_admin": Order.objects.filter(),
    }

    return render(request, "all_my_orders.html", data)


def delete_cart_item(request, tour_id):
    if Cart.objects.filter(user_id=request.user.id, tour_id=tour_id):
        cart_item = Cart.objects.get(user_id=request.user.id, tour_id=tour_id)
        cart_item.delete()
    return redirect("/all_my_cart")


def check_out(request):
    total_price_cart = 0
    carts = Cart.objects.filter(user=request.user)
    for item in carts:
        total_price_cart += int(item.tour.price)

    data = {
        "carts": carts,
        "total_price_cart": total_price_cart,
        "user_pro": Profile.objects.filter(user=request.user).first(),
    }

    return render(request, "checkout.html", data)


def place_order(request):
    if request.method == "POST":
        if not Profile.objects.filter(user=request.user):
            user_pro = Profile()
            user_pro.user = request.user
            user_pro.phone = request.POST.get("phone")
            user_pro.email = request.POST.get("email")
            user_pro.city = request.POST.get("city")
            user_pro.save()

        new_order = Order()
        new_order.user = request.user
        new_order.phone = request.POST.get("phone")
        new_order.email = request.POST.get("email")
        new_order.city = request.POST.get("city")

        carts = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in carts:
            cart_total_price += int(item.tour.price)
        new_order.total_price = cart_total_price
        new_order.save()

        new_order_item = Cart.objects.filter(user=request.user)
        for item in new_order_item:
            OrderItem.objects.create(
                order=new_order,
                product=item.tour,
                price=item.tour.price,
            )

        Cart.objects.filter(user=request.user).delete()

    return redirect("/all_my_orders")
    


def detail_order(request, order_id):
    order = Order.objects.filter(id=order_id).filter(user=request.user).first()
    data = {"order_item": OrderItem.objects.filter(order=order), "order": order}

    return render(request, "detail_order.html", data)


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = True
    order.save()
    return redirect("/all_my_orders")


def refuse_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = None
    order.save()
    return redirect("/all_my_orders")


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect("/all_my_orders")

