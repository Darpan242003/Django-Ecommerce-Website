from django.shortcuts import render
from .forms import DeliveryForm
from django.contrib.auth.models import User
from .models import DeliveryModel


# Create your views here.
def delivery_form(request):

    user_details = User.objects.get(username=request.user)

    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "order_placed.html")

    context = {
        "form": DeliveryForm(instance=user_details),
        "data": DeliveryModel.objects.filter(username=request.user),
    }

    return render(request, "delivery_form.html", context)
