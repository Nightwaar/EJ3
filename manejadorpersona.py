from clasepersona import persona
class manper:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def carga(self,nombre,direccion,dni):
        nombre=input("Ingrese nombre")
        direccion=input("Ingrese direccion")
        dni=input("Ingrese dni")
        self.__lista.append(persona(nombre,direccion,dni))
        persona=persona(nombre,direccion,dni)
        return persona