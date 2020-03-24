from math import pi
print ("Wpisz zero dla zakończenia programu")
while True:
    s= input("Znak (+,-,*,/): ")
    if s== '0': break
    if s in ('+','-','*', '/'):
        x=float(input("x= "))
        y=float(input("y= "))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s =='*':
            print("%.2f" % (x*y))
        elif s=='/':
            if y!=0:
                print("%.2f" % (x/y))
            else :
                print("Dziełenie przez zero!")
        else:
            print("Niepoprawny znak operacji!")



