from django.shortcuts import render,redirect
from .models import Car
from .forms import CarsForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarsForm()
	if request.method == "POST":
		form = CarsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Car Created Successfully.")
			return redirect("car-list")
	context = {
        "form":form
    }
	return render(request, 'car_create.html', context)


def car_update(request, car_id):
	obj = Car.objects.get(id=car_id)
	form = CarsForm(instance=obj)
	if request.method == "POST":
		form = CarsForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			messages.success(request, "Car Updated Successfully.")
			return redirect("car-list")
	context = {
        "obj":obj,
        "form":form
    }
	return render(request, 'car_update.html', context)


def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	messages.error(request, "Car Deleted Successfully.")
	return redirect("car-list")
