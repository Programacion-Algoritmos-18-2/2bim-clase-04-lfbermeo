class Equipo(object):
    """
    """
    
    def __init__(self, n, ciu, cam, num):
        """
        """
        #declaro mis variables a utilizar
        self.nombres = n
        self.ciudad = ciu
        self.campeonatos = int(cam)
        self.numJugadores = int(num)
        #Metodos obtener y agregar para cada una de las variables 
    def agregarNombres(self, n):
        """
        """
        self.nombres = n

    def obtenerNombres(self):
        """
        """
        return self.nombres

    def agregarCiudad(self, n):
        """
        """
        self.ciudad = n

    def obtenerCiudad(self):
        """
        """
        return self.ciudad
    
    def agregarCampeonatos(self, n):
        """
        """
        self.campeonatos = int(n)

    def obtenerCampeonatos(self):
        """
        """
        return self.campeonatos
   
    def agregarnumJugadores(self, n):
        """
        """
        self.numJugadores = int(n)

    def obtenernumJugadores(self):
        """
        """
        return self.numJugadores
    #Realizo la impresión 
    def __str__(self):
        """
        """
        return "%s %s %s %d" % (self.obtenerNombres(), self.obtenerCiudad(),\
                self.obtenerCampeonatos(), self.obtenernumJugadores())
    def __repr__(self):
        """
        """
        return "%s %s %s %d" % (self.obtenerNombres(), self.obtenerCiudad(),\
                self.obtenerCampeonatos(), self.obtenernumJugadores())

class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipo = listado
        #Realizo estas dons funciones dependiendo de lo que le usurio desea
    def ordenarNombres(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_equipo, key=lambda equipo: equipo.obtenerNombres())          
    def ordenarCampeonatos(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_equipo, key=lambda equipo: equipo.obtenerCampeonatos())     