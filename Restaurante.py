import random
import threading
import time

#Variables requeridas para el funcionamiento del programa/Restaurante
Platillos = ["Plato_Entrada","Plato_Fuerte","Bebida","Postre"]
Cubiertos = ["CUCHARA","TENEDOR","CUCHILLO","CUCHARA_POSTRE"]
Cant_Cucharas = 4
Cant_Tenedores = 3
Cant_Cuchillos = 4
Cant_Cucharas_Postre =3


#FUNCIONES DE UTILIDAD Y LEGIBILIDAD DE CODIGO :> CLEAN CODE
def Tomar_Tenedor():
    global Cant_Tenedores
    Cant_Tenedores-=1

def Tomar_Cuchara():
    global Cant_Cucharas
    Cant_Cucharas-=1

def Tomar_Cuchara_Postre():
    global Cant_Cucharas_Postre
    Cant_Cucharas_Postre-=1

def Tomar_Cuchillo():
    global Cant_Cuchillos
    Cant_Cuchillos-=1

def Habilitar_Tenedor():
    global Cant_Tenedores
    Cant_Tenedores+=1

def Habilitar_Cuchara():
    global Cant_Cucharas
    Cant_Cucharas+=1

def Habilitar_Cuchara_Postre():
    global Cant_Cucharas_Postre
    Cant_Cucharas_Postre+=1

def Habilitar_Cuchillo():
    global Cant_Cuchillos
    Cant_Cuchillos+=1

def Tomar_Orden():
    Orden= {Platillos[0]: random.randint(0,3),Platillos[1]: random.randint(0,3),Platillos[2]: random.randint(0,3),Platillos[3]: random.randint(0,3)}
    return Orden

def Disponible(Cubierto):
    match( Cubierto):
        case "CUCHARA":
            return Cant_Cucharas>0
        case "TENEDOR":
            return Cant_Tenedores>0
        case "CUCHILLO":
            return Cant_Cuchillos>0
        case "CUCHARA_POSTRE":
            return Cant_Cucharas_Postre>0
        case _:
            print("Cubierto INVALIDO")
            return False

def Despachar_Orden(Orden, Nombre):

    #Orden Para limpiar los cubiertos
    Orden_Limpieza = dict(Orden)

    while(Orden[Platillos[0]]>0):
        if(Disponible(Cubiertos[0])):
            Tomar_Cuchara()
            Orden[Platillos[0]]-=1
            print("\nENTRADA SERVIDA PARA "+Nombre, end='')
            time.sleep(1)
            
    while(Orden[Platillos[1]]>0):
        if(Disponible(Cubiertos[1]) and Disponible(Cubiertos[2])):
            Tomar_Tenedor()
            Tomar_Cuchillo()
            Orden[Platillos[1]]-=1
            print("\nPLATO FUERTE SERVIDO PARA "+Nombre, end='')
            time.sleep(1)
            
    while(Orden[Platillos[2]]>0):
        Orden[Platillos[2]]-=1
        print("\nBEBIDA SERVIDA PARA "+Nombre, end='')
        time.sleep(1)
    while(Orden[Platillos[3]]>0):
        if(Disponible(Cubiertos[3])):
            Orden[Platillos[3]]-=1
            Tomar_Cuchara_Postre()
            print("\nPOSTRE SERVIDO PARA "+Nombre, end='')
            time.sleep(1)
            
    #Simulando Tiempo de Ingesta de alimento
    print("\n"+Nombre+" ESTA COMIENDO...", end='')
    time.sleep(Orden_Limpieza[Platillos[0]]+Orden_Limpieza[Platillos[1]]+Orden_Limpieza[Platillos[2]]+Orden_Limpieza[Platillos[3]])
    print("\nLIMPIANDO CUBIERTOS DE "+Nombre+" ...", end='')
    
    
    #proceso de limpieza y liberacion de recursos MUTEX
    while(Orden_Limpieza[Platillos[0]]>0):
            Habilitar_Cuchara()
            Orden_Limpieza[Platillos[0]]-=1
            time.sleep(1)
            
    while(Orden_Limpieza[Platillos[1]]>0 and Orden_Limpieza[Platillos[2]]>0):
            Habilitar_Tenedor()
            Habilitar_Cuchillo()
            Orden_Limpieza[Platillos[1]]-=1
            time.sleep(1)
            
    while(Orden_Limpieza[Platillos[3]]>0):
            Habilitar_Cuchara_Postre()
            Orden_Limpieza[Platillos[3]]-=1
            time.sleep(1)
    print("\nSERVICIO DE "+Nombre+" COMPLETADO", end='')

#Programa de Restaurante
OrdenA = Tomar_Orden()
print(OrdenA)
OrdenB = Tomar_Orden()
print(OrdenB)
    
Linea_DespachoA = threading.Thread(target=Despachar_Orden, args=(OrdenA,"Luis"))
Linea_DespachoB = threading.Thread(target=Despachar_Orden, args=(OrdenB,"Miguel"))

Linea_DespachoA.start()
Linea_DespachoB.start()
















