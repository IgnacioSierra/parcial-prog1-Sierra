from validaciones import cargar_nombre, cargar_entero
from procesamientos import (buscar_mejor_promedio, buscar_peor_promedio, buscar_posicion, 
contar_alumnos_segun_condicion ,crear_lista, calcular_promedios, calcular_promedio_general, cargar_datos,
contar_vocales,mostrar_datos,mostrar_datos_individual, invertir_str, ordenamiento_burbuja)

bandera_carga = False
while True:
    print("\n===== NOTAFÁCIL =====")
    print('''
    1. Cargar alumnos
    2. Mostrar listado
    3. Mostrar estadísticas
    4. Ver ranking (ordenado)
    5. Buscar alumno
    6. Juegos con un nombre
    0. Salir''')

    opcion = input("Seleccione una opción: ")


    match opcion:
        case "1":
            print("Cargar alumnos")
            cantidad_alumnos = cargar_entero(1, 30, 'Ingrese cantidad de alumnos que desea cargar: ')
            
            lista_alumnos = crear_lista("", cantidad_alumnos)
            notas_parcial_1 = crear_lista(None, cantidad_alumnos)
            notas_parcial_2 = crear_lista(None, cantidad_alumnos) 
            cargar_datos(lista_alumnos, notas_parcial_1, notas_parcial_2)
            
            promedios = crear_lista(None, cantidad_alumnos)
            calcular_promedios(promedios, notas_parcial_1, notas_parcial_2)
            bandera_carga = True
        case "2":
            if bandera_carga == True:
                print("Mostrar listado")
                mostrar_datos(lista_alumnos, notas_parcial_1, notas_parcial_2, promedios)
            else:
                print('Para ejecutar esta opcion necesitas cargar alumnos.')
        case "3":
            if bandera_carga == True:
                print("Mostrar estadísticas")
                promedio_general = calcular_promedio_general(promedios)
                
                mejor_promedio = buscar_mejor_promedio(promedios)
                posicion_max = buscar_posicion(promedios, mejor_promedio)
                
                peor_promedio = buscar_peor_promedio(promedios)
                posicion_min = buscar_posicion(promedios, peor_promedio)
                
                lista_contador = contar_alumnos_segun_condicion(promedios)

                print(f'Promedio general: {promedio_general}')
                print(f'Mejor promedio: {mejor_promedio} Alumno: {lista_alumnos[posicion_max]}')
                print(f'Peor promedio: {peor_promedio} Alumno: {lista_alumnos[posicion_min]}')
                print(f'Cant alumnos en...')
                print(f'Promocion: {lista_contador[2]} Aprobados: {lista_contador[1]} Desaprobados: {lista_contador[0]}')
            else:
                print('Para ejecutar esta opcion necesitas cargar alumnos.')
        case "4":
            if bandera_carga == True:
                print("Ver ranking (ordenado)")
                ordenamiento_burbuja(lista_alumnos, notas_parcial_1, notas_parcial_2, promedios )
                mostrar_datos(lista_alumnos, notas_parcial_1, notas_parcial_2, promedios )        
            else:
                print('Para ejecutar esta opcion necesitas cargar alumnos.')
        case "5":
            if bandera_carga == True:               
                print("Buscando alumno")
                alumno_a_buscar = cargar_nombre('Ingrese el nombre del alumno que quiere buscar: ')
                buscar_posicion(lista_alumnos, alumno_a_buscar)
                mostrar_datos_individual(lista_alumnos, notas_parcial_1, notas_parcial_2, promedios )
            else:
                print('Para ejecutar esta opcion necesitas cargar alumnos.')
        
        case "6":
            if bandera_carga == True:
                nombre = cargar_nombre('Ingrese un nombre')
                cant_vocales = contar_vocales(nombre)
                nombre_invertido = invertir_str(nombre)
                
                print(f'Nombre: {nombre_invertido}. Tu nombre tiene {cant_vocales} vocales!!!. ')
            else:
                print('Para ejecutar esta opcion necesitas cargar alumnos.') 
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")