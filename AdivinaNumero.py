from random import randint
vidas = 8
intentos = 0
nombre = ""

print("Bienvenido a Adivina el numero")
nombre = input("Cual es tu nombre: ")
numero = randint(0, 101)
print(f"Hola {nombre}, ya tengo mi numero esta entre el 1 y el 100, podes adivinar cual es?")
intentos = 0
print(numero)


while vidas > 0:
    numero_elegido = int(input("Que numero estoy pensando: "))
    intentos+=1
    if (numero_elegido < 1 or numero_elegido > 100):
        print("El numero elegido esta fuera del rango estipulado, acabas de perder una vida por no seguir las reglas")
    elif (numero_elegido > numero):
        print(f"El numero {numero_elegido} es mas grande que el numero que pense yo")
    elif (numero_elegido < numero):
        print(f"El numero {numero_elegido} es mas chico que el numero que pense yo")
    else:
        print("----------------------------------------------------------------")
        print(f"ADIVINASTE, el numero {numero_elegido}, es el numero que eleji")
        print("--------------------------------------------------------------")
        print(f"Tuviste {intentos} intentos y te quedaron {vidas} vidas")
        print("----------------------------------------------------------------")
        print(f"Felicitaciones {nombre}, acabas de ganar el juego")
        break
    vidas -= 1
else:
    print("-------------------------------------------------")
    print("Te quedaste sin vidas")
    print("-------------------------------------------------")
    print("Game Over")
    print("-------------------------------------------------")

