#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t1 = input().split()
t2 = input().split()
aux = tuple(t2) + tuple(t1) + tuple(t2)
tup = []
for i in list(aux):
    try:
        tup.append(int(i))
    except:
        tup.append(i)

print(tuple(tup))
