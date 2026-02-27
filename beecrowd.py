import os
import math


def limpar():

    os.system('cls' if os.name == 'nt' else 'clear')


limpar()

def exercicio_1021():

    valor = float(input())
    centavos = int(round(valor * 100))

    notas_centavos = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

    print("NOTAS:")

    for n in range(0,6):

        quantidade = centavos // notas_centavos[n]
        print(f"{quantidade} nota (s) de R$ {notas_centavos[n]/100:.2f}")
        centavos = centavos % notas_centavos[n]

    print("NOTAS:")

    for n in range(6, 12):

        quantidade = centavos // notas_centavos[n]
        print(f"{quantidade} moeda (s) de R$ {notas_centavos[n]/100:.2f}")
        centavos = centavos % notas_centavos[n]

def exercicio_1035():

    a, b, c, d = map(int, input().split())

    condicao1 = b > c
    condicao2 = d > a
    condicao3 = (c + d) > (a + b)
    condicao4 = c > 0 and d > 0
    condicao5 = (a % 2) == 0

    if condicao1 and condicao2 and condicao3 and condicao4 and condicao5:

        print("Valores aceitos")
    else:
        print("Valores nao aceitos")

def exercicio_1036():

    a, b, c = map(float, input().split())
    delta = (b ** 2) - (4 * a * c)

    if a == 0 or delta < 0:

        print("Impossivel calcular")
    
    else:

        r1 = (-b + math.sqrt(delta))/(2 * a)
        r2 = (-b - math.sqrt(delta))/(2 * a)

        print(f"""R1 = {r1:.5f}\nR2 = {r2:.5f}""")

def exercicio_1037():

    valor = float(input())

    if 0 <= valor <= 25:
        print("Intervalo [0,25]")
    elif 25 < valor <= 50:
        print("Intervalo (25,50]")
    elif 50 < valor <= 75:
        print("Intervalo (50,75]")
    elif 75 < valor <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")

def exercicio_1038():

    codigo, quantidade = map(int, input().split())
    preco = [4.0, 4.5, 5.0, 2.0, 1.5]
    
    print(f"Total: R$ {(quantidade * preco[codigo - 1]):.2f}")

def exercicio_1040():

    n1, n2, n3, n4 = map(float, input().split())
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4))/(2 + 3 + 4 + 1)

    print(f"Media: {media:.1f}")

    if media >= 7:

        print("Aluno aprovado.")
    elif media < 5:

        print("Aluno reprovado.")
    elif 5 <= media <= 6.9:
        
        print("Aluno em exame.")
        n_exame = float(input())
        print(f"Nota do exame: {n_exame:.1f}")
        media_final = (media + n_exame)/2
        
        if media_final >= 5:
            
            print(f"Aluno aprovado.\nMedia final: {media_final:.1f}")
        else:
            print(f"Aluno reprovado.\nMedia final: {media_final:.1f}")

def exercicio_1041():

    x, y = map(float, input().split())

    if x == 0 and y == 0:
        print("Origem")

    elif y == 0:
        print("Eixo X")

    elif x == 0:
        print("Eixo Y")

    elif x > 0 and y > 0:
        print("Q1")
    
    elif x < 0 and y > 0:
        print("Q2")

    elif x < 0 and y < 0:
        print("Q3")

    elif x > 0 and y < 0:
        print("Q4")

def exercicio_1042():

    a, b, c = map(int, input().split())

    lista_original = [a, b, c]
    lista_ordenados = sorted(lista_original)

    for numero in lista_ordenados:
        print(numero)
    
    print()

    for numero in lista_original:
        print(numero)

def exercicio_1043():

    a, b, c = map(float, input().split())

    if a < b + c and b < a + c and c < a + b:
        perimetro = a + b + c
        print(f"Perimetro = {perimetro:.1f}")

    else:
        area = ((a + b) * c)/2
        print(f"Area = {area:.1f}")

def exercicio_1044():
    
    a, b = map(int, input().split())

    if a % b == 0 or b % a == 0:
        print("São Multiplos")
    else:
        print("Não são Multiplos")

def exercicio_1045():

    a, b, c = map(int, input().split())

    if a > 0 and b > 0 and c > 0:
        lados = [a, b, c]
        lados.sort(reverse = True)

        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        elif (a ** 2) == ((b ** 2) + (c ** 2)):
            print("TRIANGULO RETANGULO")
        elif (a ** 2) > ((b ** 2) + (c ** 2)):
            print("TRIAGULO OBTUSANGULO")
        elif (a ** 2) < ((b ** 2) + (c ** 2)):
            print("TRIANGULO ACUTANGULO")
        elif a == b == c:
            print("TRIAGULO EQUILATERO")
        elif a == b or b == c:
            print("TRIANGULO ISOSCELES")

def exercicio_1046():

    inicio, fim = map(int, input().split())

    if fim > inicio:
        
        #HORA FINAL > HORA INICIAL
        duracao = fim - inicio
    else:
        #HORA FINAL <= HORA INICIAL
        duracao = (24 - inicio) + fim

    print(f"O JOGO DUROU {duracao} HORA(S)")

def exercicio_1047():

    h_inicio, min_inicio, h_fim, min_fim = map(int, input().split())

    inicio_total = h_inicio * 60 + min_inicio
    fim_total = h_fim * 60 + min_fim

    duracao = fim_total - inicio_total

    if duracao <= 0:
        duracao += 24 * 60

    duracao_horas = duracao // 60
    duracao_min = duracao % 60

    print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_min} MINUTO(S)")

def exercicio_1048():

    salario_inicial = float(input())

    if salario_inicial <= 400:

        percentual = 15

    elif 400 < salario_inicial <= 800:

        percentual = 12
    elif 800 < salario_inicial <= 1200:

        percentual = 10
    elif 1200 < salario_inicial <= 2000:

        percentual = 7
    
    elif salario_inicial > 2000:

        percentual = 4

    reajuste = salario_inicial * (percentual/100)
    salario = salario_inicial + reajuste
    print(f"""Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %""")

exercicio_1048()

def exercicio_1049():

    animais = {
        "vertebrado": {
            "ave": {
                "carnivoro": "aguia",
                "onivoro": "pomba"
            },
            "mamifero": {
                "onivoro": "homem",
                "herbivoro": "vaca"
            }
        },
        "invertebrado": {
            "inseto": {
                "hematofago": "pulga",
                "herbivoro": "lagarta"
            },
            "anelideo": {
                "hematofago": "sanguessuga",
                "onivoro": "minhoca"
            }
        }
    }

    estrutura = input()
    classe = input()
    alimentacao = input()

    print(animais[estrutura][classe][alimentacao])

exercicio_1049()
