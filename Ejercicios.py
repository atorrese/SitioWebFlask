import random
from ClaseOpercionesVectoresMatriz import Operacion, Vector, Matriz
operacion = Operacion()
operacion_vector = Vector()
operacion_matriz = Matriz()
print("""
        ===========================================================================================
            1. Leer un número y mostrar por la salida estándar si dicho número es o no es par.
        ===========================================================================================\n
        """)
numero = int(input('Digite numero a verificar: '))
if operacion.esPar(numero):
    print('El numero {} es par'.format(numero))
else:
    print('El numero {} no es par'.format(numero))
print("""\n
        ===========================================================================================
            2. Leer 2 números y mostrar el producto de ellos.
        ===========================================================================================\n
        """)

numero1=int(input('Ingrese 1er numero: '))
numero2=int(input('Ingrese 2do numero: '))
print('El producto es {}'.format(numero1*numero2))

print("""\n
        ===========================================================================================
            3. Leer 2 números y determinar el mayor de ellos.
        ===========================================================================================\n
        """)

numero1=int(input('Ingrese 1er numero: '))
numero2=int(input('Ingrese 2do numero: '))
mayor = 'El numero mayor es {}'
if numero1 > numero2:
    mayor = mayor.format(numero1)
elif numero2 > numero1:
    mayor = mayor.format(numero2)
else:
    mayor = 'Los numeros son iguales'
    
print(mayor)
print("""\n
        ===========================================================================================
            4. Leer 3 números y determinar el mayor de ellos.
        ===========================================================================================\n
        """)

numero1=int(input('Ingrese 1er numero: '))
numero2=int(input('Ingrese 2do numero: '))
numero3=int(input('Ingrese 3do numero: '))
mayor = 'El numero mayor es {}'
if numero1 > numero2 and  numero1 > numero3:
    mayor = mayor.format(numero1)
elif numero2 > numero1 and numero2 > numero3:
    mayor = mayor.format(numero2)
elif numero3 > numero1 and numero3 > numero2:
    mayor = mayor.format(numero3)
else:
    mayor = 'Los numeros son iguales'
print(mayor)
print("""\n
        ===========================================================================================
            5. Leer un número y mostrar su tabla de multiplicar.
        ===========================================================================================\n
        """)

numero=int(input('¿ Que mumero  tabla multiplicar deseas ? : '))
operacion.tablaMultiplicar(numero)

print("""\n
        ===========================================================================================
            6. Leer una secuencia de 30 números y mostrar la suma y el producto de ellos.
        ===========================================================================================\n
        """)
suma = 0
producto= 1
for indice in range(1,31):
    numero=int(input('Ingrese un numero  {} :'.format(indice)))
    suma += numero
    producto *= numero

print('El suma de los numeros ingresado es: {}'.format(suma))
print('El producto de los numeros  es: {}'.format(producto))

print("""\n
        ===========================================================================================
            7. Leer una secuencia de números, hasta que se introduce un número negativo y
             mostrar la suma de dichos números.
        ===========================================================================================\n
        """)

suma = 0
while(True):
    numero=int(input('Ingrese un numero :'))
    if numero <=0:
        break
    suma += numero

print('La suma de los numeros es: {}'.format(suma))

print("""\n
        ===========================================================================================
            8. Leer dos números y realizar el producto mediante sumas.
        ===========================================================================================\n
        """)

numero1=int(input('Ingrese 1er  numero: '))
numero2=int(input('Ingrese 2do numero: '))
producto = 0
for num in range(numero1):
    producto += numero2
print('El producto entre {} y {} es : {}'.format(numero1,numero2,producto))

print("""\n
        ===========================================================================================
            9. Leer dos números y realizar la división mediante restas mostrando el cociente y el resto.
        ===========================================================================================\n
        """)


dividendo=int(input('Ingrese 1er numero: '))
divisor=int(input('Ingrese 2do numero: '))
residuo = 0
while dividendo >= divisor:
    dividendo -= divisor
    residuo +=1
cociente = dividendo
print('El cociente es : {} y el Residuo es {}'.format(cociente, residuo))
print("""\n
        ===========================================================================================
            10. Leer una secuencia de números y mostrar su producto, el proceso finalizará cuando el usuario pulse a la tecla F.
        ===========================================================================================\n
        """)
