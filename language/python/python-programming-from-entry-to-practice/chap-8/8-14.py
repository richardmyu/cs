def make_car(brand, model, **topp):
    car_info = {}
    car_info['brand'] = brand
    car_info['model'] = model

    for key, val in topp.items():
        car_info[key] = val

    return car_info


car = make_car('subaru', 'outback', color='red', tow_package=True)

print(car)
