


class Modulo:
    def __init__(self, lista):
        self.lista = lista


    def _es_primo(self, n):
        resultado = True
        if n < 2:
            resultado = False
        i = 2
        while i*i <= n:
            if n % i == 0:
                resultado = False
            i += 1
        return resultado
    
    def _conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def _factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser positivo'
        if (numero > 1):
            numero = numero * self._factorial(numero - 1)
        return numero

    
    def es_primo(self):
        lista_final = []
        for i in self.lista:
            if self._es_primo(i):
                
                lista_final.append(i)
        print(lista_final)
        return lista_final
    

    def mas_repetido(self):
        copia_lista = self.lista
        repetidos = []
        no_repetidos = []
        mas_repetidos = []
        if len(self.lista) == 0:
            return None
        for i in copia_lista:
            cantidad = copia_lista.count(i)
            if cantidad > 1:
                """ print(f"el numero {i} se repitio, y debe ser agregado a la lista de repetidos") """
                repetidos.append(i)
            else:
                """ print(f"el numero {i} no se repitio y debe ser agregado a la lista de no repetidos") """
                no_repetidos.append(i)


        for i in repetidos:
            """ indice = repetidos.index(i) """
            mas_repetidos.append(repetidos.count(i))
            """ print(mas_repetidos)
            print(f"el indice del elemento es {indice}") """
            moda = max(mas_repetidos)
        

        """ print(repetidos) """
        
        repetidos_sin_duplicados = set(repetidos)
        repetidos = list(repetidos_sin_duplicados)

        return print(f"Los valores que se repiten son {repetidos} y el/los mas común/es se repite/n {moda} veces")
    

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self._conversion_grados(i, origen, destino),'grados',destino)

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self._factorial(i))