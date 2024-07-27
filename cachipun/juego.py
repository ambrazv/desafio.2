#Comienzo del Juego

#Libreria
import random

#Variables a definir 

cachipun = ["tijera", "papel", "piedra"]

computador = random.choice(cachipun)

usuario = input("Ingresa tu jugada: ")

# desarrollo 
print(f"Tu jugaste {usuario}")
print(f"Computador jugó {computador}")

if usuario not in cachipun:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
elif usuario == computador:
    print("¡Empate!")
elif (usuario == "piedra" and computador == "tijera") or \
     (usuario == "papel" and computador == "piedra") or \
     (usuario == "tijera" and computador == "papel"):
    print("¡Tú ganaste!")
else:
    print("¡Perdiste!")

    #Fin