from paquete_archivos.archivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.modelo import Equipo, Operaciones

m = MiArchivo()
m2= MiArchivoEscribir()
lista = m.obtener_informacion()
#no se debe imprimir "|" este caracter 
lista = [l.split("|") for l in lista]

lista_equipo= []

for d in lista:
    e = Equipo(d[0], d[1], d[2], d[3])
    lista_equipo.append(e)

operacion = Operaciones(lista_equipo)
    
opcion = input("Si desea ordenar por nombres presione Nombres o si desea ordenar por campeonatos presione Campeonatos: ")
if opcion=='nombres':
	lista_ordenada=operacion.ordenarNombres()
else:
	lista_ordenada=operacion.ordenarCampeonatos()

for d in lista_ordenada:
	m2.agregar_informacion(d)
	print(d)

m.cerrar_archivo()
m2.cerrar_archivo()