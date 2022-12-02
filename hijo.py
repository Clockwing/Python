from padre import persona

class Docente(persona):
    titulo                 = str
    edad                   = int
    experienciaprofecional = int
    experienciaDocente     = int
    
    def __int__(self, nombre, apellido, titulo, edad, experienciaprofecional, experienciaDocente ):
     super().__int__(nombre, apellido)
     self.titulo =titulo
     self.edad =edad
     self.experienciaDocente =experienciaDocente
     self.experienciaprofecional =experienciaprofecional
    
    def BienvenidoDocente(self):
     print("estimado Docente: " + self.nombre, self.apellido + " le damos la bienvenida al intituto yavirac " + " agradecemos contar con sus " + str(self.experienciaprofecional, self.experienciaDocente) + " Años de experiencia")
    
     docente1 = Docente("Dayana", "Tafur", "Desarrollador de software", 24, 2, 1)
     docente1.BienvenidoDocente()
    