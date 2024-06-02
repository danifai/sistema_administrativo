from personas import Encargado, Profesor
from inscripciones import Inscripcion

class Gestor:
    @staticmethod
    def leer_archivo(archivo, Clase, campos):
        elementos = []
        with open(archivo) as f:
            for linea in f:
                datos = linea.strip().split(",")
                elemento = Clase(*[datos[campos.index(campo)] for campo in Clase.__init__.__code__.co_varnames[1:]])
                elementos.append(elemento)
        return elementos

    @staticmethod
    def escribir_en_archivo(archivo, elementos):
        with open(archivo, "w") as f:
            for elemento in elementos:
                f.write(",".join(str(v) for v in vars(elemento).values()) + "\n")

class GestorEncargados(Gestor):
    def __init__(self, archivo="Encargados.txt"):
        self.encargados = self.leer_archivo(archivo, Encargado, ["nombre", "dni"])

class GestorProfesores(Gestor):
    def __init__(self, archivo="Profesores.txt"):
        self.profesores = self.leer_archivo(archivo, Profesor, ["nombre", "materia", "curso", "division"])

class GestorInscripciones(Gestor):
    def __init__(self, archivo="Inscripciones.txt"):
        self.inscripciones = self.leer_archivo(archivo, Inscripcion, ["fecha", "nombre_alumno", "materia", "profesor", "curso", "division", "nota"])
