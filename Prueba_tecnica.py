#taller prueba diagnostica

#punto 1 
def numero_signos(numero):
    if numero > 0:
        print("el numero", numero, "es positivo")
    elif numero < 0:
        print("el numero", numero, "es negativo")
    else:
        print("el numero es cero")

numero = int(input("ingresa un numero: "))
numero_signos(numero)
#punto 2
def numero_par(numero):
    if numero % 2== 0:
        print("el numero",numero,"es par")
    else:
        print("el numero", numero ,"es impar")
numero=int(input("ingrese el numero"))
numero_par(numero)
#punto 3
def es_fibonacci(numero):
    a = 0
    b = 1
    if numero == 0 or numero == 1:
        print("el numero", numero, "si es fibonacci")
        return
    while b < numero:
        temporal = b     
        b = a + b         
        a = temporal     

    if b == numero:
        print("el numero", numero, "si es fibonacci")
    else:
        print("el numero", numero, "no es fibonacci")
numero=int(input("ingresa el numero"))
es_fibonacci(numero)
#punto4
def numero_primo(numero):
    if numero <= 1:
        print("el numero",numero," no es primo") 
        return
    for i in range(2,numero):
        if numero % i == 0:
            print("el numero", numero, "no es primo")
            return
    print("el numero", numero, "si es primo")
numero=int(input("ingrese el numero:"))
numero_primo(numero)
#punto5
def sumar_intermedios(num1, num2):
    if num1 > num2:
        menor = num2
        mayor = num1
    else:
        menor = num1
        mayor = num2
    suma = 0
    for i in range(menor + 1, mayor):
        suma = suma + i
    print("la suma de intermedios entre", num1, "y", num2, "es:", suma)
    numero=int(input("ingrese el numero:"))
    sumar_intermedios(num1, num2)
#punto6
def elevar(numero):
    if numero % 2 != 0:
        resultado = numero ** 2
        print("el numero", numero, "es impar, al cuadrado:", resultado)
    else:
        resultado = numero ** 3
        print("el numero", numero, "es par, al cubo:", resultado)
    numero=int(input("ingrese el numero:"))
    elevar(numero)
#punto7
def procesar_codigo(codigo):
    numero = int(codigo[-4:])
    print("numero extraido del codigo:", numero)
    numero_signos(numero)
    numero_primo(numero)
    es_fibonacci(numero)
    numero_par(numero)
    elevar(numero)

codigo = input("ingresa tu codigo de estudiante: ")
procesar_codigo(codigo)
#punto8
def procesar_entrada(entrada):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

    mes_encontrado = ""
    for mes in meses:
        if mes in entrada.lower():
            mes_encontrado = mes
            break

    if mes_encontrado == "":
        print("no se encontro un mes valido")
        return ""

    print("mes encontrado:", mes_encontrado)

    # saco el mes del texto y me quedo solo con los digitos
    texto_sin_mes = entrada.lower().replace(mes_encontrado, "")
    solo_numeros = ""
    for caracter in texto_sin_mes:
        if caracter.isdigit():
            solo_numeros = solo_numeros + caracter

    numero = int(solo_numeros)
    print("numero restante:", numero)

    numero_signos(numero)
    par_impar(numero)
    es_fibonacci(numero)
    es_primo(numero)
    elevar(numero)

    return mes_encontrado

print()
entrada = input("ingresa fecha+codigo (ejemplo: 1enero2000100032300): ")
mes = procesar_entrada(entrada)


# PUNTO 9


def vocales_consonantes(mes):
    vocales = "aeiou"
    lista_vocales = []
    lista_consonantes = []
    for letra in mes:
        if letra in vocales:
            lista_vocales.append(letra)
        else:
            lista_consonantes.append(letra)
    print("vocales:", lista_vocales)
    print("consonantes:", lista_consonantes)


    print()
    print("--- analisis del mes:", mes, "---")
    vocales_consonantes(mes)
    posicion_letras(mes)

# PUNTO 10:

def posicion_letras(mes):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    for letra in mes:
        pos = abecedario.find(letra) + 1
        print("  letra '" + letra + "' esta en la posicion", pos)


    print()
    print("--- analisis del mes:", mes, "---")
    vocales_consonantes(mes)
    posicion_letras(mes)
