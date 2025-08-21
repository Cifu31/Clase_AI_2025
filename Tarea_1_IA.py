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
# Estado inicial del robot
estado_robot = {
    "posicion": (0, 0),
    "bateria": 50,
    "objetivo_alcanzado": False
}

print("Estado inicial del robot:", estado_robot)

# ========================
# 2. ESPACIO DE ESTADOS
# ========================
posiciones = [(x, y) for x in range(3) for y in range(3)]
baterias = ["alta", "baja"]

espacio_estados = [(p, b) for p in posiciones for b in baterias]
print("\nTotal de estados posibles:", len(espacio_estados))
print("Ejemplos de estados:", espacio_estados[:5])

# ========================
# 3. ESPACIO DE ACCIONES
# ========================
acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]
print("\nAcciones posibles:", acciones)

# ========================
# 4. FUNCIÓN DE RECOMPENSA
# ========================
# 🔹 NUEVO: se agregó esta función para manejar las recompensas y castigos.
# Antes solo existía el movimiento, ahora se cuantifican las acciones.
def recompensa(accion, nuevo_estado, paso):
    # Recompensa por recargar
    if accion == "recargar":
        return 5
    
    # Castigo por intentar moverse sin batería (PUNTO 3)
    if accion in ["adelante", "atras", "izquierda", "derecha"] and nuevo_estado["bateria"] == 0 and not nuevo_estado["objetivo_alcanzado"]:
        return -5  

    # Recompensa por alcanzar el objetivo
    if nuevo_estado["objetivo_alcanzado"]:
        if paso < 5:  # Bonus por hacerlo rápido (PUNTO 3)
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
# 🔹 FUNCION MODIFICADA: mover_robot ahora incluye el consumo de batería y bloqueo
# si la batería llega a 0 (PUNTOS 1 y 2).
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
            
            # 🔹 CAMBIO: la batería baja en cada movimiento (PUNTO 1)
            estado["bateria"] = max(estado["bateria"] - 10, 0)
        else:
            # 🔹 CAMBIO: aviso si no puede moverse por falta de batería (PUNTO 2)
            print("⚠️ BATERIA AGOTADA, POR FAVOR RECARGA")

    elif accion == "recargar":
        # 🔹 NUEVO: acción de recarga (PUNTO 2)
        estado["bateria"] = 100

    # Se actualiza la posición
    estado["posicion"] = (x, y)

    # 🔹 CAMBIO: Se define (2,2) como el objetivo final
    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    return estado

# ========================
# 6. SIMULACIÓN DEL ROBOT (MANUAL)
# ========================
# 🔹 NUEVO: se agregó un bucle para controlar el robot manualmente (PUNTO 4).
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

# Resultado final
print("\n✅ Recompensa total obtenida:", recompensa_total)
