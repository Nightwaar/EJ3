from arreglotaller import talleres
from claseinscripcion import inscripcion
from clasepersona import persona
from clasetaller import TallerCapacitacion
from manejadorpersona import manper
from arregloinscripcion import inscripciones

if __name__=='__main__':
    listatalleres=talleres
    talleres.cargar()
    personas=manper
    listainscripciones=inscripciones
    print("""
1.Inscribir persona
2.Consultar inscripcion
3.Consultar inscriptos
4.Registrar pago
5.Guardar inscripciones""")
    opc=int(input("Ingrese opcion"))
    while opc<6:
        match opc:
            case 1:
                agregar=personas.carga()
                listatalleres.agregarTaller()
            case 2:
                dni=input("Ingrese dni")
                personas.buscardni(dni)
            case 3:
                nombretaller=input("Ingrese nombre de taller")
                listatalleres.listar(nombretaller)
            case 5:
                