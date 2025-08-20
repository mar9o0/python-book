def my_profile(first, last, **my_info):
    """Строит словарь с информацией о пользователе"""
    profile = {}
    profile ['first_name'] = first
    profile ['last_name'] = last
    for key, value in my_info.items():
        profile[key] = value
    return profile

user_profile = my_profile('Alina', 'Godova', location = 'Russia', field = 'fizics')
print(user_profile)