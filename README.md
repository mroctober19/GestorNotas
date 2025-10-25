
# Gestor de Notas Académicas

Redacción del problema: El Gestor de Notas Académicas es un sistema en consola diseñado para que estudiantes de cualquier nivel puedan registrar, organizar y analizar sus calificaciones de forma sencilla y eficiente. El objetivo principal del gestor es proporcionar una herramienta clara y sin distracciones o interfaces confusas que permita al estudiante visualizar su rendimiento académico en cualquier momento.

El aspecto que diferencia al gestor de métodos manuales como el lápiz y papel, o de soluciones más complejas como hojas de cálculo, es que este sistema no requiere conocimientos técnicos ni configuraciones previas, tampoco la descarga de programas pesados. Todo funciona desde un menú interactivo, funcionando totalmente en un entorno ligero que no necesita internet ni programas externos lo cual puede ser de gran utilidad y valor para quienes no lo tengan disponibles.

El gestor cubre necesidades clave como el registro ordenado de asignaturas, el cálculo de promedios, el conteo de cursos aprobados y reprobados, y la búsqueda y ordenamiento de información lo que le facilita al estudiante la toma de decisiones en cuanto a su desempeño académico. Esto permite que el estudiante dedique menos tiempo a organizar sus notas y pueda enfocarse de mejor manera en aumentar su desempeño dentro de las aulas.

---

# Requisitos del sistema

### FUNCIONALES:

1. Registro de cursos y calificaciones: El sistema permitirá ingresar el nombre de un curso junto con la calificación obtenida, validando que la nota esté en el rango de 0 a 100.

2. Visualización de notas registradas: El sistema mostrará la lista de cursos y sus calificaciones, o un mensaje de aviso si no hay datos registrados.

3. Cálculo del promedio general: El sistema calculará el promedio de todas las calificaciones y lo mostrará redondeado a dos decimales.

4. Conteo de cursos aprobados y reprobados: El sistema indicará cuántos cursos están aprobados (nota ≥ 60) y cuántos reprobados.

5. Búsqueda de cursos: El sistema permitirá buscar cursos por nombre por medio de coincidencias parciales, sin importar mayúsculas o minúsculas.

---

### NO FUNCIONALES:

1. Ejecución en consola: El programa está diseñado para ejecutarse en la consola o terminal, no necesita de una interfaz gráfica, este detalles lo hace ligero y mas eficiente.

2. Lenguaje de programación: Se utilizará Python como lenguaje de programación, ya que permite escribir código de forma clara y concisa.

3. Restricciones: Para mantener la sencillez, no se usarán librerías externas. Todo el código se desarrollará con las funcionalidades que ya vienen incluidas en Python.

4. Uso de estructuras de control: El flujo del sistema se controlará mediante bucles y condicionales. Esto permite crear una secuencia de acciones y tomar decisiones de acuerdo con las interacciones del usuario.

5. Estructura del código fuente: El código se organizará en funciones modulares. Cada función se encargará de una tarea específica, como por ejemplo registrar un curso o calcular un promedio, lo que facilita la lectura y el mantenimiento del mismo.

6. Validación de datos: Se implementarán validaciones de datos para asegurar que la información que ingresa el usuario sea correcta y evitar errores inesperados en el programa.

### ACTUALIZACIONES POR AVANCE

## AVANCE 1

Al repositorio se cargaron incialmente la descripcion README.md donde se encuentran detalladamente la redaccion del problema, el publico objetivo del proyecto y las necesidades clave que cubre. De igual manera requisitos funcionales y no funcionales para que el usuario pueda entender de la mejor manera en que consiste la logica y la funcionalidad del sistema gestor de notas. 

De igual manera en el avance 01 se presentó el primer pseudocodigo inicial para el menú del programa, implementando almenos 5 opciones distintas.

## AVANCE 2

Durante este avance 02 se siguió usando la logica del pseudocodigo, implementando oficialmente las primeras opciones del gestor de notas plasmadas en el menu que se realizó en el primer avance (ingreso de curos y notas, calculo de promedio y mostrar cursos)

## AVANCE 3

Para el avance 3 se llevó del pseudocodigo al codigo, por medio del lenguaje python. Se desarrollaron en este avance 3 opciones mas siendo el conteo de cursos aprobados y reprobados, búsqueda lineal de cursos por nombre, y actualización de notas existentes para los cursos. Esto permite que los datos se sigan almacenando en las listas son curso y nota y no pierda la estructura

## AVANCE 4

En este avance se implementaron nuevamente 3 opciones, siendo eliminación segura de registros con confirmación del usuario, y dos métodos de ordenamiento (por nota y por nombre) utilizando el algoritmo built-in sorted con funciones lambda como key. Con lo cual se incrementa el total de operaciones disponibles para los usuarios a 9 

## AVANCE 5
Durante este avance se completaron las últimas funcionalidades del sistema, alcanzando un total de once opciones dentro del menú principal.
Se añadieron las características de cola de revisión (para simular solicitudes de revisión de cursos mediante una estructura FIFO) y el historial de cambios (implementado como una pila LIFO que registra las actualizaciones y eliminaciones realizadas)

## AVANCE 6 
En este último avance, el código fue pulido, documentado y estructurado en su versión final.
Se añadieron comentarios explicativos en cada función, se mejoró la legibilidad general

El proyecto quedó totalmente funcional y estable, con todas las operaciones del menú probadas y verificadas.
Asimismo, se elaboró la documentación técnica y el manual de usuario, consolidando el desarrollo como un sistema completo que integra buenas prácticas de programación, modularidad y claridad en el diseño.

# Reflexión
## ¿Qué aprendí con este proyecto?

Con este proyecto aprendí la importancia de la modularidad en la programación. Dividir el código en funciones independientes no solo facilita la lectura y el mantenimiento, sino que también mejora la organización y la posibilidad de reutilizar partes del código en el futuro. Aunque en este caso algunas funciones, como el cálculo del promedio, se utilizaron una sola vez, aplicar este principio desde el inicio me ayudó a estructurar el sistema de forma más clara y profesional. Además, comprendí mejor cómo aplicar estructuras de datos como listas, pilas y colas en un contexto real y funcional.

## ¿Qué fue lo más desafiante de resolver?

Lo más desafiante fue implementar el historial de cambios y la cola de revisión. Estas funciones requerían comprender bien el comportamiento de las estructuras LIFO (pila) y FIFO (cola), lo que implicó investigar y practicar hasta encontrar una forma eficiente de aplicarlas. Tuve que apoyarme en videos de YouTube y foros como Reddit para entender cómo simular estos comportamientos y lograr que funcionaran correctamente dentro del flujo del programa además de las presentaciones y actividades semanales que dentro de la clase se veían, sin embargo el historial si se me complicó al inicio

## ¿Qué mejoraría si tuviera más tiempo?

Si tuviera más tiempo, mejoraría el formato general del código y del menú. Puliría los textos, títulos y mensajes que se muestran al usuario para hacerlos más claros y consistentes. También intentaría prever más escenarios y posibles errores que podrían ocurrir con ciertos tipos de entrada del usuario. Finalmente, me gustaría experimentar con una versión mejorada del sistema que incluya una interfaz gráfica simple, para hacerlo más visual y amigable sin perder la simplicidad que lo caracteriza.