producto  =1
while 0==0 :
    numero = input('Ingrese numero: ')
    if numero.isdigit():
        producto *= int(numero)
    elif numero in 'fF':
        break

print('El Producto es: {}'.format(producto))
print("""\n
        ===========================================================================================
            11. Lee una secuencia de números y determina cual es el mayor de ellos.
        ===========================================================================================\n
        """)
n=int(input('Cuantos numero va a ingresar: '))
mayor = 0
for i in range(1,n+1):
    numero=int(input('Ingrese un numero ({}): '.format(i)))
    if numero > mayor:
        mayor = numero
print('El numero  mayor es {}'.format(mayor))

print("""\n
        ===========================================================================================
            12. Dado un número mostrar su valor en binario.
        ===========================================================================================\n
        """)

numero= int(input('Digite numero a convertir  en Binario: '))
print('El  binario de {} es {}'.format(numero,operacion.decimalAbinario(numero)))

print("""\n
        ===========================================================================================
            13. Generar enteros de 3 en 3 comenzando por 2 hasta el valor máximo menor que 30.
            Calculando la suma de los enteros generados que sean divisibles por 5.
        ===========================================================================================\n
        """)

suma= 0
for numero in range(2,30,3):
    if operacion.esMultiplo5(numero):
        suma += numero 
print('La suma de multiplos de 5 es : {}'.format(suma))
print("""\n
        ===========================================================================================
            14. Calcular la media de una secuencia de números, el proceso finalizará cuando presione T
        ===========================================================================================\n
        """)


print('Si quieres Salir precione T o t')
media=0
contador =0
suma = 0
while(True):
    numero = input('Ingrese Numero: ')
    if numero.isdigit():
        contador +=1
        suma += int(numero)
    elif numero  == 'T' or numero == 't':
        break
media =  suma/contador
print('La Media de todos los valores numericos ingresado es  :',int(media))

print("""\n
        ===========================================================================================
            15. Leer una secuencia se números y mostrar cuales de ellos es el mayor y el menor, 
            el proceso finalizará cuando se introduzca un número impar.
        ===========================================================================================\n
        """)
menor=0
mayor = 0
ban = 0
while(True):
    numero = input('Ingrese Numero: ')
    if numero.isdigit():
        numero = int(numero)
        if operacion.esPar(numero):
            if ban is 0:
                ban += 1
                menor = numero
            if numero > mayor:
                mayor = numero
            elif numero < menor:
                menor = numero
        else:
            break
print('El numero mayor es {}\nEl numero menor es {}'.format(mayor,menor))

print("""\n
        ===========================================================================================
            16. Leer una secuencia de números y sumar solo los pares mostrando el resultado del proceso.
        ===========================================================================================\n
        """)
suma =0
secuencia =int(input('Cuantas secuencia de  numeros  va a leer: '))
contador = 0
while(contador < secuencia):
    numero = input('Ingrese Numero secuencia({}): '.format(contador))
    if numero.isdigit():
        numero = int(numero)
        if operacion.esPar(numero):
            suma +=numero
    contador += 1
print('Suma de pares es : {} '.format(suma))

print("""\n
        ===========================================================================================
            17. Leer una secuencia de números y mostrar la suma de los 30 números que ocupan posiciones de lectura par.
        ===========================================================================================\n
        """)
suma = 0
cont = 0
secuencia =int(input('Cuantas secuencia de  numeros  va a leer: '))
numeros=[input('Ingresar  numero en indice {}: '.format(num)) for num in range(secuencia)]
for indice in range(len(numeros)):
    if numeros[indice].isdigit():
        if operacion.esPar(indice) and cont < 30:
            suma += int(numeros[i])
            cont +=1

print('El resultado de las posiciones  pares es: ',suma)

print("""\n
        ===========================================================================================
            18. Leer un número y determinar su factorial
        ===========================================================================================\n
        """)
numero= int(input('Ingrese un numero: '))
print(operacion.factorial(num))

print("""\n
        ===========================================================================================
            19. Leer un número y determinar si es o no es primo.
        ===========================================================================================\n
        """)

numero= int(input('Ingrese Numero: '))

if operacion.esPrimo(numero):
    print('El numero {} si es primo'.format(numero))
else:
    print('El numero {} no es primo'.format(numero))
