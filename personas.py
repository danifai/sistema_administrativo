class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Encargado(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre)
        self.dni = dni

class Profesor(Persona):
    def __init__(self, nombre, materia, curso, division):
        super().__init__(nombre)
        self.materia = materia
        self.curso = curso
        self.division = division
