from django.shortcuts import render, redirect
from base.models import ProductsModel, CategoryModel, CartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.


def home(request):
    trend = False
    offer = False

    # if 'q' in request.GET:
    #     q=request.GET['q']
    #     cat=CategoryModel.objects.get(category_name__icontains=q)
    #     all_products=ProductsModel.objects.filter(Q(product_name__icontains=q)|Q(product_desc__icontains=q)|Q(product_category=cat))

    if "q" in request.GET:
        q = request.GET["q"]
        try:
            cat = CategoryModel.objects.get(category_name__icontains=q)
            all_products = ProductsModel.objects.filter(Q(product_category=cat))
        except:
            all_products = ProductsModel.objects.filter(
                Q(product_name__icontains=q) | Q(product_desc__icontains=q)
            )
            print(bool(all_products))  # False
            print(all_products)  # <[QuerySet]>

    elif "cat" in request.GET:
        cat = CategoryModel.objects.get(category_name__icontains=request.GET["cat"])
        all_products = ProductsModel.objects.filter(product_category=cat)

    elif "trending" in request.GET:
        all_products = ProductsModel.objects.filter(trending=True)
        trend = True

    elif "offer" in request.GET:
        all_products = ProductsModel.objects.filter(offer=True)
        offer = True

    else:
        all_products = ProductsModel.objects.all()

    all_category = CategoryModel.objects.all()

    if request.user.is_authenticated:
        cart_products = CartModel.objects.filter(host=request.user)
        cart_count = cart_products.count()
    else:
        cart_products = CartModel.objects.none()
        cart_count = 0
        
    context = {
        "data": all_products,
        "all_category": all_category,
        "trend": trend,
        "offer": offer,
        "cart_count": cart_count,
    }

    return render(request, "home.html", context)


def add_product(request):
    all_category = CategoryModel.objects.all()

    if request.method == "POST":
        product_category = request.POST["category_attr"]
        product_name = request.POST["product_name"]
        product_desc = request.POST["product_desc"]
        product_price = request.POST["product_price"]
        product_image = request.FILES.get("product_image", "default.jpeg")

        pk_cat_model = CategoryModel.objects.get(category_name=product_category)

        ProductsModel.objects.create(
            product_category=pk_cat_model,
            product_name=product_name,
            product_desc=product_desc,
            product_price=product_price,
            product_image=product_image,
        )

        return redirect("home")

    return render(request, "add_product.html", {"all_categories": all_category})


@login_required
def cart(request):

    cart_products = CartModel.objects.filter(host=request.user)
    cart_count = cart_products.count()

    totalamount = 0
    for i in cart_products:
        totalamount += i.total_price


    context = {
        "cart_products": cart_products,
        "TA": totalamount,
        "cart_count": cart_count,
    }

    return render(request, "cart.html", context)


# @login_required
def addtocart(request, pk):
    pro = ProductsModel.objects.get(id=pk)

    try:
        c = CartModel.objects.get(
            Q(product_name=pro.product_name) & Q(host=request.user)
        )
        c.quantity += 1
        c.total_price += c.product_price
        c.save()
        return redirect("cart")

    except:
        CartModel.objects.create(
            product_category=pro.product_category,
            product_name=pro.product_name,
            product_desc=pro.product_desc,
            product_price=pro.product_price,
            product_image=pro.product_image,
            quantity=1,
            total_price=pro.product_price,
            host=request.user,
        )
        if request.user.is_authenticated:
            return redirect("cart")
        else:
            return redirect("login")


@login_required
def removefromcart(request, pk):
    pro = CartModel.objects.get(id=pk)

    pro.delete()

    return redirect("cart")
