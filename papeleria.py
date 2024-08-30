"""
Una papeleria vende cuadernos y lapices. los cuadernos pueden ser de 50 hojas o de 100 hojas. Los
lapices pueden ser de grafito o de colores. El precio de venta es igual al precio de compra 
multiplicado por 1.30 que corresponde al margen de ganancia. La papeleria requiere construir un programa 
que le permita registrar y visualizar por los menos 2 articulos de item. Todos los cuadernos son marca
HOJITA y los lapices son marca RAYAS ya que la papeleria es un distribuidor exclusivo.
"""

class Item:
    def __init__(self, tipo, info, precio_compra):
        self.tipo = tipo
        self.info = info
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30

    def mostrar_datos(self):
        print("***PAPELERIA***\n"+
        f"Tipo: {self.tipo}\n"+
        f"Informacion: {self.info}\n"+
        f"Precio de compra: ${self.precio_compra:.2f}\n"+
        f"Precio de venta: ${self.precio_venta:.2f}\n")

def registrar_datos():
    articulos = []

    for _ in range(2):
        tipo = "Cuaderno"
        info = input("Especificacion del cuaderno (50 o 100 HOJAS): ")
        precio_compra = float(input("precio de compra del cuaderno: "))
        print("*" * 25)
        cuaderno = Item(tipo, f"{info} hojas, MARCA HOJITAS", precio_compra)
        articulos.append(cuaderno)



    for _ in range(2):
        tipo = "Lapiz"
        info = input("Especificacin del lapiz (Grafito o Colores): ")
        precio_compra = float(input("precio de compra del lapiz: "))
        print("*" * 25)
        lapiz= Item(tipo, f"{info} MARCA RAYAS", precio_compra)
        articulos.append(lapiz)

    return articulos

def mostrar_articulos(articulos):
    for articulo in articulos:
        articulo.mostrar_datos()
        print("*" * 25)


articulos = registrar_datos()
mostrar_articulos(articulos)