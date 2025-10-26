from lectura_csv import leer_paises_desde_csv
from busquedas_filtros import buscar_por_nombre, filtrar_por_continente, filtrar_por_rango_poblacion, filtrar_por_rango_superficie
from ordenamientos import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
from estadisticas import pais_con_mayor_menor_poblacion, promedio_poblacion, promedio_superficie, cantidad_por_continente
from utilidades import pedir_entero, pedir_texto

CSV_PATH = 'paises.csv'

def mostrar_paises(paises):
    if not paises:
        print('No hay países para mostrar.')
        return
    print(f'\nListado de {len(paises)} países:')
    for p in paises:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")

def menu_principal():
    paises = leer_paises_desde_csv(CSV_PATH)
    if not paises:
        print('No se cargaron países. Verifique el archivo CSV.')
    while True:
        print('\n--- MENÚ PRINCIPAL ---') 
        print('1. Buscar país por nombre')
        print('2. Filtrar países')
        print('3. Ordenar países')
        print('4. Ver estadísticas')
        print('5. Mostrar todos los países')
        print('0. Salir')

        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            termino = pedir_texto('Ingrese nombre o parte del nombre: ')
            mostrar_paises(buscar_por_nombre(paises, termino))

        elif opcion == '2':
            print('\n-- FILTRAR --') 
            print('a. Por continente') 
            print('b. Por rango de población') 
            print('c. Por rango de superficie')
            sub = input('Elija filtro (a/b/c): ').strip().lower()
            if sub == 'a':
                cont = pedir_texto('Ingrese continente (ej: América, Europa, Asia): ')
                mostrar_paises(filtrar_por_continente(paises, cont))
            elif sub == 'b':
                min_p = pedir_entero('Población mínima: ', minimo=0)
                max_p = pedir_entero('Población máxima: ', minimo=min_p)
                mostrar_paises(filtrar_por_rango_poblacion(paises, min_p, max_p))
            elif sub == 'c':
                min_s = pedir_entero('Superficie mínima (km²): ', minimo=0)
                max_s = pedir_entero('Superficie máxima (km²): ', minimo=min_s)
                mostrar_paises(filtrar_por_rango_superficie(paises, min_s, max_s))
            else:
                print('Opción inválida.')
        elif opcion == '3':
            print('\n-- ORDENAR --') 
            print('a. Por nombre') 
            print('b. Por población') 
            print('c. Por superficie') 
            sub = input('Elija criterio (a/b/c): ').strip().lower()
            sentido = input('Orden ascendente o descendente? (a/d): ').strip().lower()
            desc = True if sentido == 'd' else False
            if sub == 'a':
                mostrar_paises(ordenar_por_nombre(paises, desc))
            elif sub == 'b':
                mostrar_paises(ordenar_por_poblacion(paises, desc))
            elif sub == 'c':
                mostrar_paises(ordenar_por_superficie(paises, desc))
            else:
                print('Opción inválida.')
        elif opcion == '4':
            mayor, menor = pais_con_mayor_menor_poblacion(paises)
            if mayor and menor:
                print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})") 
                print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})") 
            print(f"Promedio de población: {promedio_poblacion(paises):.2f}") 
            print(f"Promedio de superficie: {promedio_superficie(paises):.2f} km²") 
            conteo = cantidad_por_continente(paises) 
            print('Cantidad de países por continente:') 
            for c, n in conteo.items(): 
                print(f"- {c}: {n}") 
        elif opcion == '5':
            mostrar_paises(paises)
        elif opcion == '0':
            print('Saliendo. ¡Hasta luego!')
            break
        else:
            print('Opción inválida.')

if __name__ == '__main__':
    menu_principal()
