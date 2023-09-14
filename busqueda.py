#Hecho por Antonio Valdés Hernández
import time

inicio = time.time()
def lineal(arr, x):
    for i in range(len(arr)):
            if arr[i] == x:
                print("El elemento ",x," se encontró en la posición ", i)
                return
    print("Dato no encontrado D:")


def burbuja_opt(arr):
    n = len(arr)
    xd = True
    while xd:
        xd = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                xd = True
        n -= 1
    print("Arreglo ordenado:", arr)

def binaria(arr, x):
    ini= 0
    finuwu = len(arr)-1
    while ini <= finuwu:
        medio = (ini+finuwu)//2

        if arr[medio] == x:
            print("El elemento ",x," se encontró en la posición: ",medio)
            return
        elif arr[medio] > x:
            finuwu = medio-1
        else:
            ini = medio+1
        
    print("Dato no encontrado D: ")


def main():
    print("Seleccione un método de búsqueda:")
    print("1] Búsqueda Lineal")
    print("2] Búsqueda Binaria")
    
    elec = int(input())
    
    if elec not in [1, 2]:
        print("Opción inválida")
        return
    
    tam = int(input("Ingrese el tamaño de la lista: "))
    
    x = int(input("Ingrese el dato a buscar: "))

    arr = []
    for i in range(tam):
        dato = int(input("Ingrese el elemento :" ))
        arr.append(dato)
    
    if elec == 1:
        lineal(arr, x)
    elif elec == 2:
        burbuja_opt(arr)  
        binaria(arr, x)

if __name__ == "__main__":
    main()

fin = time.time()
print("Tiempo transcurrido:", fin - inicio)
