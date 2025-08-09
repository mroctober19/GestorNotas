\# Título del proyecto

Gestor de Notas Académicas



Redacción del problema: El Gestor de Notas Académicas es un sistema en consola diseñado para que estudiantes de cualquier nivel puedan registrar, organizar y analizar sus calificaciones de forma sencilla y eficiente. El objetivo principal del gestor es proporcionar una herramienta clara y sin distracciones o interfaces confusas que permita al estudiante visualizar su rendimiento académico en cualquier momento.



El aspecto que diferencia al gestor de métodos manuales como el lápiz y papel, o de soluciones más complejas como hojas de cálculo, es que este sistema no requiere conocimientos técnicos ni configuraciones previas, tampoco la descarga de programas pesados. Todo funciona desde un menú interactivo, funcionando totalmente en un entorno ligero que no necesita internet ni programas externos lo cual puede ser de gran utilidad y valor para quienes no lo tengan disponibles.



El gestor cubre necesidades clave como el registro ordenado de asignaturas, el cálculo de promedios, el conteo de cursos aprobados y reprobados, y la búsqueda y ordenamiento de información lo que le facilita al estudiante la toma de decisiones en cuanto a su desempeño académico. Esto permite que el estudiante dedique menos tiempo a organizar sus notas y pueda enfocarse de mejor manera en aumentar su desempeño dentro de las aulas.



---



\## Requisitos del sistema



\### FUNCIONALES:



1. Registro de cursos y calificaciones: El sistema permitirá ingresar el nombre de un curso junto con la calificación obtenida, validando que la nota esté en el rango de 0 a 100.



2\. Visualización de notas registradas: El sistema mostrará la lista de cursos y sus calificaciones, o un mensaje de aviso si no hay datos registrados.



3\. Cálculo del promedio general: El sistema calculará el promedio de todas las calificaciones y lo mostrará redondeado a dos decimales.



4\. Conteo de cursos aprobados y reprobados: El sistema indicará cuántos cursos están aprobados (nota ≥ 60) y cuántos reprobados.



5\. Búsqueda de cursos: El sistema permitirá buscar cursos por nombre por medio de coincidencias parciales, sin importar mayúsculas o minúsculas.



---



\### NO FUNCIONALES:



1. Ejecución en consola: El programa está diseñado para ejecutarse en la consola o terminal, no necesita de una interfaz gráfica, este detalles lo hace ligero y mas eficiente.



2\. Lenguaje de programación: Se utilizará Python como lenguaje de programación, ya que permite escribir código de forma clara y concisa.



3\. Restricciones: Para mantener la sencillez, no se usarán librerías externas. Todo el código se desarrollará con las funcionalidades que ya vienen incluidas en Python.



4\. Uso de estructuras de control: El flujo del sistema se controlará mediante bucles y condicionales. Esto permite crear una secuencia de acciones y tomar decisiones de acuerdo con las interacciones del usuario.



5\. Estructura del código fuente: El código se organizará en funciones modulares. Cada función se encargará de una tarea específica, como por ejemplo registrar un curso o calcular un promedio, lo que facilita la lectura y el mantenimiento del mismo.



6\. Validación de datos: Se implementarán validaciones de datos para asegurar que la información que ingresa el usuario sea correcta y evitar errores inesperados en el programa.



