# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_sec = int(input('Please enter time in seconds: '))
total_min = time_sec // 60
rest_min = total_min % 60
time_hour = total_min // 60
rest_sec = time_sec % 60

if len(str(rest_min)) < 2:
    rest_min = '0' + str(rest_min)
if len(str(time_hour)) < 2:
    time_hour = '0' + str(time_hour)
if len(str(rest_sec)) < 2:
    rest_sec = '0' + str(rest_sec)

print(f'{time_sec} seconds are converted to {time_hour}:{rest_min}:{rest_sec} (hh:mm:ss).')
