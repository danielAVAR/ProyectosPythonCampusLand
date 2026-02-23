import json 
import os 

archivo = "usuarios.json"
archivo1= "peliculas.json"
archivo2= "musica.json"

def menu_principal():
    print("""
=====================================
    ADMINISTRADOR DE COLECCIÓN
=====================================
             
1. Añadir un Nuevo Elemento
2. Ver Todos los Elementos
3. Buscar un Elemento 
4. Editar un Elemento
5. Eliminar un Elemento
6. Guardar y Cargar Coleccion
7. Salir
======================================
Selecciona una opcion (1-7)""")
    
def menu_nuevo_elemento():
    print("""
===========================================
        Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):""")
    
def menu_ver_todos():
    print("""
===========================================
        Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda la Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):""")

def menu_buscar():
    print("""
===========================================
           Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por Título
2. Buscar por Autor/Director/Artista
3. Buscar por Género
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):""")
    
def menu_editar():
    print("""
===========================================
        Editar un Elemento
===========================================
¿Qué tipo de cambio deseas realizar?
1. Editar Título
2. Editar Autor/Director/Artista
3. Editar Género
4. Editar Valoración
5. Regresar al Menú Principal
===========================================
Selecciona una opción (1-5):""")

def menu_eliminar():
    print("""
===========================================
        Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Eliminar por Creador/Genero
3. Regresar al Menú Principal
===========================================
Selecciona una opción (1-3):""")
   
def menu_guadar_cargar():
    print("""
===========================================
        Guardar y Cargar Colección
===========================================
¿Qué deseas hacer?
1. Guardar la Colección Actual
2. Cargar una Colección Guardada
3. Regresar al Menú Principal
===========================================
Selecciona una opción (1-3):""")



#EJECUCION(1) AGREGAR


