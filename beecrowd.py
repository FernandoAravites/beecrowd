import os
import math
import sys


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
        print(f"{quantidade} nota(s) de R$ {notas_centavos[n]/100:.2f}")
        centavos = centavos % notas_centavos[n]

    print("MOEDAS:")

    for n in range(6, 12):

        quantidade = centavos // notas_centavos[n]
        print(f"{quantidade} moeda(s) de R$ {notas_centavos[n]/100:.2f}")
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
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

def exercicio_1045():
    valores = list(map(float, input().split()))
    valores.sort(reverse=True)
    a, b, c = valores

    if a >= (b + c):
        print("NAO FORMA TRIANGULO")
    else:
        if (a ** 2) == (b ** 2 + c ** 2):
            print("TRIANGULO RETANGULO")
        elif (a ** 2) > (b ** 2 + c ** 2):
            print("TRIANGULO OBTUSANGULO")
        else:
            print("TRIANGULO ACUTANGULO")
        if a == b == c:
            print("TRIANGULO EQUILATERO")
        elif a == b or b == c or a == c:
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

    try:
        ddd = int(input())
        resultado = municipios.get(ddd, "DDD nao cadastrado")
        print(resultado)
    except EOFError:
        pass

def exercicio_1124():

    while True:
    
        l, c, r1, r2 = map(int, input().split())

        if l == 0 and c == 0 and r1 == 0 and r2 == 0:

            break

        if 2 * r1 > min(l, c) or 2 * r2 > min(l, c):
            print("N")
            continue

        dist_centros = math.sqrt((l - r1 - r2) ** 2 + (c - r1 - r2) ** 2)

        if dist_centros >= r1 + r2:
            print("S")
        else:
            print("N")

def exercicio_1292():

    import sys
    import math

    constante = math.sin(math.radians(108)) / math.sin(math.radians(63))

    def solve():

        for linha in sys.stdin:
            linha = linha.strip()

            if not linha:
                continue

            lado_pentagono = float(linha)
            resultado = lado_pentagono * constante

            print(f"{resultado:.10f}")
    if __name__ == "__main__":
        solve()

def exercicio_1008():

    numero = int(input())
    horas_trabalhadas = int(input())
    money_p_hora = float(input())

    salario = horas_trabalhadas * money_p_hora

    print(f"NUMBER = {numero}\nSALARY = U$ {salario:.2f}")

def exercicio_1009():

    nome = input()
    salario_fixo = float(input())
    total_vendas = float(input())

    salario = salario_fixo + (total_vendas * 0.15)

    print(f"TOTAL = R$ {salario:.2f}")

def exercicio_1010():

    cod1, qtd1, valor1 = input().split()
    total = int(qtd1) * float(valor1)


    cod2, qtd2, valor2 = input().split()
    total += int(qtd2) * float(valor2)

    print(f"VALOR A PAGAR: R$ {total:.2f}")

def exercicio_1018():

    n = int(input())
    print(n)

    notas = [100, 50, 20, 10, 5, 2, 1]
    valor_restante = n

    for nota in range(notas):

        quantidade = valor_restante // nota
        valor_restante = valor_restante % nota

        print(f"{quantidade} nota(s) de R$ {nota},00")

def exercicio_1142():

    n = int(input())

    contagem = 1

    for i in range(n):
        print(f"{contagem} {contagem + 1} {contagem + 2} PUM")
        contagem += 4

def exercicio_1143():

    n = int(input())
    contagem = 1

    for i in range(1, n + 1):
        print(i, i ** 2, i ** 3)
        contagem += 1

def exercicio_1144():

    n = int(input())

    contagem = 1

    for i in range(1, n + 1):
        print(i, i ** 2, i ** 3)
        print(i, (i ** 2) + 1, (i ** 3) + 1)

        contagem += 1

def exercicio_1145():
    
    x, y = map(int, input().split())

    for i in range(1, y + 1):
        print(i, end = "")
        
        if i % x == 0 or i == y:
            print()

        else:
            print(" ", end = "")

