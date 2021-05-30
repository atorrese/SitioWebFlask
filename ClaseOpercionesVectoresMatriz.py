import random
class Operacion:
    def esPar(self, numero):
        return numero%2== 0
    
    def productoDosnumeros(self,numero1,numero2):
        return numero1*numero2

    def mayorDosNumeros(self,numero1,numero2):
        return numero1 if  numero1 > numero2  else numero2


    def mayorTresNumeros(self,numero1,numero2,numero3):
        if numero1 > numero2 and  numero1 > numero3:
            return numero1
        elif numero2 > numero1 and numero2 > numero3:
            return numero2
        elif numero3 > numero1 and numero3 > numero2:
            return numero3

    def esMultiplo3(self,numero):
        return numero % 3 ==0

    def esMultiplo5(self, num):
        return num % 5 == 0

    def tablaMultiplicar(self, numero):
        cont=1
        tabla=''
        while(cont<=12):
            #print('{} * {} = {}'.format(cont,numero,(numero*cont)))
            tabla +='{} * {} = {}\n'.format(cont,numero,(numero*cont))
            cont +=1
        return tabla
    def secuencia30NumerosSumaProducto(self):
        suma = 0
        producto= 1
        for indice in range(1,31):
            numero=random.randrange(1,50)
            suma += numero
            producto *= numero
        return suma ,producto

    def secuenciaHastaNegativo(self):
        suma = 0
        while(True):
            numero= random.randrange(-15,50)
            print(numero)
            if numero <=0:
                break
            suma += numero
        return suma

    def productoXsuma(self,numero1,numero2):
        producto =0
        for num in range(numero1):
            producto += numero2
        return producto

    def divisionXresta(self,numero1,numero2):
        residuo = 0
        cociente = 0
        while numero1 >= numero2:
            numero1 -= numero2
            residuo +=1
        cociente = numero1
        return cociente, residuo

    def secuenciaHastaLetraF(self):
        producto = 1
        dicc = {0:'f'}
        while(True):
            numero= random.randrange(50)
            if not dicc.get(numero):
                producto *= numero
            else:
                break
        return producto

    def secuenciaHallarMayor(self,longitud):
        mayor = 0
        for i in range(0,longitud):
            numero=random.randrange(100)
            if numero > mayor:
                mayor = numero
        return mayor

    def secuenciaHayarMayorMenorHastaImpar(self):
        menor=0
        mayor = 0
        ban = 0
        lista=[]
        while(True):

            numero = random.randrange(50)
            lista.append(numero)
            if self.esPar(numero):
                if ban == 0:
                    ban += 1
                    menor = numero
                    mayor = numero
                if numero > mayor:
                    mayor = numero

                if numero < menor:
                    menor = numero
            else:
                break
        return mayor,menor,lista
    
    def secuenciaHastaLetraT(self):
        suma = 0
        contador =0
        dicc = {-1:'T'}
        while(True):
            numero= random.randrange(-1,50)
            if not dicc.get(numero):
                contador +=1
                suma += numero
            else:
                break
                    
        return suma/contador if suma > 0 else 0
    
    def secuenciaSumarPares(self,longitud):
        suma=0
        lista=[]
        for i in range(longitud):
            numero = random.randrange(50)
            lista.append(numero)
            if self.esPar(numero):
                suma +=numero
        return suma,lista

    def secuenciaSumar30Numeros(self,longitud):
        suma=0
        cont=0
        numeros  = [random.randrange(50)  for num in range(longitud)]
        for indice in range(len(numeros)):
            if self.esPar(indice) and cont < 30:
                suma += numeros[indice]
                cont +=1
        return suma,numeros

    def factorial(self, numero):
        fact=1
        for mult in range(1,numero+1):
            fact *=mult
        return fact if  numero > 0 else 0

    def esPrimo(self, numero):
        contador=0
        for n in range(1,numero+1):
            if numero % n == 0:
                contador +=1
        return contador == 2 

    def secuenciaSumar30sumaPrimos(self):
        secuencia= 30
        lista= []
        suma = 0
        for  num in range(secuencia):
            numero = random.randrange(50)
            lista.append(numero)
            if self.esPrimo(numero):
                suma +=numero
        return suma,lista

    def secuenciaSumar30sumaFactorial(self):
        secuencia= 30
        lista= []
        suma = 0
        for  num in range(secuencia):
            numero = random.randrange(50)
            lista.append(numero)
            suma += self.factorial(numero)
        return suma,lista

    def secuenciaMayorPares(self,longitud):
        secuencia= longitud
        lista= []
        mayor = 0
        for  num in range(secuencia):
            numero = random.randrange(50)
            lista.append(numero)
            if self.esPar(numero) and numero > mayor:
                mayor = int(numero)

        return mayor,lista

    def secuenciaSumaParesMultiplo5(self,secuencia):
        suma_pares = 0
        suma_multiplos5 =0
        lista=[]
        for  num in range(secuencia):
            numero = random.randrange(50)
            lista.append(numero)
            if self.esPar(numero):
                suma_pares += numero
            elif self.esMultiplo5(numero):
                suma_multiplos5 *= numero

        return suma_pares,suma_multiplos5,lista

    def secuenciaMayorMultiplo5MenorMultiplo3(self,secuencia):
        ban = 0
        menor = 0
        mayor =0
        lista =[]
        for  num in range(secuencia):
            numero =random.randrange(50)
            lista.append(numero)
            if self.esMultiplo3(numero):
                if ban ==0 :
                    menor = numero
                    ban +=1
                elif numero < menor:
                    menor = numero
            elif self.esMultiplo5(numero):
                if numero >mayor:
                    mayor = numero
        return mayor,menor,lista

    def decimalAbinario(self,numero):
    	binario=''
    	while numero != 0:
    		binario+= str(numero%2)
    		numero //=2
    	return binario[::-1]  

    def decimalAoctal(self,numero):
        octal=''
        while numero != 0:
            mod = numero%8
            octal+= str(mod)
            numero //=8
        return octal[::-1]  

    def decimalAhexadecimal(self,numero):
        hexadecimal=''
        hexadecimales={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while numero != 0:
            mod = numero%16
            hexadecimal+= hexadecimales[mod] if mod >9 else str(mod)
            numero //=2
        return hexadecimal[::-1]
    
    def contarPalabrasParrafo(self, parrafo):
        return len(parrafo.split())
    
    def extraerPalabras(self,parrafo):
        return parrafo.split()

    def palabraMayorTamañoParrafo(self, parrafo):
        palabras = self.extraerPalabras(parrafo)
        mayor =0
        max_palabra =''
        for palabra in palabras:
            longitud =len(palabra)
            if longitud >mayor:
                mayor=longitud
                max_palabra =palabra
        return max_palabra
        


 


class Vector(Operacion):
    
    def sumarVectores(self,vector_1, vector_2 ):
        vector_3=[]
        if len(vector_1)==len(vector_2):
            for i in range(len(vector_1)):
                vector_3.append(vector_1[i]+vector_2[i])
        return vector_3

    def sumarPosImparmayorPosPares(self,vector):
        mayor = 0
        suma = 0
        lista_mayor =[]
        for i,valor in enumerate(vector):
            if self.esPar(i):
                suma += valor#suma de pares
            else:
                if valor >= mayor:
                    mayor = valor
                    lista_mayor = [i,mayor]#  se crea una lista para saber posicion y numero mayor de impares
        return suma, lista_mayor

    def vectorNumeroMayor(self, vector):
        mayor = None
        indice= None
        if len(vector)>0:
            mayor = vector[0] 
            for i,valor in enumerate(vector):
                if valor >= mayor:
                    mayor =valor
                    indice =i
        return indice,mayor
    
    def vectorNumeroMenor(self,vector):
        menor = None   
        indice= None 
        if len(vector)>0:
            menor = vector[0]
            for i,valor in enumerate(vector):
                if valor <= menor:
                    menor =valor
                    indice =i
        return indice,menor

    def ordenarVector(self,vector):
        vector_ordenado=[]
        while len(vector)>0:
            indice,menor=self.vectorNumeroMenor(vector)
            vector_ordenado.append(menor)
            vector.pop(indice)
        return vector_ordenado

    def buscarElementoVector(self,vector,elemento):
        encontrado = False
        for valor in vector:
            if valor  is elemento:
                encontrado = True
        return encontrado

    def vectorFactorial(self, vector):
        vector_fatorial=[]
        for valor in vector:
            vector_fatorial.append(self.factorial(valor))   
        return vector_fatorial

    def vectorPrimos(self,vector):
        vector_primos =[]
        for valor in vector:
            if self.esPrimo(valor):
                vector_primos.append(valor) 
        return vector_primos

    def esPalindromo(self, vector):
       return vector == vector[::-1]
      
class Matriz(Vector):
    def posicionMayor(self, matriz):
        mayor= 0
        posicion = ()
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] >= mayor :
                    mayor= matriz[i][j]
                    posicion = (i,j)
        return posicion, mayor

    def posicionMenor(self, matriz):
        menor= 0
        posicion = ()
        ban =0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if  ban ==0:
                    menor = matriz[i][j]
                    ban +=1  
                if matriz[i][j] <= menor :
                    menor= matriz[i][j]
                    posicion = (i,j)
        return posicion, menor
    
    def matrizAvector(self,matriz):
        vector= []
        for row in matriz:
            for valor in row:
                vector.append(valor)
        return self.ordenarVector(vector)

    def ordenarMatriz(self, matriz):
        vector = self.matrizAvector(matriz)
        cont =0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j]= vector[cont]
                cont +=1
        return matriz

    def ordenarMatrizXfila(self, matriz):
        for pos, row in enumerate(matriz):
            matriz[pos] = self.ordenarVector(row)
        return matriz
    
    def sumarMatrices(self,matriz_1, matriz_2):
        matriz=[]
        if len(matriz_1) == len(matriz_2):
            for i in range(len(matriz_1)):
                matriz.append(self.sumarVectores(matriz_1[i],matriz_2[i]))
        return matriz

