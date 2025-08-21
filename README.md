# Tarea 1 - Inteligencia Artificial

Este repositorio contiene un programa en Python que simula un robot en una cuadrícula.  
El robot puede moverse en cuatro direcciones, tiene una batería limitada y obtiene recompensas o castigos según sus acciones.  

Objetivos de la tarea
- Implementar un robot que pueda desplazarse en una cuadrícula.
- Incluir un sistema de batería que limite los movimientos del robot.
- Añadir recompensas y castigos según el comportamiento.
- Permitir un modo manual de control del robot.
- Documentar el código en un repositorio de GitHub.

---

Funcionamiento del programa
1. El robot comienza en la posición (0,0) con una batería al 100%.
2. Puede moverse en cuatro direcciones: arriba, abajo, izquierda y derecha.
3. Cada movimiento **consume batería**.
4. Si la batería llega a 0, aparece el mensaje:
5. El robot acumula puntos (recompensas o castigos) dependiendo de sus acciones.
6. Se puede jugar en modo manual, indicando los movimientos desde teclado.

---

 Reglas de recompensas y castigos
- **Moverse con batería disponible:** +1 punto.
- **Intentar moverse sin batería:** -5 puntos.
- **Llegar al objetivo:** +10 puntos.
- **Llegar al objetivo en menos de 5 movimientos:** +20 puntos adicionales.
- **Cada movimiento consume batería** (ejemplo: -10% por movimiento).

---

Cambios realizados al código original
Para cumplir con las condiciones de la tarea se hicieron los siguientes cambios:
1. **Sistema de batería:** Se agregó un contador de batería que disminuye con cada movimiento.
2. **Aviso de batería agotada:** Ahora el programa muestra el mensaje en mayúsculas `"BATERIA AGOTADA, POR FAVOR RECARGA"`.
3. **Modo manual:** Se incluyó la opción para que el usuario pueda mover el robot manualmente con entradas desde teclado.
4. **Recompensas y castigos adicionales:**
- Penalización de -5 puntos si intenta moverse sin batería.
- Bonificación extra de +20 puntos si el robot llega al objetivo en menos de 5 movimientos.
5. **Sistema de puntuación mejorado:** El robot acumula puntos según sus acciones para reflejar un entorno de recompensas.