def exercicio_1046():

    while True:

        x = int(input())

        if x == 0:
            break
        
        for i in range(1, x + 1):
            print(i, end = '')

            if i % x == 0 or i == x:
                print()

            else:
                print(" ", end = '')

def exercicio_1149():

    dados = iter(map(int, input().split()))
    a = next(dados)
    n = next(dados)

    while n <= 0:
        n = next(dados)

    soma = 0

    for i in range(0, n):
        soma += (a + i)

    print(soma)

def exercicio_1150():

    x = int(input())
    
    while True:
    
        z = int(input())
        if z > x:

            a = 0
            tenta = 0

            while a < z:
                a += x + tenta
                tenta += 1
            
            print(tenta)
            break

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

def exercicio_1098():

    i = 0
    j_inicial = 1

    while i <= 2.1:
        for k in range(3):
            j_atual = j_inicial + k
            
            i_limpo = round(i, 1)
            j_limpo = round(j_atual, 1)

            if i_limpo % 1 == 0:
                print(f"I={i_limpo:.0f} J={j_limpo:.0f}")
            else:
                print(f"I={i_limpo:.1f} J={j_limpo:.1f}")
        
        i += 0.2
        j_inicial += 0.2

def exercicio_1151():

    n = int(input())

    if 0 < n < 46:

        a, b = 0, 1
        resultado = []

        for i in range(n):

            resultado.append(str(a))
            a, b = b, a + b

        print(' '.join(resultado))

def exercicio_1153():

    n = int(input())

    fatorial = n

    for i in range(n - 1, 0, -1):
        fatorial *= i

    print(fatorial)

def exercicio_1154():

    somaIdade = 0
    quantidadeIdades = 0
    
    while True:
    
        idade = int(input())
        
        if idade < 0:
            break
        
        somaIdade += idade
        quantidadeIdades +=1
    
    mediaIdade = somaIdade/quantidadeIdades

    print(f"{mediaIdade:.2f}")

def exercicio_1155():

    s = 0

    for i in range(1, 101):
        s += 1/i
    
    print(f"{s:.2f}")

def exercicio_1156():

    denominador = 1
    s = 0

    for i in range(1, 40, 2):

        s += i/denominador

        denominador *= 2

    print(f"{s:.2f}")

def exercicio_1157():

    n = int(input())

    for i in range(1, n + 1):

        if n % i == 0:
            print(i)

def exercicio_1158():

    n = int(input())

    for casos in range(n):

        soma = 0
        x, y = map(int, input().split())

        contagem_impares = 0
        atual = x

        
        while contagem_impares < y:
            
            if atual % 2 != 0:
                soma += atual
                contagem_impares += 1
            
            atual += 1
    
        print(soma)

def exercicio_1159():


    while True:

        x = int(input())
        
        if x == 0: 
            break
        
        if x % 2 != 0: 
            x += 1
    
        resultado = 5 * x + 20
        print(resultado)

def exercicio_1039():


    def exercicio_1039_main():
        
        import math

        r1, x1, y1, r2, x2, y2 = map(int, input().split())

        dist_centros = math.hypot(x2 - x1, y2 - y1)

        if r1 >= dist_centros + r2:

            print("RICO")
        else:

            print("MORTO")

    while True:
        try:

            exercicio_1039_main()

        except EOFError:
            break

def exercicio_1160():

    t = int(input())
    
    for i in range(t):

        entrada = input().split()
        pa, pb = int(entrada[0, 1])
        g1, g2 = float(entrada[2, 3])
        anos = 0

        while True:

            pa_atual = pa
            pb_atual = pb
            
            if pa_atual > pb_atual or anos >= 100:
                break

            pa_atual = pa_atual * (1 + (g1 / 100))
            pb_atual = pb_atual * (1 + (g2 / 100))
            anos += 1

        if anos >= 100:
            print("Mais de 1 seculo")

def exercicio_1173():

    v = int(input())

    lista = []

    for i in range(10):

        lista.append(v)

        v *= 2
    
    for i in range(10):

        print(f"N[{i}] = {lista[i]}")

