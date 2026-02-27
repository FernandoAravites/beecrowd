import os
import math
import random

def limpar():

    os.system('cls' if os.name == 'nt' else 'clear')

limpar()

def exercicio_1050():
    
    municipios = {

        61: "Brasilia",
        71: "Salvador",
        11: "Sao Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitoria",
        31: "Belo Horizonte"
    }

    ddd = int(input())

    if ddd in municipios:
        
        print(f"{municipios[ddd]}")
    else:

        print("DDD nao cadastrado")

def exercicio_1051():

    salario = float(input())

    if salario <= 2000.00:

        print("Isento")

    else:

        imposto = 0.0
        salario_dedutivo = salario

        if salario_dedutivo > 4500.00:

            imposto += (salario_dedutivo - 4500.00) * 0.28
            salario_dedutivo = 4500.00
        if salario_dedutivo > 3000.00:
            
            imposto += (salario_dedutivo - 3000.00) * 0.18
            salario_dedutivo = 3000.00
        if salario_dedutivo > 2000.00:

            imposto += (salario_dedutivo - 2000.00) * 0.08

        print(f"R$ {imposto:.2f}")

def exercicio_1052():

    mes = int(input())

    meses = {

        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    print(f"{meses[mes]}")

def exercicio_1059():

    i = 0

    while i < 100:

        i += 1

        if i % 2 == 0:

            print(i)

def exercicio_1060():

    a = float(input())
    b =float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())

    quantidade = 0

    lista = [a, b, c, d, e, f]

    for i in lista:

        if i > 0:

            quantidade += 1
    
    print(f"{quantidade} valores positivos")

def exercicio_1061():


    dia_inicio = int(input().split()[1])
    h_inicio, m_inicio, s_inicio = map(int, input().split(" : "))

    dia_fim = int(input().split()[1])
    h_fim, m_fim, s_fim = map(int, input().split(" : "))

    total_inicio = dia_inicio * 86400 + h_inicio * 3600 + m_inicio * 60 + s_inicio
    total_final = dia_fim * 86400 + h_fim * 3600 + m_fim * 60 + s_fim

    dias = (total_final - total_inicio) // 86400
    resto = (total_final - total_inicio) % 86400

    horas = resto  // 3600
    resto = resto % 3600

    minutos = resto // 60
    
    segundos = resto % 60

    print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")

def exercicio_1064():

    a = float(input())
    b = float(input())
    c = float(input())
    d= float(input())
    e= float(input())
    f= float(input())

    quantidade = 0
    soma_positivo = 0

    lista = [a, b, c, d, e, f]

    for i in lista:

        if i > 0:

            quantidade += 1
            soma_positivo += i
    
    media = soma_positivo / quantidade

    print(f"{quantidade} valores positivos\n{media:.1f}")

def exercicio_1065():

    a = float(input())
    b = float(input())
    c = float(input())
    d= float(input())
    e= float(input())

    quantidade = 0

    lista = [a, b, c, d, e]

    for i in lista:

        if i % 2 == 0:

            quantidade += 1
    
    print(f"{quantidade} valores pares")

def exercicio_1066():

    a = float(input())
    b = float(input())
    c = float(input())
    d= float(input())
    e= float(input())

    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    lista = [a, b, c, d, e]

    for i in lista:

        if i % 2 == 0:

            pares += 1
        else:

            impares += 1

        if i > 0:

            positivos += 1
        if i < 0:

            negativos += 1
    
    print(f"""{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)""")

def exercicio_1067():

    x = int(input())

    for i in range(1, x + 1, 1):

        if i % 2 == 1:
            print(i)

def exercicio_1070():
    
    x = int(input())

    for i in range(x, x + 12):

        if i % 2 == 1:

            print(i)

def exercicio_1071():
    
    x = int(input())
    y = int(input())

    soma = 0
    lim_i = x
    lim_f = y

    if x > y:

        lim_i = y
        lim_f = x

    for i in range(lim_i + 1, lim_f):

        if i % 2 == 1:
            soma += i
    
    print(soma)

def exercicio_1072():

    n = int(input())

    dentro = 0
    fora = 0

    for _ in range(n):
        
        x = int(input())
        
        if 10 <= x <= 20:
            dentro += 1
        else:
            fora += 1
            
    print(f"{dentro} in")
    print(f"{fora} out")

def exercicio_1073():

    n = int(input())

    o_par = 0
    o_quadrado = 0

    for i in range(1, n + 1):

        if i % 2 == 0:

            o_par = i
            o_quadrado = i ** 2

            print(f"{o_par}^2 = {o_quadrado}")
    
def exercicio_1074():

    n = int(input())

    for i in range(n):

        x = int(input())

        if x == 0:

            print("NULL")
        else:
            if x % 2 ==0:

                texto = "EVEN"
            else:
                
                texto = "ODD"
            if x > 0:

                texto += " POSITIVE"
            else:

                texto += " NEGATIVE"
            
            print(texto)

def exercicio_1075():

    n = int(input())

    for i in range(1, 10001):

        if i % n == 2:
            print(i)

def exercicio_1078():

    n = int(input())

    for i in range(1, 11):

        produto = n * i

        print(f"{i} x {n} = {produto}")