print("""\n
        ===========================================================================================
            20. Leer una secuencia de 30 números y mostrar la suma de los primos.
        ===========================================================================================\n
        """)
secuencia= 30
suma = 0
for  num in range(secuencia):
    numero = input('Ingrese Numero secuencia({}): '.format(num))
    if numero.isdigit():
        numero =  int(numero)
        if operacion.esPrimo(numero):
            suma +=numero
    

print('La suma de los primos es : ',suma)
print("""\n
        ===========================================================================================
            21. Leer una secuencio de 30 números y mostrar la suma de su factorial.
        ===========================================================================================\n
        """)
secuencia= 30
suma = 0
for  num in range(secuencia):
    numero = input('Ingrese Numero secuencia({}): '.format(num))
    if numero.isdigit():
        numero = int(numero)
        if operacion.esPrimo(numero):
            suma += operacion.factorial(numero)
    
print('La suma  de numeros factoriales ingresados es : ',suma)

print("""\n
        ===========================================================================================
            22. Leer una secuencia de números y mostrar la suma de los pares y el producto de los  que son múltiplo de 5
        ===========================================================================================\n
        """)
secuencia =int(input('Cuantas secuencia de  numeros  va a leer: '))
suma_pares = 0
suma_multiplos5 =0
for  num in range(secuencia):
    numero = input('Ingrese Numero secuencia({}): '.format(num))
    if numero.isdigit():
        numero  = int(numero)
        if operacion.esPar(numero):
            suma_pares += numero
        elif operacion.esMultiplo5(numero):
            suma_multiplos5 *= numero

print('La suma de los pares es: {}\n El producto de los Multiplos de 5 es: {}'.format(suma_pares,suma_pares))
print("""\n
        ===========================================================================================
            23. Leer una secuencia de números y determinar el mayor de los pares leídos.
        ===========================================================================================\n
        """)
secuencia =int(input('Cuantas secuencia de  numeros  va a leer: '))
mayor = 0
for  num in range(secuencia):
    numero = input('Ingrese Numero secuencia({}): '.format(num))
    if numero.isdigit():
        numero = int(numero)
        if operacion.esPar(numero) and numero > mayor:
            mayor = int(numero)

print('La numero mayor de pares leidos es: {}'.format(mayor))

print("""\n
        ===========================================================================================
            24. Leer una secuencia de números y mostrar el mayor de los múltiplos de 5 leídos y el menor de los múltiplos de 3 leídos.
        ===========================================================================================\n
        """)


secuencia =int(input('Cuantas secuencia de  numeros  va a leer: '))
ban = 0
menor = 0
mayor =0
for  num in range(secuencia):
    numero = input('Ingrese Numero secuencia({}): '.format(num))
    if numero.isdigit():
        numero  = int(numero)
        if operacion.esMultiplo3(numero):
            if ban ==0 :
                menor = numero
                ban +=1
            elif numero < menor:
                menor = numero
        elif operacion.esMultiplo5(numero):
            if numero >mayor:
                mayor = numero


print('El numero mayor de los Multiplos de 5 es: {}\n El numero menor de los Multiplos de 3 es: {}'.format(mayor,menor))

print("""\n
        ===========================================================================================
            25. Leer una secuencia de 20 números almacenarlos en un vector y mostrar la posición donde se encuentra el mayor valor leído.
        ===========================================================================================\n
        """)

 
vector=[int(input('{} Ingrese numero:'.format(n))) for n in range(1,21)]
print('Valor Mayor es: \n',vector)
mayor = operacion_vector.vectorNumeroMayor(vector)
print('El numero mayor es {} y esta en la posicision {}\n'.format(mayor[1],mayor[0]))

print("""\n
        ===========================================================================================
            26. Dado dos vectores A y B de 15 elementos cada uno, obtener un vector C donde la posición i se almacene la suma de A[i]+B[i].
        ===========================================================================================\n
        """)


A=[random.randrange(200) for n in range(15)]
B=[random.randrange(200) for n in range(15)]
print('Vector A :',A)
print('Vector B :',B)
C=operacion_vector.sumarVectores(A,B)
print('Vector Resultado C:',C)

