#esto es un comentario

def suma_arreglos(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        raise ValueError("Los arreglos deben tener la misma longitud")
    
    resultado = [a + b for a, b in zip(arreglo1, arreglo2)]
    return resultado

def main():
    print("Aplicacion para la suma de dos arreglos")
    
    try:
        tamanio = int(input("Ingrese el tamano de los arreglos: "))
        
        arreglo1 = []
        arreglo2 = []

        print("Ingrese los elementos del primer arreglo:")
        for i in range(tamanio):
            valor = float(input(f"Elemento {i+1}: "))
            arreglo1.append(valor)

        print("Ingrese los elementos del segundo arreglo:")
        for i in range(tamanio):
            valor = float(input(f"Elemento {i+1}: "))
            arreglo2.append(valor)

        resultado = suma_arreglos(arreglo1, arreglo2)
        print("Resultado de la suma de los arreglos:", resultado)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)

if __name__ == "__main__":
    main()
