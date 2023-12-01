"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}
CRITERIOS = {"nombre", "apellido", "email", "telefonos"}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            client = linea.split(";")
            nuev_cont = {}
            nuev_cont["nombre"] = client[0]
            nuev_cont["apellido"] = client[1]
            nuev_cont["email"] = client[2]
            list_tfno = []
            if (len(client) > 3):
                for tfno in client[3:]:
                    list_tfno.append(tfno)
                nuev_cont["telefonos"] = list_tfno
            contactos.append(nuev_cont)
                

def agregar_contacto(contactos: list):
    """Agrega contactos a la lista
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    """
    nuev_cont = {}
        
    nom = pedir_nombre()
    nuev_cont["nombre"] = nom
        
    ape = pedir_apellido()
    nuev_cont["apellido"] = ape
        
    email = pedir_email(contactos)
    nuev_cont["email"] = email
        
    lis_tfno = pedir_telefono()
    if (lis_tfno != None):
        nuev_cont["telefonos"] = lis_tfno
        
    contactos.append(nuev_cont)
                
            
        
        
    
def eliminar_contacto(contactos: list, email: str):
    """ Elimina un contacto de la agenda
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    email : str
        El email a usar para elegir el contacto específico.
    """
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos, email)
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def buscar_contacto(contactos: list, email: str) -> int:
    """Busca la posición de un contacto específico a través de su email.
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    email : str
        El email a usar para elegir el contacto específico.
        
    RETURNS
    -------
    pos : int
        La posición del contacto deseado.
    """
    
    pos = None
    for contacto in range(len(contactos)):
        if (contactos[contacto]["email"] == email):
            pos = contacto
    return pos


def modificar_contacto(contactos: list, email: str):
    """Modifica un contacto deseado, esspecificado por su email.
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    email : str
        El email a usar para elegir el contacto específico.
    """
    
    encontrado = False
    try:
        for contacto in range(len(contactos)):
            if (email == contactos[contacto]["email"]):
                encontrado = True
                crit = input("Introduce el dato del contacto que deseas modificar (nombre, apellido, email o telefono): ")
                if (crit.lower() in CRITERIOS):
                    if crit.lower() == "nombre":
                        nom = pedir_nombre()
                        contactos[contacto]["nombre"] = nom
                    if crit.lower() == "apellido":
                        ape = pedir_apellido()
                        contactos[contacto]["apellido"] = ape
                    if crit.lower() == "email":
                        mail = pedir_email(contactos)
                        contactos[contacto]["email"] = mail
                    if crit.lower() == "telefonos":
                        pos_tfno = input("Introduce la posición del teléfono que deseas modificar o introduce '+' para añadir uno nuevo: ")
                        if pos_tfno == "+":
                            tfno = input("Escribe el nuevo teléfono del contacto: ")
                            tfno = tfno.replace(" ", "")
                            if ("+34" in tfno):
                                if (len(tfno[3:] != 9)):
                                    raise ValueError
                                else:
                                    contactos[contacto]["telefonos"].append(tfno)
                            if (len(tfno) != 9):
                                raise ValueError
                            else:
                                contactos[contacto]["telefonos"].append(tfno)
                        else:
                            tfno = input("Escribe el nuevo teléfono del contacto: ")
                            tfno = tfno.replace(" ", "")
                            if ("+34" in tfno):
                                if (len(tfno[3:] != 9)):
                                    raise ValueError
                                else:
                                    contactos[contacto]["telefonos"] = tfno
                            if (len(tfno) != 9):
                                raise ValueError
                            else:
                                contactos[contacto]["telefonos"] = tfno                       
    except ValueError:
        print("Valor introducido no válido.")
                            
                        

