from claseinscripcion import inscripcion
import csv
class TallerCapacitacion:
    __idTaller= int('0')
    __nombre=''
    __vacantes=int('0')
    __montoincriptos=int('0')
    __inscripcion=list
    __numinscripto=0
    def __init__(self,id,nombre,vacantes,monto):
        self.__idTaller=int(id)
        self.__nombre=nombre
        self.__vacantes=int(vacantes)
        self.__montoincriptos=int(monto)
        self.__inscripcion=[]
    def __str__(self):
        return f"ID: {self.__idTaller} Nombre:{self.__nombre} Vacantes:{self.__vacantes} Monto:{self.__vacantes}"
    @classmethod
    def getnuminscripto(cls):
        cls.__numinscripto+=1
        return cls.__numinscripto
    def idtaller(self):
        return self.__idTaller
    def nombretaller(self):
        return self.__nombre
    def monto(self):
        return self.__montoincriptos
    # def inscribir(self,persona,fecha):
    #     id=int(input("Ingrese el nombre del taller"))
    #     idtaller()
    #     taller=self.idtaller()
    #     pago=self.pago()
    #     inscripcion= inscripcion(fecha,pago,persona,taller)