import tkinter as tk
import random
import tkinter as tk
import pygame 
"""
pygame.mixer.init()

def reproducir_musica():
    pygame.mixer.music.load("musica_fondo.mp3")
    pygame.mixer.music.play(loops=-1)

def detener_musica():
    pygame.mixer.music.stop()

ventana = tk.Tk()
ventana.title("Interfaz con Música")


boton_detener = tk.Button(ventana, text="Detener Música", command=detener_musica)
boton_detener.pack()


etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenido! La música está en reproducción.")
etiqueta_bienvenida.pack()


reproducir_musica()
"""
#ventana.mainloop()

puntos_usuario = 0
puntos_computadora = 0

def jugar(opcion_usuario):
    global puntos_usuario, puntos_computadora
    opciones = ['Piedra', 'Papel', 'Tijera']
    opcion_computadora = random.choice(opciones)
    etiqueta_computadora.config(text=f"Computadora: {opcion_computadora}")

    if opcion_usuario == opcion_computadora:
        resultado = "¡Es un empate!"
    elif (opcion_usuario == 'Piedra' and opcion_computadora == 'Tijera') or \
         (opcion_usuario == 'Papel' and opcion_computadora == 'Piedra') or \
         (opcion_usuario == 'Tijera' and opcion_computadora == 'Papel'):
        resultado = "¡Ganaste esta ronda!"
        puntos_usuario += 1
    else:
        resultado = "La computadora gana esta ronda."
        puntos_computadora += 1
    
    etiqueta_resultado.config(text=f"Resultado: {resultado}")
    etiqueta_puntos.config(text=f"Usuario: {puntos_usuario} | Computadora: {puntos_computadora}")


    if puntos_usuario == 2:
        etiqueta_final.config(text="¡Felicidades, ganaste la partida!")
        deshabilitar_botones()
    elif puntos_computadora == 2:
        etiqueta_final.config(text="La computadora ganó la partida.")
        deshabilitar_botones()

def deshabilitar_botones():
    boton_piedra.config(state=tk.DISABLED)
    boton_papel.config(state=tk.DISABLED)
    boton_tijera.config(state=tk.DISABLED)

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")


etiqueta_computadora = tk.Label(ventana, text="Computadora: -")
etiqueta_computadora.pack()

etiqueta_resultado = tk.Label(ventana, text="Resultado: -")
etiqueta_resultado.pack()

etiqueta_puntos = tk.Label(ventana, text="Usuario: 0 | Computadora: 0")
etiqueta_puntos.pack()

etiqueta_final = tk.Label(ventana, text="")
etiqueta_final.pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack()

imagen_piedra = tk.PhotoImage(file="piedra.png")
imagen_papel = tk.PhotoImage(file="papel.png")
imagen_tijera = tk.PhotoImage(file="tijera.png")


boton_piedra = tk.Button(frame_botones, image=imagen_piedra, command=lambda: jugar('Piedra'))
boton_piedra.pack(side=tk.LEFT)

boton_papel = tk.Button(frame_botones, image=imagen_papel, command=lambda: jugar('Papel'))
boton_papel.pack(side=tk.LEFT)

boton_tijera = tk.Button(frame_botones, image=imagen_tijera, command=lambda: jugar('Tijera'))
boton_tijera.pack(side=tk.LEFT)

ventana.mainloop()
