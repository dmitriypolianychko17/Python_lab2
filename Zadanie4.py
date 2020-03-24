from math import pi
print ("Wpisz zero dla zakończenia programu")
while True:
    s= input("Znak (+,-,*,/, kolo): ")
    if s== '0': break
    if s in ('+','-','*', '/', 'kolo'):
        if s== 'kolo':
            r = float(input("r="))
            print("%.2f" % (pi * r * r))
        elif s == '+':
            x = float(input("x= "))
            y = float(input("y= "))
            print("%.2f" % (x+y))
        elif s == '-':
            x = float(input("x= "))
            y = float(input("y= "))
            print("%.2f" % (x-y))
        elif s =='*':
            x = float(input("x= "))
            y = float(input("y= "))
            print("%.2f" % (x*y))
        elif s=='/':
            x = float(input("x= "))
            y = float(input("y= "))
            if y!=0:
                print("%.2f" % (x/y))
            else :
                print("Dziełenie przez zero!")
        else:
            print("Niepoprawny znak operacji!")
