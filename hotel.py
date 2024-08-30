class Hotel:
    def __init__(self):
        self.habitaciones = {
            'Sencilla': 100,
            'Doble': 150,
            'Suite': 250
        }
        self.servicios_extra = {
            'Piscina': 20,
            'Golf': 50
        }
    
    #Creamoas funciones para utilizar los metodos y todo lo que queremos registrar
    def mostrar_opciones(self):
        print("--- Hotel Tropico Inn ---")
        print("Habitaciones disponibles:")
        for tipo, precio in self.habitaciones.items():
            print(f"{tipo}: ${precio} por noche")

        print("\nServicios extra disponibles:")
        for servicio, precio in self.servicios_extra.items():
            print(f"{servicio}: ${precio}")

    def solicitar_datos_cliente(self):
        nombre = input("\nIngrese el nombre del cliente: ")
        noches = int(input("Ingrese el número de noches que permanecerá: "))
        return nombre, noches

    def seleccionar_habitacion(self):
        while True:
            tipo_habitacion = input("Seleccione el tipo de habitación (Sencilla/Doble/Suite): ")
            if tipo_habitacion in self.habitaciones:
                return tipo_habitacion
            else:
                print("Opción no válida. Intente nuevamente.")

    def seleccionar_servicios_extra(self):
        servicios_seleccionados = []
        while True:
            servicio = input("Seleccione un servicio extra (Piscina/Golf) o 'n' para finalizar: ")
            if servicio == 'n':
                break
            elif servicio in self.servicios_extra:
                servicios_seleccionados.append(servicio)
            else:
                print("Opción no válida. Intente nuevamente.")
        return servicios_seleccionados

    def calcular_total(self, tipo_habitacion, noches, servicios_seleccionados):
        total_habitacion = self.habitaciones[tipo_habitacion] * noches
        total_servicios = sum([self.servicios_extra[servicio] for servicio in servicios_seleccionados])
        return total_habitacion + total_servicios
    

    #aqui generamos el ticket final
    def generar_factura(self, nombre, tipo_habitacion, noches, servicios_seleccionados, total):
        print("\n***Hotel Tropico Inn***")
        print("--- Factura Detallada ---")
        print(f"Cliente: {nombre}")
        print(f"Habitación: {tipo_habitacion}")
        print(f"Noches: {noches}")
        print(f"Total habitación: ${self.habitaciones[tipo_habitacion] * noches}")
        if servicios_seleccionados:
            print("Servicios extra:")
            for servicio in servicios_seleccionados:
                print(f"{servicio}: ${self.servicios_extra[servicio]}")
        else:
            print("No se seleccionaron servicios extra.")
        print(f"Total a pagar: ${total}")
        print("-" * 30)

#aqui este main utiliza todos los metodos que fueron definidos en la clase 
def main():
    hotel = Hotel()
    hotel.mostrar_opciones()
    
    nombre, noches = hotel.solicitar_datos_cliente()
    tipo_habitacion = hotel.seleccionar_habitacion()
    servicios_seleccionados = hotel.seleccionar_servicios_extra()
    
    total = hotel.calcular_total(tipo_habitacion, noches, servicios_seleccionados)
    hotel.generar_factura(nombre, tipo_habitacion, noches, servicios_seleccionados, total)

if __name__ == "__main__":
    main()