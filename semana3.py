"""""
def imprimir_tabla(numero, hasta):
    contador = 1
    while contador <= hasta:
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")
        contador += 1

# Ciclo principal
while True:
    
        numero = int(input("Ingrese el número de la tabla que desea imprimir: "))
        hasta = int(input(f"¿Hasta qué número desea multiplicar {numero}? "))

        imprimir_tabla(numero, hasta)
        opcion = input("¿Desea imprimir otra tabla de multiplicar? (sí/no): ").strip().lower()
        
        if opcion != 'no':
            print("¡Hasta luego!")
            break 
"""""



#for
"""
def info(nom, *materias):
     n = 1
     print(f"Estudiantes: {nom}")
     for m in materias:
          print(f"{n}-{m}")
          n+=1

info("juan", "programacion", "bases de datos", "redes")
    """



def contar(lista_palabras):
    contador = 0

    for palabra in lista_palabras:
        if letra in palabra:
            if letra.lower() == 'a':
                contador += 1

    return contador


#ejemplo
palabras = ("manzana", "banana", "aguacate", "almendra", "naranja")
resultado = (palabras) 

print(f"La letra 'a' se repite {resultado} veces en la lista de palabras.")