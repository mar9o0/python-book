friends = ['Barbara', 'Casandra', 'Jess', 'Roberto', 'Paul']
not_friends = ['ROBERTO', 'Paul', 'Marta', 'Silk', 'Daniel']
for not_friend in not_friends:
    if not_friend.lower() in [not_friend.lower() for not_friend in friends]:
        print("Такое имя уже есть в базе()")
    else:
        print("Мы добавили вас в нашу базу хороших людей!)")