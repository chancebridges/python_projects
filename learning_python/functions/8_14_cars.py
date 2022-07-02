def car_info(manufacturer, model, **additional_info):
    """Describes information regarding a car"""
    profile = {}
    profile['manufacturer']= manufacturer
    profile['model']= model
    for key, value in additional_info.items():
        profile[key]= value
    return profile

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)