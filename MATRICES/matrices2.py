suma = 0
PAISES = 14
DATOS = 6
paises = [ "Costa Rica", "Argentina", "Panamá", "Chile", "Uruguay",
    "Paraguay", "Colombia", "Peru", "Ecuador","Bolivia","Brasil",
    "México","Nicaragua","Venezuela"]
datos = [ [2290, 569, 4 , 300255, 527.7, 131],  [75, 22.8, 3.3, 9500, 416.7, 127],
          [5.9, 1, 5.9, 744, 744, 126], [2600, 634, 4.1, 276000, 435.3, 106],
          [140, 30.8, 4.5, 13430, 436, 96],[26542, 5601,4.7, 2200000, 392.8, 83],
          [10900, 2964, 3.7, 869453, 293.3, 80], [11.5, 3.3, 3.5, 850, 257.6, 74],
          [5.5, 1, 5.5, 386, 386, 70], [34, 7, 4.9, 2000, 287.4, 59],
          [16.5, 3.6, 4.6, 965, 268.1, 58], [48, 19.6, 2.5, 2687, 137.2, 56],
          [168, 31.3, 5.4, 8445, 269.6, 50], [168000, 690854, 0.2, 1308000, 1.9, 8]]


for i in range(PAISES) :
  print("%10s"%paises[i], end="   ")
  for j in range(DATOS) :
    print("%12.2f" % (datos[i][j]), end= " ")
  print()
for i in range(len(datos)):
    suma += datos[i][5]
print("Suma total de BigMacs en LATAM: ",suma)
