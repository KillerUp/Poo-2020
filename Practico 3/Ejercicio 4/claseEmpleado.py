class Empleado(object):
    __dni = ''
    __nombre = ''
    __direccion = ''
    __telefono = ''

    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def calculaSueldo(self):
        pass

    def getDni(self):
        return self.__dni

    def __eq__(self, otro):
        pass

    def __str__(self):
        cadena = 'Nombre: {}\nDireccion: {}\nDNI: {}\n'.format(self.__nombre, self.__direccion, self.__dni)
        return cadena
    
    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono