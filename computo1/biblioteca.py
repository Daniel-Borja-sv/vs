from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, dias_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_prestamo + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None

    def devolver_libro(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
        if self.fecha_devolucion > self.fecha_limite:
            dias_retraso = (self.fecha_devolucion - self.fecha_limite).days
            print(f"El libro '{self.libro}' ha sido devuelto con un retraso de {dias_retraso} días. Se aplicará una sanción.")
        else:
            print(f"El libro '{self.libro}' ha sido devuelto a tiempo. No se aplicará ninguna sanción.")

    def mostrar_info_prestamo(self):
        print(f"Usuario: {self.usuario}")
        print(f"Libro: {self.libro}")
        print(f"Fecha de Préstamo: {self.fecha_prestamo.strftime('%d/%m/%Y')}")
        print(f"Fecha Límite de Devolución: {self.fecha_limite.strftime('%d/%m/%Y')}")
        if self.fecha_devolucion:
            print(f"Fecha de Devolución: {self.fecha_devolucion.strftime('%d/%m/%Y')}")
        else:
            print("El libro aún no ha sido devuelto.")


# Ejemplo de uso
fecha_prestamo = datetime(2024, 8, 30)
prestamo1 = Prestamo("Juan Pérez", "El Quijote", fecha_prestamo, 15)

prestamo1.mostrar_info_prestamo()

# Devolución del libro (con retraso)
fecha_devolucion = datetime(2024, 9, 20)
prestamo1.devolver_libro(fecha_devolucion)
prestamo1.mostrar_info_prestamo()

# Devolución del libro (a tiempo)
prestamo2 = Prestamo("María López", "Cien Años de Soledad", fecha_prestamo, 15)
prestamo2.mostrar_info_prestamo()
fecha_devolucion2 = datetime(2024, 9, 10)
prestamo2.devolver_libro(fecha_devolucion2)
prestamo2.mostrar_info_prestamo()