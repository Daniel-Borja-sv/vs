class carro():
    """""
    def datos(self, color, modelos, crines, tmotor, transmision):
        self.color = color
        self.modelo = modelos
        self.crines = crines
        self.tmoto = tmotor
        self.transmision = transmision
        """""

    
    def __init__(self, color, modelo, crines, tmotor, transmision):
        self.color = color
        self.modelo = modelo
        self.crines = crines
        self.tmoto = tmotor
        self.transmision = transmision
        
    def mostrard(self):
        print("***Datos del carro***\n"+
              f"color:  {self.color}\n"+
              f"Modelo:  {self.modelo}\n"+
              f"crines:  {self.crines}\n"+
              f"Tipo de motor:  {self.tmotor}\n"+
              f"transmision:  {self.transmision}\n")
        

    def encender(self):
        if(self.transmision == "Manual"):
            print("se ha introducido la llave")
            while True:
                estado = input("¿La palanca esta en neutro? (s/n)")
                if(estado == "s"):
                    print("se ha girado la llave")
                    print("el motor se ha encendido")
                    break
                else:
                    print("el motor no enciende")
                    continue
         

    def enmarcha(self):
        if(self.transmision == "Manual"):
            print("Se mantiene el clutch")
            print("Se cambia a primera velocidad")
            print("se va soltando el clutch despacio")
            estado  = input("¿se ha soltado el clutch correctamente? (s/n)")
            if(estado == "s"):
                print("se utiliza el acelerador")
                print("el carro se ha puesto es marcha")
            else:
                print("el carro se apago")
                self.encender()
        


    def retroceder(self):
        if(self.transmision == "Manual"):
            pass
        else:
            pass