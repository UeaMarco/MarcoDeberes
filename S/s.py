import threading
# Definimos una variable global compartida
contador_global = 1

# Creamos un objeto mutex
mutex = threading.Lock()
# Función que incrementa el contador global de forma segura utilizando un mutex
def incrementar():
 global contador_global
 # Adquirimos el mutex
 mutex.acquire()
 try:
 # Sección crítica: Incrementamos el contador
 contador_global += 1
 finally:
 # Liberamos el mutex
 mutex.release()
# Función que ejecuta la tarea de incrementar el contador un número determinado de veces
def tarea():
 for _ in range(100000):
 incrementar()
# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
# Iniciamos los hilos
hilo1.start()
hilo2.start()
# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()
# Imprimimos el valor final del contador global
Página 2 de 3
print("El valor final del contador global es:", contador_global)