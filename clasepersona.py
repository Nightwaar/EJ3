class persona:
    __nombre=''
    __direccion=''
    __dni=''
    def __init__(self,nombre,direccion,dni):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__dni=dni
    def persona(self):
        return f"Nombre: {self.__nombre} Direccion: {self.__direccion} Dni: {self.__dni}"
    def dni(self):
        return self.__dni