import os

def Addition(x, y):
    z = x + y
    print(f"La reponse est {z}")


def Soustraction(x, y):
    z = x - y 
    print(f"La reponse est {z}")

def Multiplication(x, y):
    z = x * y
    print(f"La reponse est {z}")

def Division (x, y):
    z = x / y 
    print(f"La reponse est {z}")

try: 
    nombre1 = int(input("Quel est le premier nombre que vous souhaitez calculer ?: "))
    nombre2 = int(input("Quel est le deuxième nombre que vous souhaitez calculer ?: "))
    print("Que veux-tu faire avec les nombres?:\n ")
    print("  [1] Je veux une Addition !\n")
    print("  [2] Je veux une Soustraction !\n")
    print("  [3] Je veux une Multiplication !\n")
    print("  [4] Je veux une Division !\n")
    operator = int(input(">: "))

    if (operator == 1):
        Addition(nombre1, nombre2)
    elif (operator == 2):
        Soustraction(nombre1, nombre2)
    elif (operator == 3):
        Multiplication(nombre1, nombre2)
    elif (operator == 4):
        Division(nombre1, nombre2)

    else: 
        print("Les seules possibilitées sont 1, 2, 3 et 4.")

except ValueError:
    print("Merci d'insérer une valeur réelle.")
except:
    print("Une erreur inconnue s'est produite.")
