from random import choice
Wylosowane = set()
while len(Wylosowane) < 6:
    Wylosowane.add(choice(range(1,50)))
for x in Wylosowane:
    print(x)