class Registro:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def calculoinventario(self):
        return self.precio * self.stock
    
    def muestrainventario(self):
        return f"El valor del inventario de '{self.nombre}' es: {self.calculoinventario()}"

def menu():
    productos = []
    
    while True:
        print("--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                nombre = input("Nombre del producto: ")
                
                try:
                    precio = float(input("Precio unidad en euros:"))
                    stock = int(input("Cantidad en stock: "))
                    
                    if precio <= 0 or stock < 0:
                        raise ValueError("El precio y el stock deben ser positivos.")
                    
                    producto = Registro(nombre, precio, stock)
                    productos.append(producto)
                    print(f"Producto '{nombre}' agregado correctamente.")
                
                except ValueError as e:
                    print(f"Error: {e}. Ingrese valores numericos validos.")
            
            elif opcion == 2:
                if not productos:
                    print("No hay productos registrados")
                else:
                    for producto in productos:
                        print(producto.muestrainventario())
            
            elif opcion == 3:
                print("hasta luego")
                break
            
            else:
                print("Opcion no valida. Intente de nuevo")
        
        except ValueError:
            print("Error: introduce un numero del menu")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
        

 