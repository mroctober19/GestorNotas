 # AVANCE 3 DEL GESTOR DE NOTAS ACADEMICAS 
 
# se crea un procedimiento para mostrar el titulo del proyecto
def mostrarTitulo():
    print("* * * * * GESTOR DE NOTAS ACADÉMICAS * * * * *")


notas = [] # esto sera una lista que contenga cursos y sus respectivas notas y sera en una forma de tupla, es decir, parejas
 
 # se crea una funcion que permita registrar un nuevo cursos
def registrar_nuevo_curso():
    curso = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA REGISTRAR: ")
    nota_str = input("INGRESE LA NOTA OBTENIDA PARA EL CURSO: ")
    # se verifica que la nota sea numero o se convierta en numero y adicional que se encuentr en el rango de 0 a 100
    while not nota_str.isdigit() or not (0 <= float(nota_str) <=100 ):
        print("NOTA FUERA DEL RANGO, POR FAVOR INTENTE CON UN VALOR ENTRE [0...100]")
        nota_str = input("INGRESE LA NOTA OBTENIDA PARA EL CURSO")
    nota = float(nota_str)
    
    notas.append((curso, nota))
    print("CURSO Y NOTA INGRESADOS CORRECTAMENTE")
    print()
     

# se crea una funcion que muestre todos los valores que el usuario ha ingresado (cursos y notas)
def mostrar_cursosYnotas():
    #se evalua que la lista tenga datos, de lo contrario, se le debe indicar al usuario
    if len(notas) == 0:
        print("NO EXISTEN CURSOS Y NOTAS INGRESADAS AL MOMENTO, POR FAVOR REGISTRE UNO NUEVO")
    else:
        print("CURSOS Y NOTAS REGISTRADAS: ")
        for curso, nota in notas:
            print(f"* {curso} : {nota}")
        print()

# se creara una funcion para el calculo del promedio
def promedio_de_notas():
    #verifiar que la lista no este vacia de lo contrario, se le indica al usuario
    if len(notas) == 0:
        print("NO HAY DATOS REGISTRADOS, POR FAVOR INFRESE UNA NUEVA TUPLA")
        return 
    #usar un bucle for que vara recorriendo las notas dentro de la lista, las sume y cuente la cantidad
    suma_notas = 0
    cantidad_notas = 0
    for curso, nota in notas:
        suma_notas += nota 
        cantidad_notas += 1
    #RETORNAR suma_notas / cantidad_notas
    promedio = suma_notas / cantidad_notas
    
    print(f"EL PROMEDIO ES DE: {promedio:.2f}")
    print()
    
#se crea una funcion que cuente los aprobados y los reprobados evaluando si la nota es >= 60
def contar_aprobadosYreprobados():
    aprobados = 0
    reprobados = 0
    #el _, significa que no se tomara en cuenta el nombre del curso, sino solo la nota
    for _, nota in notas:
        if nota >= 60:
            aprobados += 1
        else:
            reprobados += 1
    print(f"EL TOTAL DE CURSOS APROBADOS ES DE: {aprobados}")
    print(f"EL TOTAL DE CURSOS REPROBADOS ES DE: {reprobados}")
    print()
    
# se crea una funcion que permita buscar un curso por medio del nombre
def buscar_curso():
    curso_buscado = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA BUSCAR ")
    encontrado = False 
    for curso, nota in notas:
        if curso.lower() == curso_buscado.lower():
            print(f"CURSO ENCONTRADO: {curso}, {nota}")
            encontrado = True
            break
    if not encontrado:
        print("CURSO NO ENCONTRADO, POR FAVOR INTENTE NUEVAMENTE")
        print()
        
# se crea una funcino que permita actualizar una nota por el usuario
def actualizar_nota():
    curso_buscado = input("INGRESE EL NOMBRE DEL CURSO QUE DESEA ACTUALIZAR ")
    #se verifica si el curso si se encontro
    encontrado = False
    
    # la variable i va a recorrer el elemento de la lista notas
    for i in range(len(notas)):
        #se compara el nombre de la posicion que tenga i para compararlo con el curso buscado
        if notas[i][0].lower() == curso_buscado.lower():
            #si se encuentra el curso "encontrado" se vuelve True
            nota_nueva = input("INGRESE LA NUEVA NOTA DEL CURSO ")
            #se verifica que la nota nueva ingresada por el usuario este dentro del rango
            while not nota_nueva.isdigit() or not (0 <= float(nota_nueva)):
                nota_nueva = input("NOTA FUERA DE RANGO, INTENTE NUEVAMENTE")
            # se crea una nueva lista con el nombre del curso y la nueva nota    
            notas[i] = (notas[i][0], int(nota_nueva))
            print("NOTA ACTUALIZADA CON EXITO")
            print()
            return
    if not encontrado:    
        print("CURSO NO ENCONTRADO, POR FAVOR INTENTE NUEVAMENTE")
        print()
                            
    

# MENU PRINCIPAL DEL GESTOR DE NOTAS ACADEMICAS

mostrarTitulo()

while True:
    print("1. REGISTRAR NUEVO CURSO")
    print("2. MOSTRAR TODOS LOS CURSOS Y NOTAS")
    print("3. CALCULAR PROMEDIO GENERAL")
    print("4. CONTAR CURSOS APROBADOS Y REPROBADOS")
    print("5. BUSCAR CURSO POR NOMBRE (BUSQUEDA LINEAL)")
    print("6. ACTUALIZAR NOTA DE UN CURSO")
    print("7. SALIR")
    
    opcion = input("POR FAVOR, SELECCIONE UNA OPCIÓN ")
    
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
        print("SALIENDO DEL PROGRAMA...¡HASTA PRONTO!")
        break
    else:
        print("OPCION INVALIDA, POR FAVOR INTENTE DE NUEVO CON LAS OPCIONES DEL 1 AL 6")

    

         
        



         