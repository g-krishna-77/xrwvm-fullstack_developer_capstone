from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import logging

from .models import CarMake, CarModel
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# --------------------- User Authentication ---------------------

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    data = {"userName": username}

    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}

    return JsonResponse(data)


@csrf_exempt
def logout_user(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    username_exist = False

    try:
        User.objects.get(username=username)
        username_exist = True
    except:
        logger.debug(f"{username} is a new user")

    if not username_exist:
        user = User.objects.create_user(username=username, password=password,
                                        first_name=first_name, last_name=last_name, email=email)
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "error": "Already Registered"})


# --------------------- Dealer Views (stubs for future) ---------------------

def get_dealerships(request):
    # Placeholder: Implementation completed in later labs
    pass


def get_dealer_reviews(request, dealer_id):
    pass


def get_dealer_details(request, dealer_id):
    pass


def add_review(request):
    pass


# --------------------- Car Make & Model Views ---------------------

def get_cars(request):
    """
    Returns all car models and their corresponding makes.
    Populates database automatically the first time it's called if empty.
    """
    count = CarMake.objects.count()

    if count == 0:
        initiate()

    car_models = CarModel.objects.select_related('car_make').all()
    cars = []

    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name,
            "Type": car_model.type,
            "Year": car_model.year
        })

    return JsonResponse({"CarModels": cars})