print("""\n
        ===========================================================================================
            27. Dado dos vectores A y B de 15 elementos cada uno, obtener un vector C donde la
            posición i se almacene la suma de A[i]+B[i] y mostrar el mayor de los C[i].
        ===========================================================================================\n
        """)

A=[random.randrange(200) for n in range(15)]
B=[random.randrange(200) for n in range(15)]
print('Vector A:',A)
print('Vector B:',B)
C=operacion_vector.sumarVectores(A,B)
print('Vector Resultado C:',C)
mayor = operacion_vector.vectorNumeroMayor(C)
print('Mayor C[i] :{}'.format(mayor))

print("""\n
        ===========================================================================================
            28. Dado una secuencia de número leídos y almacenados en un vector A mostrar dichos números en orden.
        ===========================================================================================\n
        """)

secuencia =int(input('Cuantas secuencia de  numeros  va a leer en el vector: '))
A=[int(input('Asignar elemento {}:'.format(n))) for n in range(1,secuencia+1)]
print('Vector A Ingresado: ',A)
print(operacion_vector.ordenarVector(A))


print("""\n
        ===========================================================================================
            29. Dado una secuencia de número leídos y almacenados en un vector A y un número
            leído determinar si dicho número se encuentra o no en el vector.
        ===========================================================================================\n
        """)

secuencia =int(input('Cuantas secuencia de  numeros  va a leer en el vector: '))
A = [int(input('Ingresar valor indice  {}: '.format(n))) for n in range(1,secuencia+1)]
numero=int(input('Ingrese numero a buscar en el vector: '))
print('Vector A leido ', A)
if (operacion_vector.buscarElementoVector(numero,A)):
    print('El Numero {} si esta  en el  Vector'.format(numero))
else:
    print('El Numero {} No encontrado en el  Vector'.format(numero))

print("""\n
        ===========================================================================================
            30. Leer una secuencia de 20 números y almacenar en un vector sus factoriales.
        ===========================================================================================\n
        """)
vector = [int(input('Ingresar valor indice  {}: '.format(n))) for n in range(1,secuencia+1)]
vector_factorial = operacion_vector.vectorFactorial(vector)
print('Vector Ingresado: ',vector)
print('Vector con valores factoriales:',vector_factorial)

print("""\n
        ===========================================================================================
            31. Leer 20 números y almacenarlos de manera ordenada en un vector.
        ===========================================================================================\n
        """)
vector = [int(input('Ingresar valor indice  {}: '.format(n))) for n in range(1,21)]
vector_ordenado = operacion_vector.ordenarVector(vector)
print('Vector: \n{}\nVector Ordenado:\n{}\n'.format(vector,vector_ordenado))

print("""\n
        ===========================================================================================
            32. Dado dos matrices A y B obtener la suma.
        ===========================================================================================\n
        """)
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
print('A:',A)
print('B:',B)
matriz_resultado = operacion_matriz.sumarMatrices(A,B)
print('A:{} + B:{}  \n',matriz_resultado)
print("""\n
        ===========================================================================================
            33. Dado una matriz determinar la posición (i,j) del mayor.
        ===========================================================================================\n
        """)
matriz =[
    [12,342,9,47],
    [14,26,77,99],
    [11,46,49,90],
    [12,36,79,12],
    [1,69,78,300]
    ]
posicion , numero =operacion_matriz.posicionMayor(matriz)
print('Matriz Dada',matriz)
print('Numero mayor esta en la posicion {}'.format(posicion ))
print("""\n
        ===========================================================================================
            34. Dado una matriz determinar la posición (i,j) del mayor y menor.
        ===========================================================================================\n
        """)


matriz =[
    [12,15,68,70],
    [30,29,60,17],
    [14,10,90,21],
    [100,5,75,22],
    [3,5,9,2]
    ]
pos_mayor , numero = operacion_matriz.posicionMayor(matriz)
pos_menor , numero = operacion_matriz.posicionMenor(matriz)
print('Matriz Dada',matriz)
print('Numero mayor esta en la posicion {}'.format(pos_mayor ))
print('Numero menor esta en la posicion {}'.format(pos_menor ))

print("""\n
        ===========================================================================================
            35. Leer un número y una letra si la letra es B mostrar el valor en binario, si es O en octal y si es H en hexadecimal.
        ===========================================================================================\n
        """)