def agregar_libros(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            datos = json.load(f)
    else:
        datos = []

    titulo = input("Ingrese Titulo: ")
    autor = input("Ingrese Autor: ")
    genero = input("Ingrese Genero: ")
    puntuacion = int(input("Ingrese Puntuacion: "))

    #creacion de diccionario de dato

    libro_nuevo_usuario = {
        "Titulo": titulo,
        "Creador": autor,
        "Genero": genero,
        "Puntuacion": puntuacion
    }

    datos.append(libro_nuevo_usuario)

    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

        print("Libro Guardado Correctamente")

def agregar_peliculas(archivo1):
    if os.path.exists(archivo1):
        with open(archivo1, "r") as f:
            datos = json.load(f)
    else:
        datos = []

    pelicula = input("Ingrese Pelicula: ")
    director = input("Ingrese Director: ")
    genero = input("Ingrese Genero: ")
    puntuacion = int(input("Ingrese Puntuacion: "))

    #creacion de diccionario de dato

    pelicula_nuevo_usuario = {
        "Titulo": pelicula,
        "Creador": director,
        "Genero": genero,
        "Puntuacion": puntuacion
    }

    datos.append(pelicula_nuevo_usuario)

    with open(archivo1, "w") as f:
        json.dump(datos, f, indent=4)

        print("Pelicula Guardada Correctamente")

def agregar_musica(archivo2):
    if os.path.exists(archivo2):
        with open(archivo2, "r") as f:
            datos = json.load(f)
    else:
        datos = []

    cancion = input("Ingrese Cancion: ")
    artista = input("Ingrese Artista: ")
    genero = input("Ingrese Genero: ")
    puntuacion = int(input("Ingrese Puntuacion: "))

    #creacion de diccionario de dato

    musica_nuevo_usuario = {
        "Titulo": cancion,
        "Creador": artista,
        "Genero": genero,
        "Puntuacion": puntuacion
    }

    datos.append(musica_nuevo_usuario)

    with open(archivo2, "w") as f:
        json.dump(datos, f, indent=4)

        print("Musica Guardada Correctamente")


#EJECUCION(2) MOSTRAR


def mostrar_libros(archivo):
    with open(archivo, "r") as f:
        archivo = json.load(f)

        for archivo in archivo:
            print("-" * 20)
            print("Titulo: ", archivo["Titulo"])
            print("Autor: ", archivo["Autor"])
            print("Genero: ", archivo["Genero"]) 
            print("Puntuacion: ", archivo["Puntuacion"])
            print("-" * 20)

def mostrar_peliculas(archivo1):
     with open(archivo1, "r") as f:
        archivo1 = json.load(f)

        for archivo1 in archivo1:
            print("-" * 20)
            print("Titulo: ", archivo1["Pelicula"])
            print("Director: ", archivo1["Director"])
            print("Genero: ", archivo1["Genero"]) 
            print("Puntuacion: ", archivo1["Puntuacion"])
            print("-" * 20)

def mostrar_musica(archivo2):
    with open(archivo2, "r") as f:
        archivo2 = json.load(f)

        for archivo2 in archivo2:
            print("-" * 20)
            print("Titulo: ", archivo2["Cancion"])
            print("Director: ", archivo2["Artista"])
            print("Genero: ", archivo2["Genero"]) 
            print("Puntuacion: ", archivo2["Puntuacion"])


#EJECUCION(3) BUSCAR


def buscar_titulo(archivo, archivo1, archivo2):
    archivos = [archivo, archivo1, archivo2]
    buscar = input("Buscar: ").lower()    
    
    for archivos_actuales in archivos:
        with open(archivos_actuales, "r") as f:
            datos = json.load(f)

            for item in datos:
                if buscar in item["Titulo"].lower():
                    print(f"Encontrado en {archivos_actuales}:")
                    print(item)

def buscar_autor_artista_director(archivo, archivo1, archivo2):
    archivos = [archivo, archivo1, archivo2]
    buscar = input("Buscar: ").lower()    
    
    for archivos_actuales in archivos:
        with open(archivos_actuales, "r") as f:
            datos = json.load(f)

            for item in datos:
                if buscar in item["Creador"].lower():
                    print(f"Encontrado en {archivos_actuales}:")
                    print(item)

def buscar_genero(archivo, archivo1, archivo2):
    archivos = [archivo, archivo1, archivo2]
    buscar = input("Buscar: ").lower()    
    
    for archivos_actuales in archivos:
        with open(archivos_actuales, "r") as f:
            datos = json.load(f)

            for item in datos:
                if buscar in item["Genero"].lower():
                    print(f"Encontrado en {archivos_actuales}:")
                    print(item)


    archivos = [archivo, archivo1, archivo2]
    buscar = input("Buscar: ").lower()    
    
    for archivos_actuales in archivos:
        with open(archivos_actuales, "r") as f:
            datos = json.load(f)

            for item in datos:
                if buscar in item["Puntuacion"].lower():
                    print(f"Encontrado en {archivos_actuales}:")
                    print(item)


#EJECUCION(4) EDITAR

def editar_titulo(archivo, archivo1, archivo2):
    #buscar titulo especifico
    archivos = [archivo, archivo1, archivo2]
    titulo_buscar = input("¿Que titulo quieres editar?: ").lower()

    for archivo_actual in archivos:
        with open(archivo_actual, "r") as f:
            datos = json.load(f)
        
        encontrado = False
        for item in datos:
            if item["Titulo"].lower() == titulo_buscar:
                nuevo_titulo = input("Nuevo titulo: ")
                item["Titulo"] = nuevo_titulo
                encontrado = True
                break 
        
        if encontrado:
            with open(archivo_actual, "w") as f:
                json.dump(datos, f, indent=4)
            print("Titulo actualizado correctamente")
            return 
            
    print("Pelicula no encontrada")

    #identitificar titulo

    #remplazar viejo titulo con el nuevo

def editar_creador(archivo, archivo1, archivo2):
    archivos = [archivo, archivo1, archivo2]
    creador_buscar = input("¿Que creador quieres editar?: ").lower()

    for archivo_actual in archivos:
        with open(archivo_actual, "r") as f:
            datos = json.load(f)
        
        encontrado = False

        for item in datos:
            if item["Creador"].lower() == creador_buscar:
                nuevo_creador = input("Nuevo Creador: ")
                item["Creador"] = nuevo_creador
                encontrado = True
                break 
        
        if encontrado:
            with open(archivo_actual, "w") as f:
                json.dump(datos, f, indent=4)
            print("Creador actualizado correctamente")
            return 
        
    print("Pelicula no encontrada")

def editar_genero(archivo, archivo1, archivo2):
     archivos = [archivo, archivo1, archivo2]
     titulo_buscar = input("¿Que genero quieres editar?: ").lower()

     for archivo_actual in archivos:
        with open(archivo_actual, "r") as f:
            datos = json.load(f)
        
        encontrado = False

        for item in datos:
            if item["Genero"].lower() == titulo_buscar:
                nuevo_genero = input("Nuevo Genero: ")
                item["Genero"] = nuevo_genero
                encontrado = True
                break 
        
        if encontrado:
            with open(archivo_actual, "w") as f:
                json.dump(datos, f, indent=4)
            print("Genero actualizado correctamente")
            return 
        
     print("Pelicula no encontrada")

def editar_puntuacion(archivo, archivo1, archivo2):
    archivos = [archivo, archivo1, archivo2]
    titulo_buscar = int(input("¿Que puntuacion quieres editar?: "))

    for archivo_actual in archivos:
        with open(archivo_actual, "r") as f:
            datos = json.load(f)
        
        encontrado = False

        for item in datos:
            if item["Puntuacion"] == titulo_buscar:
                nueva_puntuacion = int(input("Nueva puntuacion: "))
                item["Puntuacion"] = nueva_puntuacion
                encontrado = True
                break 
        
        if encontrado:
            with open(archivo_actual, "w") as f:
                json.dump(datos, f, indent=4)
            print("Puntuacion actualizada correctamente")
            return 
        
    print("Elemento no encontrado")


#EJECUCION(5) ELIMINAR

def eliminar_por_titulo(archivo, archivo1, archivo2):
    archivos = [archivo, archivo1, archivo2]
    titulo_buscar = input("¿Qué título deseas eliminar?: ").lower()
    
    for archivo_actual in archivos:
        if os.path.exists(archivo_actual):
            with open(archivo_actual, "r") as f:
                datos = json.load(f)
            
            # Buscamos el elemento para borrarlo
            inicial_len = len(datos)
            datos = [item for item in datos if isinstance(item, dict) and item["Titulo"].lower() != titulo_buscar]
            
            # Si el tamaño de la lista cambió, es que lo borramos
            if len(datos) < inicial_len:
                with open(archivo_actual, "w") as f:
                    json.dump(datos, f, indent=4)
                print(f"Elemento eliminado de {archivo_actual}")
                return 
                
    print("No se encontró ningún elemento con ese título.")

    archivos = [archivo, archivo1, archivo2]
    titulo_buscar = input("¿Qué título deseas eliminar?: ").lower()
    
    for archivo_actual in archivos:
        if os.path.exists(archivo_actual):
            with open(archivo_actual, "r") as f:
                datos = json.load(f)
            
            # Buscamos el elemento para borrarlo
            inicial_len = len(datos)
            datos = [item for item in datos if isinstance(item, dict) and item["Titulo"].lower() != titulo_buscar]
            
            # Si el tamaño de la lista cambió, es que lo borramos
            if len(datos) < inicial_len:
                with open(archivo_actual, "w") as f:
                    json.dump(datos, f, indent=4)
                print(f"Elemento eliminado de {archivo_actual}")
                return 
                
    print("No se encontró ningún elemento con ese título.")

    archivos = [archivo, archivo1, archivo2]
    titulo_buscar = input("¿Qué título deseas eliminar?: ").lower()
    
    for archivo_actual in archivos:
        if os.path.exists(archivo_actual):
            with open(archivo_actual, "r") as f:
                datos = json.load(f)
            
            # Buscamos el elemento para borrarlo
            inicial_len = len(datos)
            datos = [item for item in datos if isinstance(item, dict) and item["Titulo"].lower() != titulo_buscar]
            
            # Si el tamaño de la lista cambió, es que lo borramos
            if len(datos) < inicial_len:
                with open(archivo_actual, "w") as f:
                    json.dump(datos, f, indent=4)
                print(f"Elemento eliminado de {archivo_actual}")
                return 
                
    print("No se encontró ningún elemento con ese título.")

def eliminar_por_otro(archivo, archivo1, archivo2):
     archivos = [archivo, archivo1, archivo2]
     # Pedimos el dato (puede ser el nombre del autor o el género)
     busqueda = input("Ingresa el Nombre del Creador o el Género para eliminar: ").lower()
     encontrado_global = False

     for archivo_actual in archivos:
        if os.path.exists(archivo_actual):
            with open(archivo_actual, "r") as f:
                datos = json.load(f)
            
            nueva_lista = []
            for item in datos:
                # Verificamos que sea un diccionario y que tenga los campos
                if isinstance(item, dict):
                    creador = item.get("Creador", "").lower()
                    genero = item.get("Genero", "").lower()
                    
                    # Si NO coincide con ninguno, lo guardamos en la nueva lista
                    if busqueda != creador and busqueda != genero:
                        nueva_lista.append(item)
                    else:
                        encontrado_global = True

            # Si borramos algo, actualizamos el archivo
            if encontrado_global:
                with open(archivo_actual, "w") as f:
                    json.dump(nueva_lista, f, indent=4)
                print(f"Se han eliminado los elementos que coincidían en: {archivo_actual}")
    
     if not encontrado_global:
        print("No se encontró nada con ese Creador o Género.")


#EJECUCION (6) GUARDAR CARGAR
def guardar_cargar_confirmacion(archivo, archivo1, archivo2):
   
    archivos = [archivo, archivo1, archivo2]
    for a in archivos:
        if os.path.exists(a):
            with open(a, "r") as f:
                datos = json.load(f)
                print(f"Archivo {a} cargado con {len(datos)} elementos.")
        else:
            print(f"Archivo {a} no existe todavía (se creará al añadir algo).")


#EJECUCIONES
def ejecucion_1():
    while True:
        menu_nuevo_elemento()
        opcion = pedir_opcion()
        if opcion == 1:
            #Libros
            agregar_libros(archivo)
        elif opcion == 2:
            agregar_peliculas(archivo1) 
        elif opcion == 3: 
            agregar_musica(archivo2)
        elif opcion == 4: 
            menu_principal()
            break
        else:
            ("OPCION INVALIDA")

def ejecucion_2():
    while True:
        menu_ver_todos()
        opcion = pedir_opcion()
        if opcion == 1:
            mostrar_libros(archivo)

        elif opcion == 2:
            mostrar_peliculas(archivo1) 
        elif opcion == 3: 
            mostrar_musica(archivo2)
        elif opcion == 4: 
            menu_principal()
            break
        else:
            ("OPCION INVALIDA")

def ejecucion_3():
    while True:
        menu_buscar()
        opcion = pedir_opcion()
        if opcion == 1:
            buscar_titulo(archivo, archivo1, archivo2)
        elif opcion == 2:
            buscar_autor_artista_director(archivo, archivo1, archivo2) 
        elif opcion == 3: 
            buscar_genero(archivo, archivo1, archivo2)
        elif opcion == 4: 
            menu_principal()
            break
        else:
            ("OPCION INVALIDA")

def ejecucion_4():
    while True:
        menu_editar()
        opcion = pedir_opcion()
        if opcion == 1:
            editar_titulo(archivo, archivo1, archivo2)
        elif opcion == 2:
            editar_creador(archivo, archivo1, archivo2) 
        elif opcion == 3: 
            editar_genero(archivo, archivo1, archivo2)
        elif opcion == 4: 
            editar_puntuacion(archivo, archivo1, archivo2)
        elif opcion == 5:
            menu_principal()
            break
        else:
            ("OPCION INVALIDA")
    
def ejecucion_5():
    while True:
        menu_eliminar()
        opcion = pedir_opcion()
        if opcion == 1:
            eliminar_por_titulo(archivo, archivo1, archivo2)
        elif opcion == 2:
            eliminar_por_otro(archivo, archivo1, archivo2)
        elif opcion == 3:
            menu_principal()
            break 
        else:
            print("OPCION INVALIDA")
 
def ejecucion_6():
     while True:
        menu_guadar_cargar()
        opcion = pedir_opcion()
        if opcion == 1:
            print("¡Los datos se guardan automáticamente después de cada cambio!")
        elif opcion == 2:
            guardar_cargar_confirmacion(archivo, archivo1, archivo2)
        elif opcion == 3: 
            menu_principal()
            break
        else:
            print("OPCION INVALIDA")




def pedir_opcion():
    opc = int(input("Ingrese la opcion: "))
    return opc

menu_principal()

while True:
    opcion = pedir_opcion()
    if opcion == 1:
        ejecucion_1()
    elif opcion == 2:
        ejecucion_2()
    elif opcion == 3:
        ejecucion_3()
    elif opcion == 4:
        ejecucion_4()
    elif opcion == 5:
        ejecucion_5()
    elif opcion == 6:
        ejecucion_6()
    elif opcion == 7:
        print("AHH")
        break
    else:
        print("OPCION INVALIDA")


      