def exercicio_1174():

    for i in range(100):

        n = float(input())
        
        if n <= 10:
            print(f"A[{i}] = {n:.1f}")

def exercicio_1175():

    lista = []

    for i in range(20):

        lista.append(int(input()))
    
    for indiceTroca in range(10):

        oposto = 19 - indiceTroca
        
        lista[indiceTroca], lista[oposto] = lista[oposto], lista[indiceTroca]
    
    for escrever in range(20):

        print(f"N[{escrever}] = {lista[escrever]}")

def exercicio_1176():

    t = int(input())

    for _ in range(t):
    
        n = int(input())
        a, b = 0, 1

        
        for i in range(n):
            
            a, b = b, a + b
        
        print(f"Fib({n}) = {a}")

def exercicio_1177():

    t = int(input())

    lista = []

    for i in range(1000):

        for preencher in range(0, t):

            lista.append(preencher)

        print(f"N[{i}] = {lista[i]}")

def exercicio_1178():

    x = float(input())

    lista = [x]

    for i in range(1, 100):

        lista.append(lista[i - 1]/2)
    
    for escreve in range(100):

        print(f"N[{escreve}] = {lista[escreve]:.4f}")

def exercicio_1179():
    par = []
    impar = []

    for i in range(15):
        n = int(input())

        if n % 2 == 0:
            par.append(n)
            if len(par) == 5:
                for j in range(5):
                    print(f"par[{j}] = {par[j]}")
                par.clear()
        else:
            impar.append(n)
            if len(impar) == 5:
                for j in range(5):
                    print(f"impar[{j}] = {impar[j]}")
                impar.clear()

    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}")
        
    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")

def exercicio_1180():

    n = int(input())

    entrada = list(map(int, input().split()))
    menor = min(entrada)

    print(f"Menor valor: {min(entrada)}\nPosicao: {entrada.index(menor)}")

def exercicio_1181():

    linhaAlvo = int(input())
    operacao = input().upper()

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            valor = float(input())
            linhaTemp.append(valor)

        matriz.append(linhaTemp)
    
    valoresLinha = matriz[linhaAlvo]
    soma = sum(valoresLinha)

    if operacao == 'S':
        print(soma)
    
    if operacao == 'M':
        print(f"{soma/12:.1f}")

def exercicio_1182():

    colunaAlvo = int(input())
    operacao = input().upper()

    linha, coluna = 12, 12
    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            valor = float(input())
            linhaTemp.append(valor)

        matriz.append(linhaTemp)

    soma = 0

    for i in range(linha):

        soma += matriz[i][colunaAlvo]

    if operacao == 'S':
        print(soma)
    
    if operacao == 'M':
        print(f"{soma/12:.1f}")
    
def exercicio_1183():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if j > i:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1184():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if j < i:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")
    
def exercicio_1185():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if (i + j) < 11:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1186():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if (i + j) > 11:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1187():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if j > i and (i + j) < 11:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1188():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if j < i and (i + j) > 11:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1189():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if j < i and (i + j) < 11:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1190():

    operacao = input().upper()
    linha, coluna = 12, 12

    matriz = []

    for i in range(12):
        linhaTemp = []
    
        for j in range(12):
            linhaTemp.append(float(input()))

        matriz.append(linhaTemp)
    
    soma = 0
    quantidade = 0

    for i in range(linha):

        for j in range(coluna):

            if j > i and (i + j) > 11:

                soma += matriz[i][j]
                quantidade += 1
    
    if operacao == 'S':
        print(f"{soma:.1f}")
    
    if operacao == 'M':
        print(f"{soma / quantidade:.1f}")

