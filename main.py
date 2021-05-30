# import flask
from flask import Flask
# para renderizar las paginas html
from flask import render_template
# para capturar lo datos del html
from flask import request  #"request" is not accessed
# importar clase de usuarios
from coleccion import Colecciones
from calculo import  Calculos
from cadena import Cadena,SubCadena
from ClaseOpercionesVectoresMatriz import Operacion,Vector,Matriz

# instancia de flask con el nombre del  modulo

app = Flask(__name__)
#Instancias
operacion = Operacion()
operacion_vector = Vector()
operacion_matriz = Matriz()
# configuraciod de rutas o urls
# route (nombre url y el metodo(opcional))
@app.route('/')
def inicio():
    # return 'Mi p'
    return render_template("index.html")  

@app.route('/coleccion',  methods=['GET','POST'])
def coleccion():
    opcion,valor1,valor2,resp = '0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        if opcion == '1':
            lista = valor1.split()
            col =Colecciones(lista)
            if  col.getElemento(int(valor2)) != -1 :
                resp = col.getElemento(int(valor2))
            else:
                resp = 'No existe elemento en esa posicion'
        
        elif opcion == '2':
            tupla= tuple(valor1.split())
            col =Colecciones(tupla)
            resp = 'Tupla('+col.recorrido()+')'
        
        elif opcion == '3':
            lista=valor1.split()
            col =Colecciones(lista)
            resp = '['+col.recorrido()+']'

        elif opcion == '4':
            lista= valor1.split(',')
            dic ={}
            for item in lista:
                pos= item.find(":")
                clave = item[:pos]
                valor = item[pos+1:]
                dic[clave] = valor
            col = Colecciones(dic)
            resp = col.diccionario()

        elif opcion == '5':
            lista=valor1.split()
            col = Colecciones(lista)
            resp = col.invertir()

        elif opcion == '6':
            usuarios = [('Daniel','123'),('Yady','456'),('Erick','xyz')]
            col = Colecciones(usuarios)
            resp = col.listaTupla()
        elif opcion == '7':
            usuarios = [
                {'nombre':'Daniel','clave':'123'},
                {'nombre':'Yady','clave':'456'},
                {'nombre':'Erick','clave':'xyz'}
                ]
            col = Colecciones(usuarios)
            resp = col.listaDiccionario()
            
        elif opcion == '8':
            lista=valor1.split()
            col =Colecciones(lista)
            resp =  col.listaComprehension()

        elif opcion == '9':
            lista=valor1.split(',')
            col =Colecciones(lista)
            resp =  col.diccionarioComprehension()


    return render_template("colecciones.html",seleccion =opcion, n1=valor1,n2=valor2,respuesta=resp )  

@app.route('/calculo' , methods=['GET','POST'])
def calculo():
    opcion,valor1,valor2,resp = '0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        if opcion == '1':
            calculo  = Calculos(int(valor1))
            resp = calculo.divisores()

        if opcion == '2':
            calculo  = Calculos(int(valor1))
            resp = calculo.paresEimpares()

        if opcion == '3':
            calculo  = Calculos(int(valor1))
            resp = calculo.fibonacci()

        if opcion == '4':
            calculo  = Calculos(int(valor1))
            if calculo.esPrimo():
                resp = 'El numero {} Si es primo'.format(valor1)
            else:
                resp = 'El numero {} No es primo'.format(valor1)

        if opcion == '5':
            calculo  = Calculos(int(valor1))
            resp = calculo.primos()

        if opcion == '6':
            calculo  = Calculos(0)
            if calculo.primosGemelos(int(valor1),int(valor2)):
                resp = '({},{}) Son Primos Gemelos'.format(valor1,valor2)
            else:
                resp = '({},{}) No Son Primos Gemelos'.format(valor1,valor2)

        if opcion == '7':
            calculo  = Calculos(int(valor1))
            if calculo.esPerfecto():
                resp = 'El numero {} Si es perfecto'.format(valor1)
            else:
                resp = 'El numero {} No es perfecto'.format(valor1)

        if opcion == '8':
            calculo  = Calculos(0)
            if calculo.sonAmigos(int(valor1),int(valor2)):
                resp = '({},{}) Son Amigos'.format(valor1,valor2)
            else:
                resp = '({},{}) No Son Amigos'.format(valor1,valor2)
                
        if opcion == '9':
            calculo  = Calculos(int(valor1))
            resp = calculo.invertir()

        if opcion == '10':
            calculo  = Calculos(valor1)
            resp = calculo.binarioAdecimal()

        if opcion == '11':
            calculo  = Calculos(int(valor1))
            resp = calculo.decimalAbinario()


    return render_template("calculo.html",seleccion =opcion, n1=valor1,n2=valor2,respuesta=resp)  

