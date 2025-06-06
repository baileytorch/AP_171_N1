from data.crear_data import guardar_data
from data.leer_data import listado_data
from data.asignaturas import asignaturas

# READ DATA
def obtener_listado_asignaturas():    
    print()
    print('Listado de Asignaturas')
    print('======================')
    listado_data('asignaturas.py')

# READ DATA
def obtener_asignatura_individual():
    asignatura_encontrada = 'asignatura NO encontrada'
    busqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            asignatura_encontrada = asignatura
    return asignatura_encontrada

# CREATE DATA
def guardar_nueva_asignatura():
    obtener_listado_asignaturas()
    nueva_asignatura = input('Ingrese nueva asignatura: ')
    asignaturas.append(nueva_asignatura.title())
    guardar_data('asignaturas',asignaturas,'asignaturas.py')
    
# UPDATE DATA
def actualizar_asignatura():
    obtener_listado_asignaturas()
    busqueda = input("Ingrese asignatura a buscar: ")
    indice_asignatura = 0
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            asignatura_modificada = input("Ingrese nuevo nombre de asignatura: ")
            indice_asignatura = i
            break
    asignaturas[indice_asignatura] = asignatura_modificada
    guardar_data('asignaturas',asignaturas,'asignaturas.py')

# DELETE DATA
def eliminar_asignatura():
    pass