import math
a = int(input("Podaj a= "))
b = int(input("Podaj b= "))
c = int(input("Podaj c= "))
D = b ** 2 - 4 * a * c
print(f"Dyskryminant wynosi: {D}")
if D < 0:
  print("Корней нет")
elif D == 0:
  x = -b / 2 * a
  print (x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print(f"X1 wynosi: {x1}")
  print(f"X2 wynosi: {x2}")