@app.route('/cadena', methods=['GET','POST'])
def cadena():
    opcion,valor1,valor2,valor3,resp = '0','','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        valor3 = request.form['valor3']
        if opcion == '1':
            cadena  = Cadena(valor1)
            resp = cadena.recorrer()

        if opcion == '2':
            cadena  = Cadena(valor1)
            resp = cadena.invertir()

        if opcion == '3':
            cadena  = Cadena(valor1)
            enc = cadena.buscarCaracter(valor2) 
            resp ='el caracter esta en la posicion {}'.format(enc) if enc != -1 else 'Caracter No encontrado'
        
        if opcion == '4':
            cadena  = Cadena(valor1)
            resp = cadena.buscarVocales()

        if opcion == '5':
            cadena  = Cadena(valor1)
            enc = cadena.buscarCaracteres(valor2) 
            resp ='el caracter esta en las posiciones {}'.format(enc) if enc  else 'Ninguna Ocurrencia encontrada'
        
        if opcion == '6':
            cadena  = Cadena(valor1)
            resp = cadena.cancatenar(valor2)

        if opcion == '7':
            cadena  = Cadena(valor1)
            resp = cadena.reemplazarCaracter(valor2,valor3)
        if opcion == '8':
            cadena = '1,2,3,4,5,677,90,6' if not valor1 else valor1 
            lista = [int(car)for car in cadena.split(',')]
            resp = 'Lista creada: {}'.format(lista)

        if opcion == '9':
            lista  = ["hola","tal",",Como estas"]
            cadena =''
            for elem in lista:
                cadena += elem+' '
            resp = 'Lista {}\ncadena creada: {}'.format(lista,cadena)

        if opcion == '10':
            subcadena  = SubCadena(valor1)
            enc = subcadena.buscarPalabras(valor2)
            print(enc)
            resp ='La Subcadena se encuentra en las posiciones {}'.format(enc) if enc  else 'No se encontro la Subcadena'

        if opcion == '11':
            subcadena  = SubCadena(valor1)
            resp = subcadena.insertarPalabra(valor2)

        if opcion == '12':
            subcadena  = SubCadena(valor1)
            resp = subcadena.eliminarPalabra(valor2)

        if opcion == '13':
            calculo  = Calculos(valor1)
            resp = calculo.binarioAdecimal()

        if opcion == '14':
            calculo  = Calculos(int(valor1))
            resp = calculo.decimalAbinario()

    return render_template("cadena.html",seleccion =opcion, n1=valor1,n2=valor2,n3=valor3,respuesta=resp)  

@app.route('/ayuda')
def ayuda():
    return render_template("ayuda.html")  

