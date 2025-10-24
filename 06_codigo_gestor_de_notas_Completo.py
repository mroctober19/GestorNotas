"""

PROYECTO SEMESTRAL ALGORITMOS 2025 - GESTOR DE NOTAS ACADÉMICAS

Sistema para administrar cursos, calificaciones y calculos estadisticos basicos
Implementa funcionalidades de búsqueda, ordenamiento y control de cambios

"""

# TITULO DEL PROYECTO
def mostrarTitulo():
    print("* * * * * GESTOR DE NOTAS ACADÉMICAS * * * * *")
    print("MENÚ PRINCIPAL ")


# ESTRUCTURAS DE DATOS PRINCIPALES EN EL GESTOR DE NOTAS 
notas = [] # lista que contenga las parejas (curso, nota)
historial_pila = [] # pila (LIFO) para el resgistro de cambios realizador por el usuario


# OPCION NO.1 - REGISTRAR NUEVO CURSO 
# se registra un nuevo curso con su respectiva nota
def registrar_nuevo_curso():
    curso = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA REGISTRAR: ").strip().title()
    nota_str = input("INGRESE LA NOTA OBTENIDA PARA EL CURSO: ")
    # se verifica que sea un numero y se encuentre dentro del rango valido establecido
    while not nota_str.isdigit() or not (0 <= float(nota_str) <=100 ):
        print()
        print("NOTA FUERA DEL RANGO, POR FAVOR INTENTE CON UN VALOR ENTRE [0...100]")
        print()
        nota_str = input("INGRESE LA NOTA OBTENIDA PARA EL CURSO ")
        print()
    nota = float(nota_str)
    
    notas.append((curso, nota))
    print()
    print("CURSO Y NOTA INGRESADOS CORRECTAMENTE")
    print()
     
     
# OPCION NO.2 - MOSTRAR NOTAS Y CURSOS
# muestra todos los cursos y notas registrados en el sistema
def mostrar_cursosYnotas():
    if len(notas) == 0:
        print("NO EXISTEN CURSOS Y NOTAS INGRESADAS AL MOMENTO, POR FAVOR REGISTRE UNO NUEVO")
    else:
        print("CURSOS Y NOTAS REGISTRADAS: ")
        for curso, nota in notas:
            print()
            print(f"* CURSO: {curso} - NOTA: {nota}")
        print()


# OPCION NO.3 - CALCULO DE PROMEDIO
# calcula el promedio general con las notas ingresadas en el sistema
def promedio_de_notas():
    if len(notas) == 0:
        print("NO HAY DATOS REGISTRADOS, POR FAVOR INGRESE UN CURSO Y UNA NOTA")
        print()
        return 
    suma_notas = 0
    cantidad_notas = 0
    for curso, nota in notas:
        suma_notas += nota 
        cantidad_notas += 1
    promedio = suma_notas / cantidad_notas
    
    print()
    print(f"EL PROMEDIO ES DE: {promedio:.2f}")
    print()
    

# OPCION NO.4 - CONTAR APROBADOS Y REPROBADOS 
# cuenta y muestra cuantos cursos ha aprobado el estudiante (>=60) y cuantos ha reprobado (<60)
def contar_aprobadosYreprobados():
    aprobados = 0
    reprobados = 0
    for _, nota in notas: # el _, significa que no se tomara en cuenta el nombre del curso, sino solo la nota
        if nota >= 60:
            aprobados += 1
        else:
            reprobados += 1
    print()        
    print(f"EL TOTAL DE CURSOS APROBADOS ES DE: {aprobados}")
    print(f"EL TOTAL DE CURSOS REPROBADOS ES DE: {reprobados}")
    print()
    

# OPCION NO.5 - BUSCAR CURSO 
# busca un curso dentro del sistema por nombre
def buscar_curso():
    curso_buscado = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA BUSCAR ")
    encontrado = False 
    for curso, nota in notas:
        if curso.lower() == curso_buscado.lower():
            print()
            print(f"CURSO ENCONTRADO: CURSO: {curso} - NOTA: {nota}")
            print()
            encontrado = True
            break
    if not encontrado:
        print()
        print("CURSO NO ENCONTRADO, POR FAVOR INTENTE NUEVAMENTE")
        print()
        

