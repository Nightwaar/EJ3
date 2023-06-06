from datetime import date
from clasepersona import persona
from clasetaller import TallerCapacitacion

class inscripcion:
    __fechainscripcion= date.now()
    __pago=bool
    __montopago=int
    __persona=object
    __taller=object
    def __init__(self,fecha,pago,persona,TallerCapacitacion):
        self.__fechainscripcion=fecha
        self.__pago=pago
        self.__persona=persona
        self.__taller=TallerCapacitacion
    def pago(self,pago):
        if pago==TallerCapacitacion.monto():
            return True
    def montopago(self):
        return self.__montopago
    