numero= int(input('Ingrese Numero a  convertir: '))
opcion = input('Ingrese letra\nB=> Binario\nO=> Octal\nH=> Hexadecimal\nopcion: ')
resultado = ''
if opcion == 'B':
    resultado = operacion.decimalAbinario(numero)
elif opcion == 'O':
    resultado =operacion.decimalAoctal(numero)
elif opcion == 'H':
    resultado = operacion.decimalAhexadecimal(numero)
else:
    resultado = 'No ingreso una opcion'
print('Resultado es ',resultado)

print("""\n
        ===========================================================================================
            36. Leer una secuencia de 20 números almacenarlos en un vector A[1..20] y mostrar la
            suma de los elementos que ocupan posiciones pares y el mayor de los que ocupan
            posiciones impares.
        ===========================================================================================\n
        """)
secuencia = 20
vector=[int(input('Asignar elemento {}:'.format(n))) for n in range(1,secuencia+1)]
print('Vector Leido',vector)
resultado = operacion_vector.sumarPosImparmayorPosPares(vector)
print('Sumas de posiciones pares: {} \n Numero Mayor posiciones impares: {}'.format(resultado[0],resultado[1][1]))

print("""\n
        ===========================================================================================
           37. Dada una matriz A[1..4][1..5] realiza la ordenación de la misma.
        ===========================================================================================\n
        """)

matriz =[
    [12,15,68,70],
    [30,29,60,17],
    [14,10,90,21],
    [100,5,75,22],
    [3,5,9,2]
    ]
print('Matriz Dada:\n {} '.format(matriz))
matriz_ordenada= operacion_matriz.ordenarMatriz(matriz)
print('\nMatriz Ordenada: \n {}'.format(matriz_ordenada))
print("""\n
        ===========================================================================================
           38. Dada una matriz A[1..4][1..5] realiza el proceso de ordenar solo por filas.
        ===========================================================================================\n
        """)
matriz =[
    [12,15,68,70],
    [30,29,60,17],
    [14,10,90,21],
    [100,5,75,22],
    [3,5,9,2]
    ]
print('Matriz Ingresada:\n {} '.format(matriz))
matriz_ordenada_fila= operacion_matriz.ordenarMatrizXfila(matriz)
print('\nMatriz Ordenada por fila: \n {}'.format(matriz_ordenada_fila))
print("""\n
        ===========================================================================================
           39. Dado un vector de números determina aquellos que sea primos.
        ===========================================================================================\n
        """)

vector=[14,54,37,17,22,78,71,40,78,15,7,5,8,16,46,60,19]
print(vector)
vector_primos = operacion_vector.vectorPrimos(vector)
print('Los primos encontrados son : ',vector_primos)
print("""\n
        ===========================================================================================
           40. Realiza un algoritmo que lea un conjunto de secuencias y determine dada una leída si se encuentra en ese conjunto.
        ===========================================================================================\n
        """)

conjunto=[]
secuencia =int(input('Cuantas secuencia de  numeros  va a leer en el vector: '))
for indice in range(n):
    numero = int(input('{} Ingrese un numero: '.format(indice)))
    if operacion_vector.buscarElementoVector(numero,conjunto):
        print('El numero {} ya esta en el conjunto '.format(numero))
    else:
        conjunto.append(numero)
print('Numeros ingresados: ',conjunto)

print("""\n
        ===========================================================================================
          41. Dado un párrafo leído por el teclado determine cuantas palabras contiene.
        ===========================================================================================\n
        """)

parrafo = input('Escribir parrafo para contar palabras:  ')
print('El parrafo esta compuesto {} palabras'.format(operacion.contarPalabrasParrafo(parrafo)))
print("""\n
        ===========================================================================================
          42. Dado un párrafo leído por el teclado determine la palabra de mayor tamaño.
        ===========================================================================================\n
        """)

parrafo = input('Escribir parrafos:  ')
palabra_mayor  = operacion.palabraMayorTamañoParrafo(parrafo)

print('La palabra con mayor tamaño  es :  ',palabra_mayor)

print("""\n
        ===========================================================================================
          43. Dado una secuencia determina si es palíndromo.
        ===========================================================================================\n
        """) 
sec = [20,11,2,7]
sec = [15,0,0,15]
if (op.esPalindromo(sec)):
    print('Es palindromo')
else:
    print('No es palindromo')