# OPCION NO.6 - ACTUALIZAR NOTA DE CURSO
# actualiza la nota de un curso ya existente y ese cambio lo guarda en la pila de historial de cambios
def actualizar_nota():
    curso_buscado = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA ACTUALIZAR ").strip()
    
    for i in range(len(notas)):
        if notas[i][0].lower() == curso_buscado.lower():
            nota_anterior = notas[i][1] # Captura la nota anterior
            
            nota_nueva = input("INGRESE LA NUEVA NOTA DEL CURSO ")
            while not nota_nueva.isdigit() or not (0 <= float(nota_nueva) <=100):
                nota_nueva = input("NOTA FUERA DE RANGO, INTENTE NUEVAMENTE")
                
            # se registra el cambio en el historial    
            historial_pila.append(f"ACTUALIZADO: '{notas[i][0]}' de {nota_anterior} a {nota_nueva}")
                
            # se crea una nueva lista con el nombre del curso y la nueva nota    
            notas[i] = (notas[i][0], int(nota_nueva))
            print()
            print("NOTA ACTUALIZADA CON EXITO")
            print()
            return
        
    print("CURSO NO ENCONTRADO, POR FAVOR INTENTE NUEVAMENTE")
    print()


# OPCION NO.7 - ELIMINAR CURSO
# elimina un curso ya existente de la lista luego de una confirmacion por el usuario
def eliminar_curso():
    curso_a_eliminar = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA ELIMINAR: ").strip()
    print()
    permiso = input("¿DESEA ELIMINAR EL CURSO PERMANENTEMENTE SI O NO? ").strip().upper()
    if permiso == "SI":
        for curso in notas:
            if curso[0].lower() == curso_a_eliminar.lower():
                
                # registra la eliminacion del curso dentro del historial
                historial_pila.append(f"ELIMINADO: '{curso[0]}' con nota {curso[1]}")
                
                notas.remove(curso)
                print()
                print("CURSO ELIMINADO CORRECTAMENTE")
                print()
                print("LA LISTA ACTUAL ES LA SIGUIENTE: ", notas)
                print()
                return
    elif permiso== "NO":
        print("SE CANCELÓ LA ACCIÓN ANTERIOR")  
        print()      
    print("ERROR:, EL CURSO YA FUE ELIMINADO O EL NOMBRE INGRESADO ES INCORRECTO, INTENTE NUEVAMENTE ")
    print()
print()
    
        
# OPCION NO.8 - ORDENAR POR NOTA    
# ordena los cursos de la lista segun el valor de las notas, de menor a mayor utilizando algoritmo de ordenamiento de burbuja
def ordenar_por_nota():
    n = len(notas)
    cambio = True
    # el bucle while continua mientras se resten realizando intercambios
    while cambio:
        cambio = False
        for i in range(n - 1):
            if notas[i][1] > notas[i + 1][1]:
                #se realiza el interbamcio entre notas
                notas[i], notas[i + 1] = notas[i + 1], notas[i]
                cambio = True
        n -=1
    print()
    print("Lista ordenada por notas: ", notas)
    print()  
    return notas

    
# OPCION NO.9 - ORDENAR POR NOMBRE
# ordena los cursos de la lista en base a su nombre utilizando el algoritmo de ordenamiento por insercion
def ordenar_por_nombre():
    n = len(notas)
    for i in range(1, n):
        clave = notas[i]
        j = i -1
        while j >= 0 and notas[j][0] > clave[0]:
            notas[j + 1] = notas[j]
            j = j -1
        notas[j + 1] = clave
    print()
    print("La lista ordenada por nombre: ", notas)
    print()
    
    
