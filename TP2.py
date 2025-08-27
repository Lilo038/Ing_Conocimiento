
import random
print("Ejercicio 1.")
print("Mi Primer Código En Python.")

print("Ejercicio 2.")
lista = ["A\t","B\t","C\t","D\t","E\t","F\t","G\t","H\t","I\t"]

for i in range(0, 9):
    if i == 3 or i == 6:
        print()    
    print(lista[i], end=" ")

print("\nEjercicio 3.")

print("¿Que estas estudiando?")
respuesta= input()
print(respuesta)
    
print("Ejercicio 4.")       
print("¿En qué país vives?")    
respuesta= input()
print(respuesta)

print("Ejercicio 5.")
nombre="David Bowman"
edad="51"
print(nombre,edad)

print("Ejercicio 6.")
nombre = "Julia"
apellido = "Roberts"
nombrecompleto= nombre+" "+apellido
print(nombrecompleto)

print("Ejercicio 7.")
materia= "Ingeniería del conocimiento"
print("Estas estudiando "+materia)

print("Ejercicio 8.")
numl= 35
print(type(numl))

print("Ejercicio 9.")
nombre_asociado= nombrecompleto
numero_asociado= str(random.randint(1000, 9999))
print("Estimado/a "+nombre_asociado+", su número de asociado es: "+numero_asociado)

print("Ejercicio 10.")
print(874//27)

print("Ejercicio 11.")
print(round(10.676767))

print("Ejercicio 12.")

productos = []
for i in range (0,3):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    cantidad = int(input(f"Ingrese la cantidad disponible de {nombre}: "))
    productos.append((nombre, precio, cantidad))
print(max(productos, key= lambda p: p[1]))

print("Ejercicio 13.")

estudiantes = {}
calificaciones = []    
for i in range (0,3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    calificaciones = {}
    for x in range (0,3):
        materia = input(f"Ingrese la materia {x+1}: ")
        nota = int(input(f"Ingrese la nota de {nombre} en {materia}: "))
        calificaciones[materia]=nota
    estudiantes[i]= {
        "nombre": nombre,
        "edad": edad,
        "calificaciones":calificaciones
    }
print(estudiantes)
def promedio(estudiante):
    notas = estudiante["calificaciones"]
    return sum(notas.values()) / len(notas)

registro = int(input("Ingrese el registro del estudiante: "))
prom = promedio(estudiantes[registro])
print(f"El promedio del estudiante es: {prom}")

print("Ejercicio 14.")
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def maxima(temperaturas):
    return max(temperaturas)
def minima(temperaturas):
    return min(temperaturas)
def media(temperaturas):
    return sum(temperaturas)/len(temperaturas)
print("La media de este mes fue: ", media(temperaturas),"ºC con una maxima de ", maxima(temperaturas),"ºC y una minima de ", minima(temperaturas),"ºC")

print("Ejercicio 15.")
def calcular_promedio(*args):
    return sum(args)/len(args)

print("Promedio: ", calcular_promedio(85, 90, 78, 92))

print("Ejercicio 16.")
usuario = {}
def crear_perfil(**kwargs):
    
    return kwargs

usuario[1] = crear_perfil(nombre="Luis", edad=25, email="Luis@mail.com", ciudad="Mendoza")
usuario[2] = crear_perfil(nombre="Juan", edad=25, email="juan@mail.com", ciudad="San Rafael")
print (usuario)
print (usuario[1]["nombre"])

print("Ejercicio 17.")

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
monto = 2600

def ganan_mas(empleados, monto):
    mayores  = {id: datos for id, datos in empleados.items() if datos[2] > monto}
    return mayores

print("Estos empleados " , ganan_mas(empleados,monto)," ganan mas de ", monto)

print("Ejercicio 18.")

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def procesar(ventas_diarias):
    total=sum(ventas_diarias)
    prom=total/len(ventas_diarias)
    return total,prom
total,promedio=procesar(ventas_diarias)
print(f"Total de ventas: {total}")
print(f"Promedio de ventas por día: {promedio:.2f}")

print("Ejercicio 19.")
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def goles(resultados):
    anotados = sum(gol[0] for gol in resultados.values())
    recibidos = sum(gol[1] for gol in resultados.values())
    return anotados,recibidos

anotados,recibidos = goles(resultados)

print(f"Total anotados {anotados}")
print(f"Total recibidos {recibidos}")

print("Ejercicio 20.")

def configurar_app(**kwargs):
    return  kwargs

config = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

print(config)
print(config["modo_oscuro"])

print("Ejercicio 21.")

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def mayor_a_menor(puntuaciones):
    return sorted(puntuaciones, key=lambda x:x[1])
orden = mayor_a_menor(puntuaciones)
print(f"Lista ordenada de mayor a menor: {orden}")

print("Ejercicio 22.")

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]
def costototal(paquetes):
    dic_pack = {Destino: precio * dias for Destino, precio, dias in paquetes}
    return dic_pack
destinos=costototal(paquetes)
print(destinos)

print("Ejercicio 23.")

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(a,b):
    resta = [x - y for x, y in zip(a, b)]
    return resta

inventario = actualizar_inventario(inventario,ventas)
print(f"Inventario Actualizado: {inventario}")

print("Ejercicio 24.")

def organizar_eventos(*args):
    for i, eventos in enumerate(args,start=1):
        print(f"{i}: {eventos}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

print("Ejercicio 25.")

def analizar_finanzas(**kwargs):
    balance = sum(kwargs.values())
    return balance
print(analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)) 

print("Ejercicio 26.")

def registro_empleado(nombre, edad, salario,**kwargs):
    empleados= {
        "Nombre":nombre,
        "Edad":edad,
        "Salario":salario
    }
    empleados.update(kwargs)
    return empleados

print(registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789"))

print("Ejercicio 27.")

def calcular_ventas(mensual):
    
    calculo={
        "Promedio":sum(mensual)/len(mensual),
        "Total":sum(mensual),
        "mes con mayores ventas":mensual.index(max(mensual))+1
    }
    return calculo


ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

print(calcular_ventas(ventas_mensuales))

print("Ejercicio 28.")

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"},
}

def despues_del_2000(biblioteca):
    libros_recientes = [titulo for titulo, info in biblioteca.items() if info["año"] > 2000]
    return libros_recientes
    
print(despues_del_2000(biblioteca))

print("Ejercicio 29.")
notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
def calcular_promedios(notas_estudiantes):
    promedios = {}  # Diccionario resultado
    for nombre, calificaciones in notas_estudiantes:
        promedio = sum(calificaciones) / len(calificaciones)  # promedio de cada lista
        promedios[nombre] = promedio  # guardar en el diccionario
    return promedios

print(calcular_promedios(notas_estudiantes))

print("Ejercicio 30.")

usuarios = ["Ana", "Luis", "María"]


def configurar_perfiles(usuarios,**kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = list(kwargs.items())
    return perfiles

print(configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False))

print("Ejercicio 31.")

def publicar(usuario, texto, etiquetas=None, **kwargs):

    if etiquetas is None:
        etiquetas = []

    publicacion = {
        "usuario": usuario,
        "texto": texto,
        "etiquetas": etiquetas
    }

    for clave, valor in kwargs.items():
        publicacion[clave] = valor

    return publicacion

print(publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100))

