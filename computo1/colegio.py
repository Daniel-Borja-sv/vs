from datetime import datetime
#importamos una libreria que sirve para usar los meses, años, dia, hora.

#en este codigo utilizaremos 2 clases

# Creamos una clase
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_asistencia = []

    def registrar_asistencia(self, estado, fecha, razon_permiso = None):
        if estado.lower() == 'permiso' and not razon_permiso:
            print("Debe proporcionar una razón para el permiso.")
            return
        self.registro_asistencia.append({
            'estado': estado,
            'fecha': fecha,
            'razon_permiso': razon_permiso
        })

    def mostrar_registro_asistencia(self):
        print(f"Registro de asistencia de {self.nombre}:")
        for registro in self.registro_asistencia:
            estado = registro['estado']
            fecha = registro['fecha']
            razon = registro['razon_permiso']
            if estado.lower() == 'permiso':
                print(f"Fecha: {fecha}, Estado: {estado}, Razón: {razon}\n")
            else:
                print(f"Fecha: {fecha}, Estado: {estado}\n")

# Clase para representar a un docente con una lista de estudiantes
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def registrar_asistencia_estudiante(self, nombre_estudiante, estado, fecha, razon_permiso=None):
        estudiante = next((e for e in self.estudiantes if e.nombre == nombre_estudiante), None)
        if estudiante:
            estudiante.registrar_asistencia(estado, fecha, razon_permiso)
        else:
            print(f"Estudiante {nombre_estudiante} no encontrado.")

    def mostrar_registros(self):
        print("-" * 30)
        print(f"Registros de asistencia del docente {self.nombre}:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_registro_asistencia()

# Ejemplo de uso
docente = Docente("Ing William")

# Agregar estudiantes
estudiante1 = Estudiante("Borja")
estudiante2 = Estudiante("Cristian")
estudiante3 = Estudiante("Juni")
estudiante4 = Estudiante("Enrique")


docente.agregar_estudiante(estudiante1)
docente.agregar_estudiante(estudiante2)
docente.agregar_estudiante(estudiante3)
docente.agregar_estudiante(estudiante4)


# Registrar asistencia
fecha_hoy = datetime.now().strftime("%Y-%m-%d")
docente.registrar_asistencia_estudiante("Borja", "Asistencia", fecha_hoy)
docente.registrar_asistencia_estudiante("Cristian", "Permiso", fecha_hoy, "Cita médica")
docente.registrar_asistencia_estudiante("Juni", "Permiso", fecha_hoy, "Problemas Personales")
docente.registrar_asistencia_estudiante("Enrique", "Asistencia", fecha_hoy)
docente.registrar_asistencia_estudiante("Miguel", "Asistencia", fecha_hoy)#este estudiante no esta registrado en la lista suponiendo que ya no pertenece a la institucion

# Mostrar registros
docente.mostrar_registros()