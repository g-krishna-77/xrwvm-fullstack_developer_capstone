from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "Nissan", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "German engineering excellence"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Reliable and efficient"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], description=data['description'])
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "Sedan", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year']
        )
