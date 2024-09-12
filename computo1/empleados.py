class Empleado:
    def __init__(self, nombre, anios_laborados):
        self.nombre = nombre
        self.anios_laborados = anios_laborados

    def calcular_pago(self):
        pass

    def calcular_bono(self):
        if self.anios_laborados > 5:
            return 1000  # Bono adicional si ha laborado más de 5 años
        return 0


class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anios_laborados, salario_base, comisiones):
        super().__init__(nombre, anios_laborados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_pago(self):
        pago = self.salario_base + self.comisiones + self.calcular_bono()
        return pago


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anios_laborados, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, anios_laborados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self):
        pago = self.horas_trabajadas * self.tarifa_hora + self.calcular_bono()
        return pago


# Ejemplo de uso
empleado1 = EmpleadoPlazaFija("Daniel Borja", 10, 1000, 300) #aqui lleva el bono de mas de 5 años trabajando
empleado2 = EmpleadoPorHoras("Kevin Diaz", 3, 40, 13.50)
empleado3 = EmpleadoPorHoras("William Giron", 1, 50, 20)
empleado4 = EmpleadoPlazaFija("Diego Marino", 4, 500, 400)

print("Empleado 1 (plaza fija)")
print(f"Pago a {empleado1.nombre}: ${empleado1.calcular_pago()} ya con Abono por mas de 5 años ")

print("\nEmpleado 2 (Por horas)")
print(f"Pago a {empleado2.nombre}: ${empleado2.calcular_pago()}")

print("\nEmpleado 3 (por horas)")
print(f"Pago a {empleado3.nombre}: ${empleado3.calcular_pago()}")

print("\nEmpleado 4 (plaza fija)")
print(f"Pago a {empleado3.nombre}: ${empleado3.calcular_pago()}")