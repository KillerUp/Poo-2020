class ManejadorHelados(object):
    #Variables de instancia
    __helados = []

    #Metodos de instancia
    def __init__(self):
        self.__helados = []

    def agregarHelado(self, helado):
        self.__helados.append(helado)
    
    def contarSabores(self):
        for helado in self.__helados: #Para cada helado pedido
            for sabor in helado.getSabores(): #para cada sabor de helado pedido
                sabor.contarPedido() #+1 a la cantidad de veces que se pidio ese sabor
    
    def pesoEstimado(self,num_sabor):
        acum = 0
        for helado in self.__helados: #Para cada helado
            lista = helado.getSabores() #Sabores por cada helado
            peso = int(helado.getTipo()) // int(helado.cantidadSabores())  #Peso estimado de cada sabor por helado

            for sabor in lista: #Para cada sabor
                if num_sabor == sabor.getId(): #Verifica que el sabor este en el helado
                    acum+=peso
        return acum

    def saboresVendidos(self, tipo):
        lista = []
        for helado in self.__helados: #Para cada helado
            if helado.getTipo() == tipo:
                lista_sabores = helado.getSabores() #Sabores por helado
                for sabor in lista_sabores:
                    if lista.count(sabor) == 0: #Verifica que ese sabor no este ya en la lista
                        lista.append(sabor)
        return lista


            

