from paquete_archivos.archivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.modelo import Equipo, Operaciones
#creo los objetos para que lean los archivos y lo vuelva a sobreescribir ya ordenado el archivo
m = MiArchivo()
m2= MiArchivoEscribir()
lista = m.obtener_informacion()
#no se debe imprimir "|" este caracter 
lista = [l.split("|") for l in lista]
#Creo esta lista
lista_equipo= []

for d in lista:
    e = Equipo(d[0], d[1], d[2], d[3])
    #agrego los atributos a la lista que cree
    lista_equipo.append(e)
#Creo el objeto donde envió la lista
operacion = Operaciones(lista_equipo)
#Realizo la pregunta al usuario para la opcion que desea    
opcion = input("Si desea ordenar por nombres presione 1 o si desea ordenar por campeonatos presione 2: ")
#Se realiza la comparacion
if opcion== 1:
	lista_ordenada=operacion.ordenarNombres()
else:
	lista_ordenada=operacion.ordenarCampeonatos()
#Se agrega la información
for d in lista_ordenada:
	m2.agregar_informacion(d)
	print(d)
#Cierran los archivos
m.cerrar_archivo()
m2.cerrar_archivo()