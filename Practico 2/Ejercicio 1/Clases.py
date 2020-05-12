import re

class Email:
    def __init__(self, idCuenta = '', dom = '', tipDom = '', contr = ''):
        self.__idCuenta = idCuenta
        self.__dom = dom
        self.__tipDom = tipDom
        self.__contr = contr
        pass

    def retornaEmail(self):
        return(self.__idCuenta + '@' + self.__dom + '.' + self.__tipDom)
    
    def getDominio(self):
        return(self.__dom)

    def confir_contr(self, contr = ''):
        if(contr != self.__contr):
            return(-1)
        else:
            pass

    def cambiar_contr(self, nueva = ''):
        self.__contr = nueva
        pass
    
    def crearCuenta(self, correo = '', contraseña = ''):
        if((correo.find('@') == -1) or (correo.find('.') == -1) or (correo.find('@') > correo.find('.'))):
            print("Error: CORREO NO VÁLIDO")
            return(-1)
        elif (not contraseña) or (contraseña == ' '):
            print("ERROR: La contraseña no puede estar vacia")
            return(-1)
        else:
            a, b = correo.split('@')
            b, c = b.split('.', 1)
            self.__idCuenta = a
            self.__dom = b
            self.__tipDom = c
            self.__contr = contraseña
            pass  
