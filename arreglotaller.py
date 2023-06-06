import csv
import numpy as np
from clasetaller import TallerCapacitacion
class talleres():
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__talleres = np.empty(dimension, dtype=TallerCapacitacion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarTaller(self, taller):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__talleres.resize(self.__dimension)
        self.__talleres[self.__cantidad]=taller
        self.__cantidad += 1
    def gettalleres(self, indice):
        return self.__talleres[indice]
    def mostrarTalleres(self):
        for i in range(self.__cantidad):
            print(self.__talleres[i])
    def cargar(self,nomArch="talleres.csv"):
        archivo=open(nomArch)
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.agregarTaller(TallerCapacitacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
    def buscarid(self,nombre):
        bandera=False
        i=0
        while bandera!=True and i<len(self.__talleres):
            if nombre==self.__talleres[i].nombretaller():
                return i
            i+=1
    def inscribir(self,persona,fecha,inscripciones):
        nombre=int(input("Ingrese el nombre del taller"))
        idtaller=self.buscarid(id)
        pago=int(input("Ingrese el monto que pago"))
        if pago>0:
            boolpago=True
        else:
            boolpago:False
        inscripcion= inscripcion(fecha,boolpago,pago,persona,idtaller)
        inscripciones.agregarInscripciones(inscripcion)
#     def listar(self,nombre,personas,inscripciones):
#         for i in range(len(self.__talleres)):
#             if self.__talleres.nombretaller() == nombre:
#                 print(f"""
# Nombre: {self})