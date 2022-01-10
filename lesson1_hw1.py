time = 400153
sek = time % 60
minutes = (time // 60) % 60
hours = (time // 3600) % 24
days = time // 86400
print(days, 'дня', hours, 'часов', minutes, 'минут', sek, 'секунд')