@app.route('/ejercicio',  methods=['GET','POST'])
def ejercicio():
    opcion,valor1,valor2,valor3,resp = '0','','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        valor3 = request.form['valor3']

        if opcion == '1':
            numero = int(valor1) 
            if operacion.esPar(numero):
                resp='El numero {} es par'.format(numero)
            else:
                resp='El numero {} no es par'.format(numero)

        if opcion == '2':
            resp ='El producto es {}'.format(operacion.productoDosnumeros(int(valor1),int(valor2)))
        
        if opcion == '3':
            numero1 =int(valor1)
            numero2 =int(valor2)
            resp ='El  numero mayor es {}'.format(operacion.mayorDosNumeros(numero1,numero2)) if numero1 != numero2 else 'Los numeros son iguales'
        
        if opcion == '4':
            numero1 =int(valor1)
            numero2 =int(valor2)
            numero3 =int(valor3)
            resp ='Los numeros son iguales'if numero1 == numero2 == numero3 else  'El  numero mayor es {}'.format(operacion.mayorTresNumeros(numero1,numero2,numero3)) 
        
        if opcion == '5':
            numero =int(valor1)
            resp =operacion.tablaMultiplicar(numero)

        if opcion == '6':
            suma,producto = operacion.secuencia30NumerosSumaProducto()
            resp ='30 Numeros aleatorios:\nLa suma es: {}\nEl producto es: {}'.format(suma,producto)

        if opcion == '7':
            suma = operacion.secuenciaHastaNegativo()
            resp ='Secuencia Hasta Que sea Negativo:\nLa suma es: {}'.format(suma)

        if opcion == '8':
            numero1 =int(valor1)
            numero2 =int(valor2)
            producto = operacion.productoXsuma(numero1,numero2)
            resp ='El producto entre {} y {} es : {}'.format(numero1,numero2,producto)
  
        if opcion == '9':
            numero1 =int(valor1)
            numero2 =int(valor2)
            cociente ,residuo = operacion.divisionXresta(numero1,numero2)
            resp ='El cociente es : {} y el Residuo es {}'.format(cociente, residuo)
 
        if opcion == '10':
            producto = operacion.secuenciaHastaLetraF()
            resp ='Secuencia Hasta Que sea Letra  F:\nEl Producto es: {}'.format(producto)

        if opcion == '11':
            longitud = int(valor1) if valor1.isdigit() else 5
            mayor  = operacion.secuenciaHallarMayor(longitud)
            resp ='Secuencia con longitud de {}:\nEl Mayor es: {}'.format(longitud,mayor)
        
        if opcion == '12':
            decimal = int(valor1)
            binario = operacion.decimalAbinario(decimal)
            resp ='El  binario de {} es {}'.format(decimal,binario)

        if opcion == '13':
            suma= 0
            for numero in range(2,30,3):
                if operacion.esMultiplo5(numero):
                    suma += numero
            resp = 'La suma de multiplos de 5  de 2  al 30 es : {} '.format(suma)
        
        if opcion == '14':
            media = round(operacion.secuenciaHastaLetraT(),2)
            resp ='La Media de todos Secuencia los valores numericos aleatorios hasta que sea T: \nLa Media es {}'.format(media)
           
        if opcion == '15':
            mayor,menor,lista = operacion.secuenciaHayarMayorMenorHastaImpar()
            resp ='Leer una secuencia se números y mostrar cuales de ellos es el mayor y el menor: \nLista numeros:{}\nEl Mayor es: {}\nEl Menor es: {}'.format(lista,mayor,menor)
           
        if opcion == '16':
            longitud = int(valor1) if valor1.isdigit() else 5
            suma,lista = operacion.secuenciaSumarPares(longitud)
            resp ='Leer una secuencia de números es {} y sumar solo los pares mostrando el resultado del proceso.: \nLista numeros:{}\nLa suma de Pares es :{}'.format(longitud,lista,suma)
        
        if opcion == '17':
            longitud = int(valor1) if valor1.isdigit() else 5
            suma,lista = operacion.secuenciaSumar30Numeros(longitud)
            resp ='Leer una secuencia de números con longitud {} y mostrar la suma de los 30 números que ocupan posiciones de lectura par.: \nLista numeros:{}\nLa suma de Posicion Pares es :{}'.format(longitud,lista,suma)
        
        if opcion ==  '18':
            numero = int(valor1)
            resp = 'Leer un número y determinar su factorial\nEl Factorial de {} es {}'.format(numero,operacion.factorial(numero))  
        
        if opcion ==  '19':
            numero = int(valor1)
            primo = 'El numero {} es primo'.format(numero) if operacion.esPrimo(numero) else 'El numero {} No es primo'.format(numero) 
            resp = 'Leer un número y determinar si es o no es primo.\n{}'.format(primo)  
        
        if opcion ==  '20':
            suma,lista = operacion.secuenciaSumar30sumaPrimos()
            resp = 'Leer una secuencia de 30 números y mostrar la suma de los primos.\nLista Numeros Generados: {}\nLa suma de los primos es: {}'.format(lista,suma)  
        
        if opcion ==  '21':
            suma,lista = operacion.secuenciaSumar30sumaFactorial()
            resp = 'Leer una secuencio de 30 números y mostrar la suma de su factorial.\nLista Numeros Generados: {}\nLa suma de los factoriales  de cada numero es: {}'.format(lista,suma)  
        
        
        if opcion ==  '22':
            longitud = int(valor1) if valor1.isdigit() else 5
            suma_pares,suma_multiplos5,lista = operacion.secuenciaSumaParesMultiplo5(longitud)
            resp = ' Leer una secuencia de números y mostrar la suma de los pares y el producto de los  que son múltiplo de 5\nLista Numeros Generados: {}\nLa suma pares: {} \nLa suma Multiplo5: {}'.format(lista,suma_pares,suma_multiplos5)  
        
        if opcion ==  '23':
            longitud = int(valor1) if valor1.isdigit() else 5
            mayor,lista = operacion.secuenciaMayorPares(longitud)
            resp = ' Leer una secuencia de números y determinar el mayor de los pares leídos.\nLongitud Secuencia {}\nLista Numeros Generados: {}\nNumero Mayor de los Pares es: {}'.format(longitud,lista,mayor)  
        
        if opcion ==  '24':
            longitud = int(valor1) if valor1.isdigit() else 5
            mayor,menor,lista = operacion.secuenciaMayorMultiplo5MenorMultiplo3(longitud)
            resp = 'Secuencia de {} numeros\nSecuenci Generada:{}\nMayor Multiplo de 5: {}\nMenor Multiplo de 3: {}'.format(longitud,lista,mayor,menor)  
        
        if opcion ==  '25':
            lis= valor1.split(',') 
            col = Colecciones(lis)
            vector =col.listaComprehension()
            vector = [int(car) for car in vector]
            mayor  = operacion_vector.vectorNumeroMayor(vector)
            resp = 'Secuencia:{}\nMayor Numero es: {} en poscicion {}'.format(vector,mayor[1],mayor[0])  

        if opcion == '26':
            A = [int(car)for car in valor1.split(',')]
            B = [int(car)for car in valor2.split(',')]
            C = operacion_vector.sumarVectores(A,B)
            resp ='Vector A: {}\nVector B: {}\nResultado: {}'.format(A,B,C)
        
        if opcion == '27':
            A = [int(car)for car in valor1.split(',')]
            B = [int(car)for car in valor2.split(',')]
            C = operacion_vector.sumarVectores(A,B)
            mayor= operacion_vector.vectorNumeroMayor(C)
            resp ='Vector A: {}\nVector B: {}\nC: {}\nMayor vector C: {} esta en posicion {}'.format(A,B,C,mayor[1],mayor[0])
           
        if opcion == '28':
            A = [int(car)for car in valor1.split(',')]
            aux =[int(car)for car in valor1.split(',')]
            vector_ordenado= operacion_vector.ordenarVector(aux)
            resp ='Vector Ingresado: {}\nVector Ordenado: {}'.format(A,vector_ordenado)

        if opcion == '29':
            A = [int(car)for car in valor1.split(',')]
            numero=int(valor2)
            print('Vector A leido ', A)
            if (operacion_vector.buscarElementoVector(A,numero)):
                resp='El Numero {} si esta  en el  Vector'.format(numero)
            else:
                resp= 'El Numero {} No encontrado en el  Vector'.format(numero)

        if opcion == '30':
            vector = [int(car)for car in valor1.split(',')]
            vector_factorial = operacion_vector.vectorFactorial(vector)
            resp ='Vector Ingresado:{}\n Vector con valores factoriales: {}'.format(vector,vector_factorial)

        if opcion == '31':
            vector = [int(car)for car in valor1.split(',')]
            aux = [int(car)for car in valor1.split(',')]
            vector_ordenado = operacion_vector.ordenarVector(aux)
            resp='Vector: \n{}\nVector Ordenado:\n{}'.format(vector,vector_ordenado)

        if opcion == '32':
            A=[
                [12,342,9,47],
                [14,26,77,99],
                [11,46,49,90],
                [12,36,79,12],
                [1,69,78,300]
                ]
            B=[
                [12,15,68,70],
                [30,29,60,17],
                [14,10,90,21],
                [100,5,75,22],
                [3,5,9,2]
                ]
            matriz_resultado = operacion_matriz.sumarMatrices(A,B)
            resp='Vector A: \n{}\nVector B:\nResultado: {}'.format(A,B,matriz_resultado)

        if opcion == '33':           
            A = [int(car)for car in valor1.split(',')]
            B = [int(car)for car in valor2.split(',')]
            matriz =[
            [12,342,9,47],
            [14,26,77,99],
            [11,46,49,90],
            [12,36,79,12],
            [1,69,78,300]
            ]
            
            posicion , mayor =operacion_matriz.posicionMayor(matriz)
            resp='Matriz Dada {}\n Numero mayor es {} esta en la posicion {}'.format(matriz,mayor,posicion)
        
        if opcion == '34':
            matriz =[
                [12,15,68,70],
                [30,29,60,17],
                [14,10,90,21],
                [100,5,75,22],
                [3,5,9,2]
                ]
            pos_mayor , numero = operacion_matriz.posicionMayor(matriz)
            pos_menor , numero = operacion_matriz.posicionMenor(matriz)
            resp = '''
                    Matriz Dada: {}\n
                    Numero mayor esta en la posicion {}\n
                    Numero menor esta en la posicion {}\n
            '''.format(matriz,pos_mayor,pos_menor)
    
        if opcion == '35':
            numero= int(valor1)
            opcion = valor2
            resultado = ''
            if opcion == 'B':
                resultado = operacion.decimalAbinario(numero)
            elif opcion == 'O':
                resultado =operacion.decimalAoctal(numero)
            elif opcion == 'H':
                resultado = operacion.decimalAhexadecimal(numero)
            else:
                resultado = 'No ingreso una opcion'
            resp ='Resultado es '+resultado
   
        if opcion == '36':
            secuencia = 20
            vector=[int(car)for car in valor1.split(',')]
            print('Vector Leido',vector)
            suma,lista_mayor = operacion_vector.sumarPosImparmayorPosPares(vector)
            resp='Sumas de posiciones pares: {} \n Numero Mayor posiciones impares: {}'.format(suma,lista_mayor)

        if opcion == '37':
            matriz =[
                [12,15,68,70],
                [30,29,60,17],
                [14,10,90,21],
                [100,5,75,22],
                [3,5,9,2]
                ]
            resp +='Matriz Dada:\n {} '.format(matriz)
            matriz_ordenada= operacion_matriz.ordenarMatriz(matriz)
            resp+='\nMatriz Ordenada: \n {}'.format(matriz_ordenada)
        if opcion == '38':
            matriz =[
                [12,15,68,70],
                [30,29,60,17],
                [14,10,90,21],
                [100,5,75,22],
                [3,5,9,2]
                ]
            resp +='Matriz Ingresada:\n {} '.format(matriz)
            matriz_ordenada_fila= operacion_matriz.ordenarMatrizXfila(matriz)
            resp +='\nMatriz Ordenada por fila: \n {}'.format(matriz_ordenada_fila)

        if opcion == '39':
            vector=[14,54,37,17,22,78,71,40,78,15,7,5,8,16,46,60,19]
            vector_primos = operacion_vector.vectorPrimos(vector)
            resp='Vector:{}  \nprimos encontrados son : {}'.format(vector,vector_primos)
        if opcion == '40':
            conjunto =[]
            print(valor1.split(','))
            secuencia = [int(car) for car in valor1.split(',')]
            print(secuencia)
            elementos_repetidos =[]
            for elem in secuencia:
                print(elem)
                if operacion_vector.buscarElementoVector(conjunto,elem):
                    elementos_repetidos.append(elem)
                else:
                    conjunto.append(elem)
            resp = '''
                    Seccuencia Ingresada: \n{}\n
                    Valores  Repetidos: \n{}\n
                    Valores  Unicos: \n{}\n
            '''.format(secuencia,elementos_repetidos,conjunto)

        
        if opcion == '41':
            parrafo = valor1
            resp='El parrafo esta compuesto {} palabras'.format(operacion.contarPalabrasParrafo(parrafo))   
        
        if opcion == '42':
            parrafo = valor1
            palabra_mayor  = operacion.palabraMayorTamañoParrafo(parrafo)
            resp ='La palabra con mayor tamaño  es :  {}'.format(palabra_mayor)   
        if opcion == '43':
            if (operacion_vector.esPalindromo(valor1)):
                resp='Es palindromo'
            else:
                resp='No es palindromo'

    return render_template("ejercicios.html",seleccion =opcion, n1=valor1,n2=valor2,n3=valor3,respuesta=resp )

if __name__ == '__main__':
    app.run(port=3000,debug=True)