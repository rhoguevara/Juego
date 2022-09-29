#Importando:
from random import randint
import os

#Constante de color:
RED = '\033[31m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

#titulo:
titulo = "COMBATE DE GOKU VS VEGETA"
print(MAGENTA + '-' * 15 + titulo + '-' * 15 + RESET + '\n')

#Variables:
VIDA_INICIAL_GOKU = 100
VIDA_INICIAL_VEGETA = 100

vida_goku = VIDA_INICIAL_GOKU
vida_vegeta = VIDA_INICIAL_VEGETA

len_barra = 40

#Desarrollo:
while vida_goku > 0 and vida_vegeta > 0:
    #Turno de vegeta:
    print("TURNO DE VEGETA")
    ataque_vegeta = randint(1, 2)
    if ataque_vegeta == 1:
        print("Vegeta ataca con Ataque BigBang ==>")
        vida_goku = vida_goku - 20
    else:
        print("Vegeta ataca con Granadas Explosivas ==>")
        vida_goku = vida_goku - 19
    
    #Para no mostrar numeros negativos:
    if vida_vegeta < 0:
        vida_vegeta = 0
    if vida_goku < 0:
        vida_goku = 0
    
    #Mostramos barras de vida de Goku y Vegeta:
    barra_vida_vegeta = int((vida_vegeta * len_barra / VIDA_INICIAL_VEGETA))
    print(YELLOW + "VEGETA: [{}{}] ({}/{})".format("#" * barra_vida_vegeta, " " * (len_barra - barra_vida_vegeta), 
    vida_vegeta, VIDA_INICIAL_VEGETA) + RESET)
    
    barra_vida_goku = int((vida_goku * len_barra / VIDA_INICIAL_GOKU))
    print(YELLOW + "  GOKU: [{}{}] ({}/{})".format("#" * barra_vida_goku, " " * (len_barra - barra_vida_goku), 
    vida_goku, VIDA_INICIAL_GOKU) + RESET)
    
    #Pulsamos enter para resetear la ventana:
    input(RED + " Enter " + RESET + "para continuar...")
    os.system("clear")

    #Turno de Goku:
    print("TURNO DE GOKU")
    ataque_goku = None
    while ataque_goku != "K" and ataque_goku != "G" and ataque_goku != "P" and ataque_goku != "A":
        ataque_goku = input("¿Que ataque deseas hacer? [K]Kamehameha, [G]Genkidama, [P]PuñoDeDragon, [A]AFK: ")
        if ataque_goku == "K":
            print("Goku ataca con Kamehameha ==>")
            vida_vegeta = vida_vegeta - 19
        elif ataque_goku == "G":
            print("Goku ataca con Genkidama ==>")
            vida_vegeta = vida_vegeta - 20
        elif ataque_goku == "P":
            print("Goku ataca con PuñoDeDragon ==>")
            vida_vegeta = vida_vegeta - 21
        elif ataque_goku == "A":
            vida_vegeta = vida_vegeta - 0
    
    #Para no mostrar numeros negativos:
    if vida_vegeta < 0:
        vida_vegeta = 0
    if vida_goku < 0:
        vida_goku = 0
    
    #Mostramos barras de vida de Goku y Vegeta:
    barra_vida_vegeta = int((vida_vegeta * len_barra / VIDA_INICIAL_VEGETA))
    print(YELLOW + "VEGETA: [{}{}] ({}/{})".format("#" * barra_vida_vegeta, " " * (len_barra - barra_vida_vegeta), 
    vida_vegeta, VIDA_INICIAL_VEGETA) + RESET)

    barra_vida_goku = int((vida_goku * len_barra / VIDA_INICIAL_GOKU))
    print(YELLOW + "  GOKU: [{}{}] ({}/{})".format("#" * barra_vida_goku, " " * (len_barra - barra_vida_goku), 
    vida_goku, VIDA_INICIAL_GOKU) + RESET)
    
    #Pulsamos enter para resetear la ventana:
    input(RED + " Enter " + RESET + "para continuar...")
    os.system("clear")

#Salida:    
if vida_goku > vida_vegeta:
    print("¡Felicidades, Ganaste el juego!")
elif vida_vegeta > vida_goku:
    print("¡Vegeta le gano a Goku, suerte para la proxima!")