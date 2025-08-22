print ("---------------------------------")
print("lista - sumar todos")
print ("---------------------------------")
#solicitar un numero final de la lista
num1=int(input("ingrese un numero hasta 100"))

#crea la lista desde 1 hasta el num1
lista = list(range(1, num1+1))

#calcular la suma
resultante=sum(lista)

#imprimir el resultado
print(f"la suma de la lista hasta {num1} es {resultante}")