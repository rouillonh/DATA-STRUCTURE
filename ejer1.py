n = int(input("Ingrese un número: "))
suma = 0
for i in range(1,n+1):
    if i%7==0 or i%8==0:
        suma += i
print("La suma de todos los valores que cumplen es: ",suma)