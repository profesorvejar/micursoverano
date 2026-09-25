cantidad = int(input("¿Cuántas notas quieres ingresar? "))
suma = 0
nota_maxima = 0
nota_minima = 10
for i in range(1, cantidad + 1):
    nota = float(input(f" Nota {i}: "))
    suma += nota
    if nota > nota_maxima:
        nota_maxima = nota
    if nota < nota_minima:
        nota_minima = nota
promedio = suma / cantidad
print(f" Notas ingresadas: {cantidad}")
print(f" Nota más alta:    {nota_maxima:.1f}")
print(f" Nota más baja:    {nota_minima:.1f}")
print(f" PROMEDIO: {promedio:.2f}")     
print(f" Estado: {'Aprobado ' if promedio >= 6 else 'Reprobado '}")