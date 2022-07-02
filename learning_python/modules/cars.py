def car_info(manufacturer, model, **additional_info):
    """Describes information regarding a car"""
    profile = {}
    profile['manufacturer']= manufacturer
    profile['model']= model
    for key, value in additional_info.items():
        profile[key]= value
    return profile
    print(profile)