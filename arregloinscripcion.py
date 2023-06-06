import csv
import numpy as np
from claseinscripcion import inscripcion
import json
class inscripciones():
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__listains = np.empty(dimension, dtype=inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarInscripcion(self, inscripcion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listains.resize(self.__dimension)
        self.__listains[self.__cantidad]=inscripcion
        self.__cantidad += 1
    def buscarpersona(self,dni):
        bandera=False
        i=0
        while bandera!=True and i<len(self.__listains):
            if dni == self.__listains[i].dni():
                print("El taller es: {}".format(self.__listains[i].nombretaller()))
                print(f"El monto que adeuda es: {self.__listains[i].montopago()}")
            i+=1
    def listar(self,nombre,personas,inscripciones):
        for i in range(len(self.__listains)):
            if self.__listains.nombretaller() == nombre:
                print(self.__listains[i].persona())