import codecs
import sys

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        #"data..."hace referencia la ruta del archico y con "r" lo lee
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        #readlines retorna los valores de archivo y las corre
        return self.archivo.readlines()

    def cerrar_archivo(self):
        #cierra el programa
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion_ordenada.csv", "a")
        #Se imprime la infrmacion
    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%s-%d\n" % (p.obtenerNombres(), p.obtenerCiudad(),\
                p.obtenerCampeonatos(), p.obtenernumJugadores()))

    def cerrar_archivo(self):
        self.archivo.close()