def mostrar_contactos(contactos: list):
    """Muestra todos los contactos actuales en la agenda.
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    """
    
    print("AGENDA ({lencont})".format(lencont = len(contactos)))
    print("------")
    for contacto in range(len(contactos)):
        print("Nombre: {nom} {ape} ({email})".format(nom = contactos[contacto]["nombre"], ape = contactos[contacto]["apellido"], email = contactos[contacto]["email"]))
        if (len(contactos[contacto]) == 3):
            print("Teléfonos: Ninguno")
        else:
            ser = "Teléfonos: "
            for telefono in contactos[contacto]["telefonos"]:
                encontrar = ("+34" in telefono)
                if (encontrar == True):
                    telefono = "+34-" + telefono[3:]
                    ser += "{telefono} / ".format(telefono = telefono)
                else:
                    ser += "{telefono} / ".format(telefono = telefono)
            print(ser[:-3])
        print("......")
        
        
def pedir_nombre():
    """Pide un nombre que será introducido en el contacto.
    
    """
    
    nom = input("Escribe el nombre del contacto: ")
    if (nom == " " or nom == ""):
            raise ValueError
    nom = nom[:1].title() + nom[1:]
    return nom


def pedir_apellido():
    """Pide un apellido que será introducido en el contacto.
    
    """
    
    ape = input("Escribe el apellido del contacto: ")
    if (ape == " " or ape == ""):
        raise ValueError
    ape = ape[:1].title() + ape[1:]
    return ape


def pedir_email(contactos_iniciales: list):
    """Pide un email que será introducido en el contacto.
    
    PARAMETERS
    ----------
    contactos_iniciales : list
        La lista de contactos introducida inicialmente
    """
    
    email = input("Escribe el email del contacto: ")
    if (email.lower() in contactos_iniciales):
        raise ValueError("el email ya existe en la agenda")
    elif (email == ""):
        raise ValueError("el email no puede ser una cadena vacía")
    elif ("@" not in email):
        raise ValueError("el email no es un correo válido")
    else:
        return email


def validar_email(contactos_iniciales: list, email: str):
    """Se asegura de que el email introducido es correcto
    
    PARAMETERS
    ----------
    contactos_iniciales : list
        La lista de contactos introducida inicialmente
    email : str
        El email que será validado.
    """
    
    if (email.lower() in contactos_iniciales):
        raise ValueError("el email ya existe en la agenda")
    elif (email == ""):
        raise ValueError("el email no puede ser una cadena vacía")
    elif ("@" not in email):
        raise ValueError("el email no es un correo válido")
        
        
def pedir_telefono():
    """Pide el teléfono a introducir en el contacto.
    
    """
    
    tfno = "x"
    lis_tfno = []
    while (tfno != ""):
        tfno = input("Escribe el teléfono del contacto: ")
        if (tfno != ""):
            tfno = tfno.replace(" ", "")
            validar_telefono(tfno)
            lis_tfno.append(tfno)
    return lis_tfno        
        
        
def validar_telefono(input_tel: str):
    """Se asegura de que el telefono introducido es correcto.
    
    PARAMETERS
    ----------
    input_tel : str
        El telefono introducido que será validado.
    """
    
    encontrar = ("+34" in input_tel)
    if (encontrar == True):
        if (len(input_tel[3:]) != 9):
            raise ValueError("Longitud teléfono incorrecta.") 
    elif (len(input_tel) != 9):
            raise ValueError("Longitud teléfono incorrecta.")

        


        
def mostrar_menu():
    """Muestra el menú de la agenda
    
    """
    
    print("AGENDA")
    print("------")
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir")
    print("")
    

def pedir_opcion():
    """Solicita la opción del menú de la agenda a elegir.
    
    """
    
    try:
        opcion = int(input(">> Seleccione una opción: "))
        if (type(opcion) != int):
            raise ValueError
        elif (opcion not in OPCIONES_MENU):
            raise NameError
        else:
            return opcion
    except ValueError:
        print("**ERROR** Tipo de valor no válido.")
    except NameError:
        print("**ERROR** Opción elegida no válida.")
    


