class Inscripcion:
    def __init__(self, fecha, nombre_alumno, materia, profesor, curso, division, nota=-1):
        self.fecha = fecha
        self.nombre_alumno = nombre_alumno
        self.materia = materia
        self.profesor = profesor
        self.curso = curso
        self.division = division
        self.nota = nota

    def modificar_datos(self, nueva_fecha=None, nuevo_nombre=None, nueva_materia=None, 
                        nuevo_profesor=None, nuevo_curso=None, nueva_division=None):
        if nueva_fecha: self.fecha = nueva_fecha
        if nuevo_nombre: self.nombre_alumno = nuevo_nombre
        if nueva_materia: self.materia = nueva_materia
        if nuevo_profesor: self.profesor = nuevo_profesor
        if nuevo_curso: self.curso = nuevo_curso
        if nueva_division: self.division = nueva_division

    def cargar_nota(self, nota):
        self.nota = nota