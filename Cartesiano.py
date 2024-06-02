def determinar_cuadrante (x, y):
    if x == 0 or y == 0:
        print ("Las coordenadas no deben ser cero.")
    elif x > 0 and y > 0:
        print ("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print ("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print ("El punto se encuentra en el cuadrante IV.")

try:
    x = float (input("Ingrese X: "))
    y = float (input("Ingrese Y: "))
    determinar_cuadrante(x, y)
except ValueError:
    print("Por favor, ingrese numeros validos.")