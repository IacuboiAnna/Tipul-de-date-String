sir=input("Introduceti sirul de caractere:")
suma_m=0
suma_c=0
suma_cs=0
for i in sir:
    if ord(i) in range(65,91):
        suma_m+=1
    if ord(i) in range(48,58):
        suma_c+=1
    if (ord(i) in range(33,48)) or (ord(i) in range(58,65)) or (ord(i) in range(91,97)) or (ord(i) in range(123,128)):
        suma_cs+=1

print(suma_m, suma_c, suma_cs)