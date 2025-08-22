entrada = input ("Ingrese números separados por coma: ")

try:
    # convertir la entrada en lista de numeros
    numeros = [float(num) for num in entrada.split(',')]

    if not numeros:
        print("no se ingresaron numeros.")
    else:
        mayor = max(numeros)
        print(f"el mayor numero ingresado es: {mayor}")
except ValueError:
    print("por favor, ingrese solo numeros separados por coma.")