def exercicio_1435():

    def contruirMatriz(n):

        # cria uma matriz quadarada só com o 0
        matriz = [[0 for _ in range(n)] for _ in range(n)]
        #[[0 for _ in range(n)] gera [0, 0, 0], for _ in range(n) faz denovo em outra linha

        # preenche a matriz com valores em relação a distância até a borda
        for i in range(n):
            for j in range(n):
                distancia = min(i, j, n -1-i, n-1-j) + 1
                # 1 1 1
                # 1 2 1 -> min(1, 1, 3-1-1, 3-1-1) = 1; 1+1 = 2
                # 1 1 1
                matriz[i][j] = distancia

        return matriz
    
    def imprimirMatriz(matriz):

        n = len(matriz)

        for i in range(n):
            linha = []
            
            for j in range(n):
                # formata com o campo de tamnho 3 justificado à direita
                linha.append(f"{matriz[i][j]:3d}")
            # coloca espaço entre os elemntos, não no começo ou fim
            print(" ".join(linha))
        print()

    def exercicio_1435_main():

        while True:
            try:
                n = int(input())
                if n == 0:
                    break
                else:
                    matriz = contruirMatriz(n)
                    imprimirMatriz(matriz)
            except EOFError:
                break

    if __name__ == "__main__":
        exercicio_1435_main()
def exercicioFizzBuzz():

    # multiplo de 3 = fizz
    # multiplo de 5 = buzz
    # multiplo 15 = fizzbuzz

    for i in range(1, int(input()) + 1):

        if i % 3 and i % 5:
            print("FizzBuzz")
        
        elif i % 3 == 0:
            print("Fizz")
        
        elif i % 5 == 0:
            print("Buzz")
        
        else:
            print(i)
import sys


def exericio_1478():

    def construir_e_imprimir(n):
        # Geramos a linha e já imprimimos para economizar memória
        for i in range(n):
            linha = []
            for j in range(n):
                valor = abs(i - j) + 1
                # {:3d} garante o campo de 3 caracteres alinhado à direita
                linha.append("{:3d}".format(valor))
            
            # Junta com um espaço e imprime a linha
            print(" ".join(linha))
        # Imprime a linha em branco obrigatória após cada matriz
        print()

    def main():
        # Usando sys.stdin para evitar problemas de performance e EOF
        input_data = sys.stdin.read().split()
        
        for valor in input_data:
            n = int(valor)
            if n == 0:
                break
            construir_e_imprimir(n)

    if __name__ == "__main__":
        main()

def exercicio_1534():

    import sys

    def resolver_1534():
        # Lê todas as entradas disponíveis no arquivo/terminal
        entrada = sys.stdin.read().split()
        
        for n_str in entrada:
            n = int(n_str)
            
            for i in range(n):
                linha = []
                for j in range(n):
                    # A secundária tem prioridade sobre a principal
                    if i + j == n - 1:
                        linha.append("2")
                    elif i == j:
                        linha.append("1")
                    else:
                        linha.append("3")
                
                # No 1534, os números são grudados, sem espaços
                print("".join(linha))

    if __name__ == "__main__":
        resolver_1534()

def exercicio_1541():

    import math as m

    while True:
        
        entrada = input().split()

        if entrada[0] == '0':
            break

        a, b, c = int(entrada[0]), int(entrada[1]), int(entrada[2])
        areaTerreno = (100 / c) * (a * b)

        ladoTerreno = int(m.sqrt(areaTerreno))

        print(ladoTerreno)

def exercicio_1557():

    import sys

    def resolver_1557():
        entrada = sys.stdin.read().split()
        
        for n_str in entrada:
            n = int(n_str)

            if n == 0:
                break

            maiorNumero = 2 ** (n + n - 2)
            largura = len(str(maiorNumero))
            
            for i in range(n):
                linha = []
                for j in range(n):
                    valor = 2**(i + j)
                    item = f"{valor:{largura}d}"
                    linha.append(item)

                print(" ".join(linha))
            print()
    if __name__ == "__main__":
        resolver_1557()

def exercicio_1564():

    while True:
            try:

                n = int(input())

                if n == 0:
                    print("vai ter copa!")
                
                else:
                    print("vai ter duas!")

            except EOFError:
                break

