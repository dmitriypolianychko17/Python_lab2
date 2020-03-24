list=[1,2,3,4,5,6,7,8,9]
suma=sum(list)
lista=str(list)
print(f"Suma wynosi: {suma}")
with open('list.txt', 'w') as file:
    for line in lista:
        file.write(line + '\n')

with open(r"list.txt", "r") as file:
    for line in file:
        print(line)