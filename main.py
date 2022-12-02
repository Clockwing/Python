class persona:
    nombre = str
    edad = int
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        def saluda (self, otra_persona):
            return f'Hola {otra_persona.nombre}, me llamo'
        if __name__== "__main__":
            Persona1 = persona("Diegp", 33)
            Persona2 = persona("carla", 35)
            print (Persona1.saluda(Persona2))
            
    class MiClase:
        nombre = "Diego"
        edad = 21
        
    p1 = MiClase()
    print(p1.nombre)
    
    class persona2:
        nombre = str
        edad = int
        genero = str
        
        def __init__(self, nombre, edad, genero):
            self.nombre = nombre
            self.edad = edad
            self.genero = genero
    p2 = persona2("Diego", 29, "MAsculino")         
    
    print(p2.nombre)
    print(p2.edad)
    print(p2.genero)
    
    #la funcion _str_()
    class persona3:
        nombre   = str
        edad     = int
        genero   = str
        estatura = int
        def __init__(self, nombre, edad, genero, estatura):
            self.nombre   = nombre
            self.edad     = edad
            self.genero   = genero
            self.estatura = estatura
        def __str__(self):
            return f'Hola me llamo{self.nombre}, tengo {self.edad}'
        p3 = persona3("Juan",21,"masculino", 189)
        print(p3)
        
    #Metodos dentro de objetos
    

class persona4:
    nombre = str
    semestre = str
    def __init__(self, nombre, semestre):
        self.nombre = nombre
        self.semestre = semestre
        def saludo(self):
        print("Bienvenido " + self.nombre + "al " +self.semestre)
        p4 = persona4("Antonio", "semestre")
        p4.saludo()
        p4.nombre ="Jonathan"
        p4.saludo()
        del p4
        p4.saludo()
            
            
        
        
        
        
        
        
        
        