def exercicio_1024():

    import math

    def resolver():
        try:
            # Lê a quantidade de casos de teste
            n = int(input())
        except EOFError:
            return

        for _ in range(n):
            m = input()
            
            # --- PRIMEIRA PASSADA ---
            # Desloca letras em +3 na tabela ASCII
            m_passada1 = ""
            for char in m:
                if char.isalpha():
                    m_passada1 += chr(ord(char) + 3)
                else:
                    m_passada1 += char
            
            # --- SEGUNDA PASSADA ---
            # Inverte a string
            m_passada2 = m_passada1[::-1]
            
            # --- TERCEIRA PASSADA ---
            # Desloca -1 da metade em diante
            metade = len(m_passada2) // 2
            
            parte1 = m_passada2[:metade]
            parte2 = ""
            
            for i in range(metade, len(m_passada2)):
                parte2 += chr(ord(m_passada2[i]) - 1)
                
            print(parte1 + parte2)

    resolver()

def exercicio_1847():
    
    t1, t2, t3 = map(int, input().split())

    if t1 > t2: # DESCEU DO 1° PRO 2°

        if t2 < t3 or t2 == t3: # SUBIU DO 2° PRO 3° OU CTE
            print(":)")
        
        elif t2 > t3: # DESCEU DO 2° PRO 3° 
            
            if (t1 - t2) > (t2 - t3): # DESCEU MAIS DO 1° PRO 2° 
                print(":)")
            
            elif (t1 - t2) <= (t2 - t3): # DESCEU MAIS DO 2° PRO 3°
                print(":(")
    
    elif t1 < t2:

        if t2 > t3 or t2 == t3:
            print(":(")
        
        elif t2 < t3:

            if (t2 - t1) > (t3 - t2):
                print(":(")
            
            elif (t2 - t1) <= (t3 - t2):
                print(":)")
    else: # CTE, mas...

        if t2 < t3:
            print(":)")
        
        else:
            print(":(")

def exercicio_1848():
    for _ in range(3):
        soma = 0

        while True:
            try:
                entrada = input()
                
                if entrada == "caw caw":
                    print(soma)
                    break

                else:
                    binario = entrada.replace('*', '1').replace('-', '0')
                    soma += int(binario, 2)

            except EOFError:
                return

def exercicio_1858():

    n = int(input())

    entrada = input().split()

    lista = []

    for i in range(n):

        valor = int(entrada[i])
        lista.append(valor)

    print(lista.index(min(lista)) + 1)

def exercicio_1864():

    frase = "life is not a problem to be solved"
    fraseLista = [letra.upper() for letra in frase]

    resultado = ''

    for i in range(int(input())):

        resultado += str(fraseLista[i])
    
    print(resultado)

def exercicio_1865():

    for i in range(int(input())):

        p = input()

        if 'Thor' in p:
            print("Y")

        else:
            print("N")

def exercicio_1866():

    for i in range(int(input())):
        s = 0
        adicional = 1

        for j in range(int(input())):
            s += adicional
            adicional *= (-1)
        
        print(s)

def exercicio_1914():

    for i in range(int(input())):

        nome1, esolha1, nome2, escolha2 = input().split()
        valor1, valor2 = map(int, input().split())

        soma = valor1 + valor2
        resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'

        if esolha1 == resultado:
            print(nome1)
        
        else:
            print(nome2)
        
def exercicio_1924():

    def eh_triangulo(a, b, c):
        if (a + b > c) and (a + c > b) and (b + c > a):
            return True
        
        return False

    a, b, c, d = map(int, input().split())


    if eh_triangulo(a, b, c) or eh_triangulo(a, b, d) or \
    eh_triangulo(a, c, d) or eh_triangulo(b, c, d):
        print("S")
        
    else:
        print("N")
    
def exercicio_1930():

    t1, t2, t3, t4 = map(int, input().split())
    tomadasTotais = t1 + t2 + t3 + t4 - 3

    print(tomadasTotais)

def exercicio_1933():

    c1, c2 = map(int, input().split())

    print(max(c1, c2))

def exercicio_1957():

    numero = int(input())

    print(f"{numero:X}")

def exercicio_1958():

    try:
    
        linha = input()
        x = float(linha)

        print(f"{x:+.4E}")
    
    except EOFError:
        pass
    
exercicio_1958()
