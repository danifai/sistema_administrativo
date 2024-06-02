## Aclaraciones sobre el sistema

El sistema fue desarrollado con Python en una pc con Linux como sistema operativo, utilizando Visual Studio.

Todos los archivos están a un mismo nivel de carpeta. Se debe descomprimir el zip, entrar a la carpeta y ejecutar el archivo "main.py".
Al ejecutarlo, habrá un menú de acceso para encargado o profesor.
Acompañan archivos .txt a modo de "base de datos" para usar con el sistema, los respectivos módulos con los objetos,
y un archivo "sistema.py" con las principales funcionalidades.

En cuanto al diseño del sistema, validación try-except para el menú general de acceso, para que el sistema no rompa al ingresar 
un caracter distinto a número entero. En el caso del encargado, al validar el ingreso puede cargar un alumno, modificar un alumno,
o eliminarlo. A la hora de cargar al alumno, deja un "enter" para que haya una línea vacía al final para poder cargar al siguiente.
En el caso del profesor, solamente carga notas, buscando por alumno coincidente con la materia que dicta, por lo que no puede 
escribir nota de alumnos que no sean suyos.
