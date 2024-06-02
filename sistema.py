from personas import Encargado, Profesor
from inscripciones import Inscripcion
from gestores import GestorEncargados, GestorProfesores, GestorInscripciones

class Sistema:
    def __init__(self):
        self.gestor_encargados = GestorEncargados()
        self.gestor_profesores = GestorProfesores()
        self.gestor_inscripciones = GestorInscripciones()
        self.inscripciones_archivo = "Inscripciones.txt"
        self.profesor_actual = None

    def acceso(self, individuo, grupo):
        return individuo in [vars(persona) for persona in grupo]

    def mostrar_menu_principal(self):
        print("\nBienvenido al sistema de inscripciones")
        print("1. Acceso Encargado")
        print("2. Acceso Profesor")
        print("0. Salir del sistema")
        return int(input("Ingrese la opción deseada: "))

    def mostrar_menu_encargado(self):
        print("\n1. Inscribir alumno")
        print("2. Modificar alumno")
        print("3. Eliminar alumno")
        print("0. Salir")
        return int(input("Seleccione una opción: "))

    def mostrar_menu_profesor(self):
        print("\n1. Cargar nota")
        print("0. Salir")
        return int(input("Seleccione una opción: "))

    def inscribir_alumno(self):
        fecha = input("Fecha: ")
        nombre_alumno = input("Nombre del alumno: ")
        materia = input("Materia: ")
        profesor = input("Nombre del profesor: ")
        curso = input("Curso: ")
        division = input("División: ")
        nota = -1
        nueva_inscripcion = f"{fecha},{nombre_alumno},{materia},{profesor},{curso},{division},{nota}\n"
        
        with open(self.inscripciones_archivo, "a") as f:
            f.write(nueva_inscripcion)
        
        print("Alumno inscrito exitosamente")

    def modificar_datos(self):
        while True:
            nombre_alumno = input("Ingrese el nombre del alumno a modificar (0 para salir): ")
            if nombre_alumno == "0":
                break
            
            with open(self.inscripciones_archivo, "r+") as f:
                lineas = f.readlines()
                f.seek(0)
                alumno_encontrado = False

                for i, linea in enumerate(lineas):
                    campos = linea.strip().split(",")
                    if campos[1] == nombre_alumno:
                        alumno_encontrado = True
                        print(f"Alumno encontrado: {linea}")
                        nueva_fecha = input("Nueva fecha (deje en blanco para no modificar): ")
                        nuevo_nombre = input("Nuevo nombre (deje en blanco para no modificar): ")
                        nueva_materia = input("Nueva materia (deje en blanco para no modificar): ")
                        nuevo_profesor = input("Nuevo profesor (deje en blanco para no modificar): ")
                        nuevo_curso = input("Nuevo curso (deje en blanco para no modificar): ")
                        nueva_division = input("Nueva división (deje en blanco para no modificar): ")

                        if nueva_fecha:
                            campos[0] = nueva_fecha
                        if nuevo_nombre:
                            campos[1] = nuevo_nombre
                        if nueva_materia:
                            campos[2] = nueva_materia
                        if nuevo_profesor:
                            campos[3] = nuevo_profesor
                        if nuevo_curso:
                            campos[4] = nuevo_curso
                        if nueva_division:
                            campos[5] = nueva_division

                        lineas[i] = ",".join(campos) + "\n"

                f.seek(0)
                f.writelines(lineas)
                f.truncate()

                if alumno_encontrado:
                    print("Datos modificados exitosamente")
                else:
                    print("No se encontró al alumno con ese nombre")

    def eliminar_alumno(self):
        while True:
            volver_al_menu = False
            nombre_alumno = input("Ingrese el nombre del alumno a eliminar (0 para salir): ")
            if nombre_alumno == "0":
                break
            
            materia_alumno = input("Ingrese la materia del alumno: ")

            with open(self.inscripciones_archivo, "r+") as f:
                lineas = f.readlines()
                f.seek(0)
                alumno_encontrado = False

                for i, linea in enumerate(lineas):
                    campos = linea.strip().split(",")
                    if campos[1] == nombre_alumno and campos[2] == materia_alumno:
                        alumno_encontrado = True
                        print(f"Alumno encontrado: {linea}")
                        eliminar = input("¿Desea eliminar este alumno? (s/n): ").lower()
                        if eliminar == "s":
                            del lineas[i]
                            print("Alumno eliminado exitosamente")
                            volver_al_menu = True
                        break

                f.seek(0)
                f.writelines(lineas)
                f.truncate()

                if not alumno_encontrado:
                    print("No se encontró al alumno con ese nombre y materia")
                    volver_al_menu = True

            if volver_al_menu:
                self.mostrar_menu_encargado()

    def cargar_nota(self):
        if self.profesor_actual is not None:
            nombre_materia_profesor = f"{self.profesor_actual.materia},{self.profesor_actual.curso},{self.profesor_actual.division}"
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            
            with open(self.inscripciones_archivo, "r+") as f:
                lineas = f.readlines()
                f.seek(0)  # Volver al inicio del archivo
                alumno_encontrado = False
                
                for i, linea in enumerate(lineas):
                    campos = linea.strip().split(",")
                    if campos[1] == nombre_alumno and campos[3] == self.profesor_actual.nombre:
                        alumno_encontrado = True
                        materia = campos[2]
                        nota = int(input(f"Ingrese la nota para {campos[1]} en {materia}: "))
                        campos[-1] = str(nota)
                        lineas[i] = ",".join(campos) + "\n"
                
                f.seek(0)  # Volver al inicio del archivo
                f.writelines(lineas)  # Escribir las líneas actualizadas
                f.truncate()  # Eliminar contenido restante si es necesario
                
                if alumno_encontrado:
                    print("Notas cargadas exitosamente")
                else:
                    print("No se encontró al alumno con ese nombre")

        else:
            print("Debe iniciar sesión como profesor primero")

    def ejecutar(self):
        op = -1
        while op != 0:
            try:
                op = self.mostrar_menu_principal()
                if op == 1:  # Acceso Encargado
                    nombre_enc = input("Nombre del encargado: ")
                    dni_enc = input("DNI del encargado: ")
                    encargado = Encargado(nombre_enc, dni_enc)
                    if self.acceso(vars(encargado), self.gestor_encargados.encargados):
                        print("Acceso concedido a encargado.")
                        while (opcion := self.mostrar_menu_encargado()) != 0:
                            if opcion == 1:
                                self.inscribir_alumno()
                            elif opcion == 2:
                                self.modificar_datos_alumno()
                            elif opcion == 3:
                                self.eliminar_alumno()
                    else:
                        print("Acceso denegado. Por favor ingrese datos válidos.")
                elif op == 2:  # Acceso Profesor
                    nombre_prof = input("Nombre del profesor: ")
                    materia_prof = input("Materia del profesor: ")
                    curso_prof = input("Curso del profesor: ")
                    division_prof = input("División del profesor: ")
                    profesor = Profesor(nombre_prof, materia_prof, curso_prof, division_prof)
                    if self.acceso(vars(profesor), self.gestor_profesores.profesores):
                        print("Acceso concedido a profesor.")
                        self.profesor_actual = profesor
                        while (opcion := self.mostrar_menu_profesor()) != 0:
                            if opcion == 1:
                                self.cargar_nota()
                    else:
                        print("Acceso denegado. Por favor ingrese datos válidos.")
                elif op != 0:
                    print("Opción no válida.")

            except ValueError:
                print("Por favor ingrese una opción válida (número entero)")