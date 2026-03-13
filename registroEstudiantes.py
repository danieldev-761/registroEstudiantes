def registroEstudiantes():

    materias= ("Matemáticas", "Lengua", "Ciencias sociales", "Ciencias naturales", "Educación física", "Inglés", "Informática")
   
    estudiantes= []
    id_actual_est= 1
    id_actual_materia= 1

    cantidad_notas_x_materia =1



    
    

    while True:
        print('''
              --------------- CALCULADORA DE NOTAS ---------------
                1. Registrar estudiantes
                2. Ver registros (individuales o generales)
                3. Agregar materias
                5. Salir
                
                Nota: - Para registrar un estudiante, primero debes agregar las materias a evaluar. 
                - Si no agregas materias, el programa registrará las notas de los estudiantes  
                - con las materias predefinidas.
        ''')
        
        try:
            
            opcion= int(input("Ingresa una opción del menú (1,2,3,4): "))
                
            match opcion:
                
                case 1:
                        
                    opc= 1
                    
                    while opc==1:

                        nombre= str(input("¿Cuál es el nombre del estudiante? "))

                        materias_regis = []
                        for materia in materias:
                            print(f"\nIngresando notas de {materia}:")

                            notas = []
                            for nota_indice in range(cantidad_notas_x_materia):
                                nota_valida = False
                                while not nota_valida:
                                    try:
                                        calificacion = float(input(f"Ingresa {nota_indice+1}° nota: "))
                                        if calificacion < 0 or calificacion > 5:
                                            print("Error: La nota debe ser un número entre 0 y 5")
                                        else:
                                            notas.append(calificacion)
                                            nota_valida = True

                                    except ValueError:
                                        print("Error: La nota debe ser un número válido")

                            promedio_materia = calcularPromedio(notas, cantidad_notas_x_materia)
                            materias_regis.append({
                                "id": id_actual_materia,
                                "materia": materia,
                                "notas": notas,
                                "promedio": promedio_materia
                            })
                            id_actual_materia += 1

                        promedios_materias = [m['promedio'] for m in materias_regis]
                        promedio = round(sum(promedios_materias) / len(promedios_materias), 3)
                        aprobado = True if promedio >= 3 else False

                        estudiante = {
                            "id": id_actual_est,
                            "nombre": nombre,
                            "materias": materias_regis,
                            "promedio": promedio,
                            "aprobado": aprobado
                        }

                        estudiantes.append(estudiante)
                        id_actual_est += 1

                        cargar_registros(estudiantes)

                        opc= (input("¿Desea registrar otro estudiante? (1: Sí, Cualquier otro valor: No) "))
                        opc= int(opc)
                    
                    numero_estudiantes= len(estudiantes)
                    
                    calcularPromedioGeneral(estudiantes, numero_estudiantes)

                    
                        

                case 2:

                    print("""----- REGISTROS DE ESTUDIANTES -----\n
                    1. Ver registros de todos los estudiantes
                    2. Ver registros de un estudiante específico
                          """)
                    
                    opcion_registros= int(input("Ingresa una opción (1 o 2, cualquier otra tecla para salir): "))

                    match opcion_registros:
                        case 1:
                    
                            if estudiantes!=[]:
                                
                                print("Cargando registros de estudiantes...")
                                cargar_registros(estudiantes)
                                numero_estudiantes= len(estudiantes)
                                calcularPromedioGeneral(estudiantes, numero_estudiantes)
                            else:
                                print("Base de datos vacía. Volviendo al menú principal...")

                        case 2:
                            if estudiantes!=[]:

                                print("Cargando registros de estudiantes...")
                                cargar_estudiantes(estudiantes)
                                

    
                                id_estudiante= int(input("Ingresa el ID del estudiante que deseas consultar: "))

                                estudiante_encontrado = None
                                for est in estudiantes:

                                    if est['id'] == id_estudiante:

                                        estudiante_encontrado = est
                                        break

                                if estudiante_encontrado:
                                    print(f"ID: {estudiante_encontrado['id']}  |  Estudiante: {estudiante_encontrado['nombre']}")

                                    for mat in estudiante_encontrado.get('materias', []):
                                        print(f"  - Materia: {mat['materia']} | Notas: {mat['notas']} | Promedio: {mat['promedio']}")

                                    print(f"  Promedio general (todas las materias): {estudiante_encontrado.get('promedio')}")

                                else:
                                    print("Error: No se encontró un estudiante con ese ID. Volviendo al menú principal...")
                            else:
                                print("Base de datos vacía. Volviendo al menú principal...")

                        case _:
                            print("Volviendo al menú principal...")
                    

                case 3:
                    seguir= 1
                    while seguir==1:

                        print("----- AGREGAR MATERIAS -----\n")
                        
                        print("MATERIAS ACTUALES")
                        
                        for i, materia in enumerate(materias, start=1):
                            print(f"{i}. {materia}")
                            
                        
                        nueva_materia= str(input("Ingresa el nombre de la nueva materia: ")).capitalize()
                        
                        if not validar_materia(nueva_materia, materias):
                            continue


                        print(f"Materia '{nueva_materia}' agregada exitosamente. Volviendo al menú principal... \n")
                        
                        seguir= (input("¿Desea agregar otra materia? (1: Sí, Cualquier otro valor: No) \n"))
                        seguir= int(seguir)
                
                case 4:
                    print("¡Gracias por usar nuestro programa! Vuelva pronto")
                    break

                case _:
                    print("Error: Opción no válida")


        except ValueError:
            print("Error: Campos con valores erróneos. Volviendo al menú principal...")
            
            
            
            
def calcularPromedio(notas, cantidad_notas):
    promedio= round(((sum(notas))/cantidad_notas), 3)
    return promedio
    
def cargar_registros(estudiantes):
    print("\nREGISTROS GUARDADOS:\n")

    for est in estudiantes:
        print(f"ID: {est['id']}  |  Estudiante: {est['nombre']}")
        for mat in est.get('materias', []):
            print(f"  - Materia: {mat['materia']} | Notas: {mat['notas']} | Promedio: {mat['promedio']}")
        print(f"  Promedio general (todas las materias): {est.get('promedio')}")
        print("--------------------------------------------------")

def calcularPromedioGeneral(estudiantes, numero_estudiantes):
    suma_promedios= 0 

    suma_promedios= sum(est['promedio'] for est in estudiantes)

    promedio_general= suma_promedios/numero_estudiantes

    print(f"Promedio general del salón de clases: {promedio_general}")

    aprobados= len([est for est in estudiantes if est['aprobado']== True])
    porcentaje_aprobados= (aprobados/numero_estudiantes)*100

    print(f"Cantidad de estudiantes aprobados: {aprobados}/{numero_estudiantes}")
    print(f"Porcentaje de estudiantes aprobados: {porcentaje_aprobados}%")

def validar_materia(nueva_materia, materias):

    if nueva_materia.strip() == "":
        print("Error: El nombre de la materia no puede estar vacío.")
        return False
    
    elif not nueva_materia.isalpha():
        print("Error: El nombre de la materia solo puede contener letras.")
        return False
    
    elif nueva_materia in materias:
        print("Error: La materia ya existe.")
        return False
    

    
    return True

def cargar_estudiantes(estudiantes):
    print("\nREGISTROS GUARDADOS:\n")

    for est in estudiantes:
        print(f"ID: {est['id']}  |  Estudiante: {est['nombre']}")
        

    
registroEstudiantes()