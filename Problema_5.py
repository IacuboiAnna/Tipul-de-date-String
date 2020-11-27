sir=input("Introduceti posibilul CNP al persoanei:")
if len(sir)==13:
    i=0
    while (i!=len(sir)) and (ord(sir[i]) in range(48,58)): 
        i+=1
    if i==len(sir):
        print('CNP-ul este corect')
    else:
        print('CNP-ul este incorect')
else:
    print('CNP-ul este incorect')