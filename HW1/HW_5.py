# 5. Напишите программу, которая принимает на вход 
# координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(round(dist,3))