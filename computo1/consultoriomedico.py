class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.cita_asignada = None

class ConsultorioMedico:
    def __init__(self):
        self.pacientes = []
        self.sala_de_espera = []

    def registrar_paciente(self, nombre, motivo_consulta):
        paciente_existente = self.buscar_paciente(nombre)
        
        if paciente_existente:
            print(f"{nombre} ya tiene una cita asignada.")
            self.sala_de_espera.append(paciente_existente)
        else:
            nuevo_paciente = Paciente(nombre, motivo_consulta)
            self.pacientes.append(nuevo_paciente)
            self.asignar_cita(nuevo_paciente)
            print(f"Se ha registrado a {nombre} para la consulta: '{motivo_consulta}'.")

    def buscar_paciente(self, nombre):
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                return paciente
        return None

    def asignar_cita(self, paciente):
        # Aquí se podría implementar lógica más compleja para asignar la fecha
        paciente.cita_asignada = "Fecha asignada: 2024-09-01"
        print(f"Cita asignada a {paciente.nombre} en la fecha: {paciente.cita_asignada}")

    def listar_pacientes(self):
        print("Lista de pacientes con cita:")
        for paciente in self.pacientes:
            print(f"Nombre: {paciente.nombre}, Motivo: {paciente.motivo_consulta}, Cita: {paciente.cita_asignada}")

    def listar_sala_de_espera(self):
        print("Pacientes en la sala de espera:")
        for paciente in self.sala_de_espera:
            print(f"Nombre: {paciente.nombre}, Motivo: {paciente.motivo_consulta}")

# Uso del programa
consultorio = ConsultorioMedico()
consultorio.registrar_paciente("Juan Pérez", "Consulta general")
consultorio.registrar_paciente("María López", "Revisión médica")
consultorio.registrar_paciente("Juan Pérez", "Consulta general")  # Este ya tiene cita
consultorio.listar_pacientes()
consultorio.listar_sala_de_espera()