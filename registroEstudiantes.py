def registroEstudiantes():

    materias= ("Matemáticas", "Lengua", "Ciencias sociales", "Ciencias naturales", "Educación física", "Inglés", "Informática")
   
    estudiantes= []
    id_actual_est= 1
    id_actual_materia= 1

    cantidad_notas_x_materia =3

    notas_x_estudiante=[]

    
    

    while True:
        print('''
              --------------- CALCULADORA DE NOTAS ---------------
                1. Registrar estudiantes
                2. Ver registros
                3. Agregar materias
                4. Salir
        ''')
        
        try:
            
            opcion= int(input("Ingresa una opción del menú: "))
            
                
            match opcion:
                
                case 1:
                        
                    opc= 1
                    
                    while opc==1:

                        nombre= str(input("¿Cuál es el nombre del estudiante? "))
                                            
                        notas= []
                        i= 0

                        for materia in range(len(materias)):
                            print(f"\nIngresando notas de {materias[materia]}:")
                            for nota in range(cantidad_notas_x_materia):

                                nota_valida = False
                                while not nota_valida:
                                    try:
                                        calificacion = float(input(f"Ingresa {nota+1}° nota: "))

                                        if calificacion < 0 or calificacion > 5:
                                            print("Error: La nota debe ser un número entre 0 y 5")
                                        else:
                                            notas.append(calificacion)
                                            i += 1
                                            nota_valida = True

                                    except ValueError:
                                        print("Error: La nota debe ser un número válido")
                            
                        
                        promedio= calcularPromedio(notas, cantidad_notas_x_materia)
                        aprobado= True if promedio>=3 else False
                                
                

                        notas_x_materia={
                            "id": id_actual_materia,
                            "materia": materias[i],
                            "notas": notas
                        }

                        estudiante = {
                        "id": id_actual_est,
                        "nombre": nombre,
                        "notas": notas_x_materia,
                        "promedio": promedio,
                        "aprobado": aprobado
                    }

                        notas_x_estudiante.append(notas_x_materia)
                        estudiantes.append(estudiante)

                        id_actual_materia += 1
                        id_actual_est += 1
                            
                        cargar_registros(estudiantes)
                    
                    numero_estudiantes= len(estudiantes)
                    
                    calcularPromedioGeneral(estudiantes, numero_estudiantes)

                    opc= (input("¿Desea registrar otro estudiante? (1: Sí, Cualquier otro valor: No) "))
                    opc= int(opc)
                        

                case 2:
                    
                    if estudiantes!=[]:
                        
                        print("Cargando registros de estudiantes...")
                        cargar_registros(estudiantes)
                        numero_estudiantes= len(estudiantes)
                        calcularPromedioGeneral(estudiantes, numero_estudiantes)
                    else:
                        print("Base de datos vacía. Volviendo al menú principal...")
                    

                case 3:
                    print("¡Gracias por usar nuestro programa! Vuelva pronto")
                    break

                case _:
                    print("Error: Opción no válida")


        except ValueError:
            print("Error: Campos con valores erróneos")
            
            
            
            
def calcularPromedio(notas, cantidad_notas):
    promedio= round(((sum(notas))/cantidad_notas), 3)
    return promedio
    
def cargar_registros(estudiantes):
    print("\nREGISTROS GUARDADOS:\n")
    print("ID  | ESTUDIANTE | NOTAS | PROMEDIO | APROBADO")
    print("--------------------------------------------------")
        
    for est in estudiantes:
            print(f"  {est['id']}  | {est['nombre']} |    {est['notas']} |    {est['promedio']} |    {est['aprobado']}")
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

    
registroEstudiantes()