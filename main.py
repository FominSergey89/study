#hours = 19
#minutes = 52
#step_minutes = 260


# %24 это мы обнуляем день, так как в одном дне 24 часа
#new_hours = (hours + (minutes + step_minutes) // 60) % 24
#new_minutes = (minutes + step_minutes) % 60
#print (new_hours, new_minutes)


# Домашнее задание урок 1 задание 1
#time = 400153
#sek = time % 60
#minutes = (time // 60) % 60
#hours = (time // 3600) % 24
#days = time // 86400
#print(days, 'дня', hours, 'часов', minutes, 'минут', sek, 'секунд')

#param = int(input('Сколько месяцев году?'))
#if param == 12:
#    print('Поздравляем вы угадали')
#else:
#    print('Не правильно. Правильный ответ 12')

#print("""Привет! Как у тебя дела?
#Все хорошо. Как у тебя?
#У меня тоже отлично!""")

#new = 'как дела?'
#print('Привет ' + new)

#print('spam' * 3)


#bremen_music = ['кот', 'пес', 'осел', 'петух', 'вася']
#for i in bremen_music:
#    print(i)
#print(bremen_music[::-1])
#print(len(bremen_music))

cub_number = list(range(1,1001,2))
for i in cub_number:
    i = i ** 3
    print(i)