from math import pi
print ("Wpisz zero dla zakończenia programu")
while True:
    s= input("Znak (+,-,*,/, kolo): ")
    if s== '0': break
    if s in ('+','-','*', '/', 'kolo'):
        if s== 'kolo':
            my_file = open('kolo.txt', 'w')
            r = float(input("r="))
            my_file.write(str(f"Radius: {r}     "))
            my_file.write(str(f"Pole kola: {pi * r * r}"))
            my_file.close()
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