# OPCION NO.10 - COLA DE REVISION
# esta funcion simula una cola (FIFO) de solicitudes de revision de cursos
def cola_revision():

    cola_cursos = []
    # Bucle principal para recibir comandos del usuario
    while True:
        opcion = input("Escriba 'AGREGAR' para agregar un curso, 'REVISAR' para revisar el siguiente, o 'FIN' para salir: ").strip().upper()

        if opcion == "FIN":
            print("Se finaliza la revision!!!")
            break
        
        elif opcion == "AGREGAR":
            # Pide el nombre del curso y lo agrega al final de la cola
            curso_nuevo = input("INGRESE EL CURSO PARA REVISIÓN: ").strip().title()
            if curso_nuevo:
                cola_cursos.append(curso_nuevo)
                print("curso añadido a la cola de revision")
            else:
                print("debe ingresar un nombre valido")

        elif opcion == "REVISAR":
            if len(cola_cursos)>0:
                # saca de la cola el primer elemento de la cola 
                curso_a_revisar = cola_cursos.pop(0) 
                
                print("PROCESANDO SOLICITUDES...")
                print("Revisando: ", curso_a_revisar)
                print("Se Revisó: ", curso_a_revisar)
            else:
                print("No hay mas cursos para revisar")
        else:
            print("Opción Invalida. Use solamente 'AGREGAR', 'REVISAR' o 'FIN' ")
                
        # Muestra el estado actual de la cola después de cada acción ingresada por el usuario
        print("La cola Actual de Revision es: ", cola_cursos)
        print()
        
        
# OPCION NO.11 - HISTORIAL DE CAMBIOS
# muestra los cambios realizados por el usuario recientemente, se presenta de manera LIFO (mas reciente primero)
def historial():
    if not historial_pila:
        print("NO HAY CAMBIOS REGISTRADOS ACTUALMENTE DENTRO DEL GESTOR DE NOTAS")
        return

    print()
    print("* * * * HISTORIAL DE CAMBIOS (MÁS RECIENTE PRIMERO) * * * *")
    print()

    # Se recorre la pila de atrás hacia adelante (LIFO)
    for i in range(1, len(historial_pila) + 1):
        cambio = historial_pila[-i] 
        print(f"  {i}. {cambio}")
        print()
    
 
    
# * * * * * * * * * CODIGO PRINCIPAL GESTOR DE NOTAS ACADEMICAS * * * * * * * *

# MENU PRINCIPAL DEL GESTOR DE NOTAS ACADEMICAS

mostrarTitulo()

while True:
    print("1. REGISTRAR NUEVO CURSO")
    print("2. MOSTRAR TODOS LOS CURSOS Y NOTAS")
    print("3. CALCULAR PROMEDIO GENERAL")
    print("4. CONTAR CURSOS APROBADOS Y REPROBADOS")
    print("5. BUSCAR CURSO POR NOMBRE")
    print("6. ACTUALIZAR NOTA DE UN CURSO")
    print("7. ELIMINAR UN CURSO")
    print("8. ORDENAR CURSOS POR NOTA")
    print("9. ORDENAR CURSOS POR NOMBRE")
    print("10. REVISION DE CURSOS")
    print("11. HISTORIAL DE CAMBIOS")
    print("12. SALIR")
    opcion = input("POR FAVOR, SELECCIONE UNA OPCIÓN ")
    print()
    
 # dependiendo de la opción seleccionada, se llamara a la funcion correspondiente   
    
    if opcion == "1":
        registrar_nuevo_curso()
    elif opcion == "2":
        mostrar_cursosYnotas()
    elif opcion == "3":
        promedio_de_notas()
    elif opcion == "4":
        contar_aprobadosYreprobados()
    elif opcion == "5":
        buscar_curso()
    elif opcion == "6":
        actualizar_nota()
    elif opcion == "7":
        eliminar_curso()
    elif opcion == "8":
        ordenar_por_nota()
    elif opcion == "9":
        ordenar_por_nombre()
    elif opcion == "10":
        cola_revision()
    elif opcion == "11":
        historial()
    elif opcion == "12":
        print("SALIENDO DEL PROGRAMA...¡HASTA PRONTO!")
        print()
        break
    else:
        print("OPCION INVALIDA, POR FAVOR INTENTE DE NUEVO CON LAS OPCIONES DEL 1 AL 10")
        print()
