def evaluar_palabra (palabra):
    longitud = len (palabra)
    if 4 <= longitud <=8:
        print (f"La palabra es correcta")
    elif longitud <4:
        print (f"hacen falta letras. Solo tiene {longitud} letras")
    else:
        print (f"Sobran letras. Tiene {longitud} letras")
        
palabra_ingresada = input ("Ingrese una palabra: ")
evaluar_palabra (palabra_ingresada)
        