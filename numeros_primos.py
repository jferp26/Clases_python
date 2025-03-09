import time

def primsos():
    primos=[]
    num=int(input("intoduce el numero final: "))
    inicio=time.time()
    for i in range (2,num+1):
         for j in primos:
            if i % j==0:
                break
    else:
            print(i)
            
            primos.append(i)
    fin=time.time()
    print(primos)
    print(f"ha tardado{fin-inicio}")

primsos()
