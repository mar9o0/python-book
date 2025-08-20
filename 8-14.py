def make_car(proizvod, model, **avto_info):
    """Строит словарь с информацией о пользователе"""
    avto = {}
    avto ['proizvod_avto'] = proizvod
    avto ['model_avto'] = model
    for key, value in avto_info.items():
        avto[key] = value
    return avto

car = make_car('Hinday', 'Accent', color = 'blue', tow_packeg = True)
print(car)