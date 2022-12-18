# 4. Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

quarter = int(input())
while quarter < 1 or quarter > 4:
    print("Это не номер четверти! Попробуйте ещё раз:")
    quarter = int(input())
if quarter == 1:
    print("x > 0, y > 0")
elif quarter == 2:
    print("x < 0, y > 0")
elif quarter == 3:
    print("x < 0, y < 0")
elif quarter == 4:
    print("x > 0, y < 0")      