print("Ejercicio 32.")


def simular_ventas(*args):
    total=0
    for producto, cantidad , precio in args:
        ventas= cantidad*precio
        total=+ventas

    return total

print(simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0)))

print("Ejercicio 33.")


def hacer_reserva(reservas, fecha, huesped, habitacion, precio):

    if fecha not in reservas:
        reservas[fecha] = []

    for reserva in reservas[fecha]:
        if reserva[1] == habitacion: 
            return f"Habitación {habitacion} ya está ocupada en {fecha}"

    reservas[fecha].append((huesped, habitacion, precio))
    return f"Reserva confirmada para {huesped} en {fecha}, habitación {habitacion}"

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

print(hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 160))  

print(hacer_reserva(reservas, "2024-08-15", "Sofía", 103, 200))  


print(reservas)

print("Ejercicio 34.")



def contador(encuestas):
    resultados={}
    for pregunta, respuestas in encuestas.items():
        frecuencias={}
        for r in respuestas:
            frecuencias[r] = frecuencias.get(r, 0) + 1  
            resultados[pregunta] = frecuencias  

    return resultados 

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
print(contador(encuestas))


print("Ejercicio 35.")

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]



def optimizar_rutas(rutas,distancia_max):
    rutas_validas = []
    for i,(origen, destino, distancia) in enumerate(rutas):
        if distancia<=distancia_max[i]:
            rutas_validas.append((origen, destino, distancia))
    return rutas_validas

print(optimizar_rutas(rutas,distancias_max))

print("Ejercicio 36.")


inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(tienda, **kwargs):
    
    if tienda not in inventario:
        inventario[tienda] = {}  

    
    for producto, cambio in kwargs.items():
        if producto in inventario[tienda]:
            inventario[tienda][producto] += cambio
        else:
            inventario[tienda][producto] = cambio

        if inventario[tienda][producto] < 0:
            inventario[tienda][producto] = 0

    return inventario


print(actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5))


print("Ejercicio 37.")

def analizar_tendencias(hashtags, tendencias, minimo=100):

    dict_tendencias = dict(tendencias)

   
    resultado = []

    for hashtag in set(hashtags):  
        if hashtag in dict_tendencias and dict_tendencias[hashtag] > minimo:
            resultado.append((hashtag, dict_tendencias[hashtag]))

    return resultado

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

print(analizar_tendencias(hashtags, tendencias, minimo=100))

print("Ejercicio 38.")

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
 
    
    if usuario not in suscripciones:
        suscripciones[usuario] = []

    
    suscripciones[usuario].append(suscripcion)

    
    if kwargs:
        
        suscripciones[usuario].append(kwargs)

    return suscripciones

print(actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True))
print(actualizar_suscripcion(usuario="Ana", suscripcion="anual"))

print("Ejercicio 39.")

def simular_mercado(precios_diarios, operaciones):
    beneficio_total = 0
    cantidad_acciones = 0
    precio_compra = 0

    for op, dia in operaciones:
        precio = precios_diarios[dia]

        if op == "compra":
            
            cantidad_acciones += 1
            precio_compra += precio  

        elif op == "venta":
            if cantidad_acciones > 0:
                
                promedio_compra = precio_compra / cantidad_acciones
                beneficio_total += (precio - promedio_compra) * cantidad_acciones
                
                cantidad_acciones = 0
                precio_compra = 0
            else:
                print(f"Venta en día {dia} sin acciones disponibles")

    return beneficio_total

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = simular_mercado(precios_diarios, operaciones)
print("Beneficio/Pérdida total:", resultado)

print("Ejercicio 40")

def ranking_estudiantes(estudiantes):
    promedios = {}

    for id_est, materias in estudiantes.items():
        
        todas_calificaciones = []
        for notas in materias.values():
            todas_calificaciones.extend(notas)
        
        promedio = sum(todas_calificaciones) / len(todas_calificaciones)
        promedios[id_est] = promedio


    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)

    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

resultado = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes (ID, promedio):")
for id_est, prom in resultado:
    print(f"{id_est}: {prom:.2f}")

