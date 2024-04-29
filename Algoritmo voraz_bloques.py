class Proceso:
    def __init__(self, id_proceso, tamano):
        self.id_proceso = id_proceso
        self.tamano = tamano

class BloqueMemoria:
    def __init__(self, id_bloque, capacidad):
        self.id_bloque = id_bloque
        self.capacidad = capacidad
        self.memoria_disponible = capacidad

def asignar_procesos(procesos, bloques):
    procesos_ordenados = sorted(procesos, key=lambda x: x.tamano, reverse=True)
    for proceso in procesos_ordenados:
        for bloque in bloques:
            if bloque.memoria_disponible >= proceso.tamano:
                bloque.memoria_disponible -= proceso.tamano
                break

    print("Asignación de procesos a bloques:")
    for bloque in bloques:
        memoria_utilizada = bloque.capacidad - bloque.memoria_disponible
        print(f"Bloque {bloque.id_bloque}: {memoria_utilizada} MB utilizados")

# Crear procesos y bloques de memoria
procesos = [
    Proceso(1, 212),
    Proceso(2, 417),
    Proceso(3, 112),
    Proceso(4, 426)
]

bloques = [
    BloqueMemoria(1, 100),
    BloqueMemoria(2, 500),
    BloqueMemoria(3, 200),
    BloqueMemoria(4, 300),
    BloqueMemoria(5, 600)
]

# Asignar procesos a bloques de memoria
asignar_procesos(procesos, bloques)


"""class Proceso:
    def __init__(self, id_proceso, tamano):
        self.id_proceso = id_proceso
        self.tamano = tamano

class BloqueMemoria:
    def __init__(self, id_bloque, capacidad):
        self.id_bloque = id_bloque
        self.capacidad = capacidad
        self.memoria_disponible = capacidad

def asignar_procesos(procesos, bloques):
    procesos_ordenados = sorted(procesos, key=lambda x: x.tamano, reverse=True)
    for proceso in procesos_ordenados:
        for bloque in bloques:
            if bloque.memoria_disponible >= proceso.tamano:
                bloque.memoria_disponible -= proceso.tamano
                break

    print("Asignación de procesos a bloques:")
    for bloque in bloques:
        memoria_utilizada = bloque.capacidad - bloque.memoria_disponible
        print(f"Bloque {bloque.id_bloque}: {memoria_utilizada} MB utilizados")

# Crear procesos y bloques de memoria
procesos = [
    Proceso(1, 350),
    Proceso(2, 500),
    Proceso(3, 50),
    Proceso(4, 470)
]

bloques = [
    BloqueMemoria(1, 100),
    BloqueMemoria(2, 500),
    BloqueMemoria(3, 200),
    BloqueMemoria(4, 300),
    BloqueMemoria(5, 600)
]

# Asignar procesos a bloques de memoria
asignar_procesos(procesos, bloques)"""
