#Mini Calculadora

print("=== Mini Calculadora ===")
print("Opciones disponibles:")
print("1. suma")
print("2. resta")
print("3. multi")
print("4. divi")

operacion = input("ingresa la operacion que desees: ")


x = float(input("Ingrese num1: "))
y = float(input("Ingrese num2: "))

if operacion == "suma":
    print("Resultado:", x + y)
elif operacion == "resta":
    print("Resultado:", x - y)
elif operacion == "multi":
    print("Resultado:", x * y)
elif operacion == "divi":
    if y != 0:
        print("Resultado:", x / y)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("No existe esa operación en mi código")