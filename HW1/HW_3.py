# 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input())
y = int(input())

if x==0 and y==0:
    print("начало координат")
elif x == 0 and y > 0:
    print("ось y, между I и II четвертями")
elif x == 0 and y < 0:
    print("ось y, между III и IV четвертями")
elif y == 0 and x > 0:
    print("ось x, между I и IV четвертями")  
elif y == 0 and x < 0:
    print("ось x, между II и III четвертями")      
elif x > 0 and y > 0:
    print("I")
elif x < 0 < y:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 > y:
    print("IV")  