def buscar_por_criterio(contactos: list, crit: str):
    """Busca un contacto específico de la agenda a través de un criterio previamente elegido.
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    crit : str
        El criterio elegido para buscar el contacto.
    """
    
    if crit.lower() == "nombre":
        nom = input("Introduce el nombre del cliente a buscar: ")
        for contacto in range(len(contactos)):
            if contactos[contacto]["nombre"] == nom:
                print("Nombre: {nom} {ape} ({email})".format(nom = contactos[contacto]["nombre"], ape = contactos[contacto]["apellido"], email = contactos[contacto]["email"]))
                if (contactos[contacto]["telefonos"] == None):
                    print("Teléfonos: Ninguno")
                else:
                    print("Teléfonos: {tfno}".format(tfno = (" / ".join(contactos[contacto]["telefonos"]))))
                print("......")
    if crit.lower() == "apellido":
        ape = input("Introduce el apellido del cliente a buscar: ")
        for contacto in range(len(contactos)):
            if contactos[contacto]["apellido"] == ape:
                print("Nombre: {nom} {ape} ({email})".format(nom = contactos[contacto]["nombre"], ape = contactos[contacto]["apellido"], email = contactos[contacto]["email"]))
                if (contactos[contacto]["telefonos"] == None):
                    print("Teléfonos: Ninguno")
                else:
                    print("Teléfonos: {tfno}".format(tfno = (" / ".join(contactos[contacto]["telefonos"]))))
                print("......")
    if crit.lower() == "email":
        email = input("Introduce el email del cliente a buscar: ")
        for contacto in range(len(contactos)):
            if contactos[contacto]["email"] == email:
                print("Nombre: {nom} {ape} ({email})".format(nom = contactos[contacto]["nombre"], ape = contactos[contacto]["apellido"], email = contactos[contacto]["email"]))
                if (contactos[contacto]["telefonos"] == None):
                    print("Teléfonos: Ninguno")
                else:
                    print("Teléfonos: {tfno}".format(tfno = (" / ".join(contactos[contacto]["telefonos"]))))
                print("......")
    if crit.lower() == "telefonos":
        tfno = input("Introduce el teléfono del cliente a buscar: ")
        for contacto in range(len(contactos)):
            for telefono in range(len(contactos[contacto]["telefonos"])):
                if contactos[contacto]["telefonos"][telefono] == tfno:
                    print("Nombre: {nom} {ape} ({email})".format(nom = contactos[contacto]["nombre"], ape = contactos[contacto]["apellido"], email = contactos[contacto]["email"]))
                    if (len(contactos[contacto]) == 3):
                        print("Teléfonos: Ninguno")
                    else:
                        ser = "Teléfonos: "
                        for telefono in contactos[contacto]["telefonos"]:
                            encontrar = ("+34" in telefono)
                            if (encontrar == True):
                                telefono = "+34-" + telefono[3:]
                                ser += "{telefono} / ".format(telefono = telefono)
                            else:
                                ser += "{telefono} / ".format(telefono = telefono)
                        print(ser[:-3])
                    print("......")


def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones.
    
    PARAMETERS
    ----------
    contactos : list
        Lista de los contactos actuales.
    """
    
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    opcion = None
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        salida = {8}
        OPCIONES_MENU.discard(salida)
        if opcion in OPCIONES_MENU:
            if opcion == 1:
                agregar_contacto(contactos)
            elif opcion == 2:
                email = input("Introduce el email del contacto que deseas modificar: ")
                modificar_contacto(contactos, email)
            elif opcion == 3:
                email = input("Introduce el email del contacto que deseas eliminar: ")
                eliminar_contacto(contactos, email)
            elif opcion == 4:
                contactos.clear()
                print("Agenda vaciada.")
            elif opcion == 5:
                contactos.clear()
                cargar_contactos(contactos)
                print("Agenda devuelta a su estado inicial.")
            elif opcion == 6:
                crit = input("Introduce el criterio por el que deseas buscar (nombre, apellido, email o telefonos): ")
                if (crit.lower() in CRITERIOS):
                    buscar_por_criterio(contactos, crit)
                else:
                    print("Criterio no válido.")
            elif opcion == 7:
                mostrar_contactos(contactos)



def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla.
    
    """
    print("\n")
    os.system("pause")


def main():
    """ Función principal del programa.
    
    """
    borrar_consola()

    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = []

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
    cargar_contactos(contactos)

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    email = "rciruelo@gmail.com"
    eliminar_contacto(contactos, email)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    agenda(contactos)


if __name__ == "__main__":
    main()