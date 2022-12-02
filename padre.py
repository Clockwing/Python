class persona:
    nombre   = str
    apellido = str
    
    def __int__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(self.nombre, self.apellido)
        
x=persona("Alexander", "Flores")
x.imprimir()

class estudiante(persona):
    pass

y = estudiante("jose", "Cañar")
y.imprimir()

class student(persona):
    edad =int
    def __init__(self, nombre, apellido, edad):
     persona.__init__(self, nombre, apellido,edad)
     self.edad = edad
estudiante1= student("carlos", "Deli", 24)
estudiante.imprimir()

#Agregar medotos a una herencia

class student1(persona):
       edad = int
       semestre = str
       def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(self, nombre, apellido,edad, semestre)
        self.edad = edad
        self.semestre = semestre
       def bienvenido(self):
           print("bienvenido " + self.apellido +"al " + self.semestre + " ingrese a los "+ str(self.edad)) 
p5= student1("Diego", "Yanez", 29, "semstre")
p5.bienvenido()

