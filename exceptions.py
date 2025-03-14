
def calculadora():





    try:
         x= int(input("introduzca un numero: "))
         y= int(input("introduzca un numero distinto: "))

         print(x/y)
    
    except ZeroDivisionError:
        print("no se puede dividir entre cero")

    except Exception as e:
        print(f"Ha ocurrido un error {e}")

    finally:
        print ("esto se ejecuta SIEMPRE")

calculadora()