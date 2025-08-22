print('------------------------')
print('Diego Rivera')
print('USTR018824')
print('------------------------')

# crear la funcion
def evaluar_numero(num):
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "cero"

# solicitar el numero
num = int(input("Introduce un número: "))

# imprimir el resultado
print(f"El número {num} es {evaluar_numero(num)}")
