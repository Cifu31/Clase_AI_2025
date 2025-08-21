# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 18:54:49 2025

@author: camic

Este código desarrolla una simulación simple de un robot en una grilla 2x2,
aplicando los conceptos de:
- Estado
- Espacio de estados
- Acciones
- Recompensa
- Ambiente

Además, cumple con los 4 puntos solicitados en la tarea:

1. Modificar la función mover_robot para que la batería baje en cada movimiento.
2. Si la batería llega a 0, el robot no se puede mover hasta recargar.
3. Añadir más recompensas o castigos (intentar moverse sin batería, bonus por llegar rápido, etc).
4. Probar diferentes estrategias de movimiento para maximizar la recompensa.
"""

# ========================
# 1. VARIABLES DE ESTADO
# ========================
# El estado inicial del robot incluye:
# - posición en la grilla (0,0)
# - nivel de batería (50)
# - si alcanzó o no el objetivo (False)
estado_robot = {
    "posicion": (0, 0),
    "bateria": 50,
    "objetivo_alcanzado": False
}

print("Estado inicial del robot:", estado_robot)

# ========================
# 2. ESPACIO DE ESTADOS
# ========================
# El espacio de estados es el conjunto de todas las combinaciones
# posibles de posiciones y niveles de batería (simplificado en "alta" o "baja").
posiciones = [(x, y) for x in range(3) for y in range(3)]
baterias = ["alta", "baja"]

espacio_estados = [(p, b) for p in posiciones for b in baterias]
print("\nTotal de estados posibles:", len(espacio_estados))
print("Ejemplos de estados:", espacio_estados[:5])

# ========================
# 3. ESPACIO DE ACCIONES
# ========================
# El robot puede moverse en las 4 direcciones básicas o recargar su batería.
acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]
print("\nAcciones posibles:", acciones)

# ========================
# 4. FUNCIÓN DE RECOMPENSA
# ========================
# Aquí se definen las recompensas y castigos que recibe el robot
# dependiendo de la acción tomada y el estado alcanzado.
def recompensa(accion, nuevo_estado, paso):
    # Recompensa por recargar
    if accion == "recargar":
        return 5
    
    # Castigo por intentar moverse sin batería
    if accion in ["adelante", "atras", "izquierda", "derecha"] and nuevo_estado["bateria"] == 0 and not nuevo_estado["objetivo_alcanzado"]:
        return -5  

    # Recompensa por alcanzar el objetivo
    if nuevo_estado["objetivo_alcanzado"]:
        if paso < 5:  # Bonus por hacerlo rápido
            return 30  
        else:
            return 10  
    
    # Costo de cada movimiento normal
    if accion in ["adelante", "atras", "izquierda", "derecha"]:
        return -1  
    
    return 0

# ========================
# 5. AMBIENTE Y SIMULACIÓN
# ========================
# Esta función describe cómo el ambiente responde a las acciones del robot.
def mover_robot(estado, accion):
    x, y = estado["posicion"]

    if accion in ["adelante", "atras", "derecha", "izquierda"]:
        # SOLO se mueve si tiene batería
        if estado["bateria"] > 0:
            if accion == "adelante":
                x = min(x + 1, 2)
            elif accion == "atras":
                x = max(x - 1, 0)
            elif accion == "derecha":
                y = min(y + 1, 2)
            elif accion == "izquierda":
                y = max(y - 1, 0)
            
            # La batería baja 10 unidades por cada movimiento (PUNTO 1)
            estado["bateria"] = max(estado["bateria"] - 10, 0)
        else:
            # Si no tiene batería, no se mueve (PUNTO 2)
            print("⚠️ BATERIA AGOTADA, POR FAVOR RECARGA")

    elif accion == "recargar":
        # Acción de recarga, devuelve batería al 100
        estado["bateria"] = 100

    # Se actualiza la posición
    estado["posicion"] = (x, y)

    # Si llega a (2, 2), se considera objetivo alcanzado
    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    return estado

# ========================
# 6. SIMULACIÓN DEL ROBOT (MANUAL)
# ========================
# Aquí se permite al usuario controlar el robot manualmente.
# La recompensa total se acumula según las reglas definidas.
estado = {"posicion": (0, 0), "bateria": 50, "objetivo_alcanzado": False}
recompensa_total = 0

print("\n=== SIMULACIÓN DEL ROBOT (MODO MANUAL) ===")
for paso in range(10):  # Se limita a 10 pasos
    print("\nEstado actual:", estado)
    accion = input("Elige una acción (adelante, atras, izquierda, derecha, recargar): ")

    # Normalizamos la entrada
    accion = accion.strip().lower()

    if accion not in acciones:
        print("⚠️ Acción no válida, intenta de nuevo.")
        continue

    # Se actualiza el estado con la acción elegida
    estado = mover_robot(estado, accion)

    # Se calcula la recompensa correspondiente
    r = recompensa(accion, estado, paso)
    recompensa_total += r

    print(f"Paso {paso+1}: Acción = {accion}, Estado = {estado}, Recompensa = {r}")

    # Si el robot llega a la meta, se termina la simulación
    if estado["objetivo_alcanzado"]:
        print("🎉 ¡Objetivo alcanzado!")
        break

# Al final se muestra la recompensa acumulada
print("\n✅ Recompensa total obtenida:", recompensa_total)

