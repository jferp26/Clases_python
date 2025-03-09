def tablamultipilcar(num):
    #num=int(input("introduzca un numero:"))
    for i in range(1,11):
        print(str(num) + "x" + str(i)+"="+ str(num*i))
        print(f"{num} x {i}={num*i}")
numero_usuario=int(input("introduzca un numero:"))
tablamultipilcar(numero_usuario)
print(f"el numero elegido por el usuario fue el {numero_usuario}")