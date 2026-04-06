# Meu primeiro programa em python

'''nome = input("Digite seu nome: ")
print(nome)
print(type(nome))
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número para soma: "))
soma = n1 + n2
media = soma/2
print(f"A soma de {n1} + {n2} é igual {soma}")
print(type(soma))
print(f"A média é igual {media}")
print(type(media))'''
from time import sleep

#Ex1, Ex2, Ex3:
"""nome = input('Digite seu nome: ')
print(f"Prazer {nome}!")
a = 3
b = 5
prod = 2 * a * 3 * b
print(f"O produto de 2 x 3 x 3 x 5 é igual: {prod}")
print("Digite três números inteiros abaixo e veja a soma total: ")
n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3: "))
soma = n1 + n2 + n3
print(f"A soma dos 3 números é igual: {soma}")"""

"""print("Média de duas notas")
n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))
media = (n1 + n2) / 2
print(f"Sua média foi {media:.1f}")"""

'''n1 = int(input("Digite um número inteiro para saber se é par ou impar: "))
if n1 % 2 == 0:
    print(f"O número {n1} é par!")
else:
    print(f"O número {n1} é impar!")

n2 = int(input("Digite um número no qual ao dividir o resultado é a divisão inteira: "))
n3 = int(input("Digiete um número que será o divisor: "))
divInt = n2 // n3
print(f"A divisão inteira é igual a: {divInt}")'''

'''n1 = float(input('Digite o Check Point 1: '))
n2 = float(input('Digite o Check Point 2: '))
media = (n1 + n2) / 2
print(f"A média é: {media:.2f}")
if n1 > n2:
    print(f"O Check Point 1 ({n1:.2f}) é maior que o Check Point 2 ({n2:.2f})!")
if n1 < n2:
    print(f"O Check Point 2 ({n2:.2f}) é maior que o Check Point 1 ({n1:.2f})!")
if n1 == n2:
    print('Os Check Points são iguais!')'''

#Ex4, Ex5, Ex6
'''n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
soma = n1 + n2
print(f"A soma de {n1} + {n2} é igual a {soma}\n")

metros = float(input("Digite a medida em metros: "))
milimitros = metros * 1000
print(f"{metros} em milimitros é: {milimitros:.2f}\n")

dias = int(input("Digite apenas dias atuais: "))
horas = int(input("Digite apenas horas atuais: "))
minutos = int(input("Digite apenas minutos atuais: "))
segundos = int(input("Digite apenas segundos atuais: "))

segundosDias = dias * 86400
segundosHoras = horas * 3600
segundosMinutos = minutos * 60

segundosTot = segundosDias + segundosHoras + segundosMinutos + segundos

print(f"O total em segundos é igual: {segundosTot}")'''

#Ex7, Ex8
'''salario = float(input("Digite seu salário: "))
percSal = float(input("Digite a porcentagem de aumento: "))
valorPercSal = (salario * percSal /100) + salario
print(f"Seu salário com aumento é: {valorPercSal}")'''

'''1. Escreva um programa que pergunte a velocidade do
carro de um usuário. Caso ultrapasse 80km/h, exiba
uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$5 por
km acima de 80km/h.

velocidade = int(input('Digite a velocidade: '))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f'Sua velocidade foi de {velocidade:.2f} Km/h. Sua multa foi de R${multa:.2f}')
else:
    print(f'Sua velocidade foi de {velocidade} Km/h, você esta liberado!')'''

'''2. Escreva um programa que leia três números e que
imprima o maior e o menor.

n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3 :"))
maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n2 >= n3:
    maior = n3
menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n2 <= n3:
    menor = n3
print(f"Maior = {maior}")
print(f"Menor = {menor}")'''


'''3. Escreva um programa que pergunte o salário do
funcionário e calcule o valor do aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%.
Para inferiores ou iguais, de 15%.

salario = float(input("Digite seu salário: "))
if salario > 1250.00:
    salSup = (salario * 0.10) + salario
    print(f"Salário com aumento de 10% é igual a R${salSup:.2f}")
if salario <= 1250.00:
    salInf = (salario * 0.15) + salario
    print(f"Salário com aumento de 15% é igual a R${salInf:.2f}")'''

'''4. Escreva um programa que pergunte a distância que
um passageiro deseja percorrer em km. Calcule o preço
da passagem, cobrando R$ 0,50 por km para viagens de
até 200 km e R$ 0,45 para viagens mais longas.

dist = float(input("Distancia em Km: "))
if dist <= 200:
        valMen = dist * 0.50
        print(f"Você fez uma corrida de {dist} Km. O valor da sua viagem ficou R${valMen:.2f}")
else:
        valMai = dist * 0.45
        print(f"Você fez uma corrida de {dist} Km. O valor da sua viagem ficou R${valMai:.2f}")'''

'''5. Escreva um programa que leia dois números e que
pergunte qual operação você deseja realizar. Você deve
poder calcular soma, subtração, multiplicação e divisão.
Exiba o resultado da operação solicitada.

n1 = float(input("Digite um número que deseje realizar uma operação matemática: "))
n2 = float(input("Digite outro número que deseje realizar uma operação matemática: "))
print("Escolha sua opção: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
opcao = int(input("Digite sua opção: "))
if opcao == 1:
    soma = n1+n2
    print(f"{n1} + {n2} = {soma}")
if opcao == 2:
    sub = n1-n2
    print(f"{n1} - {n2} = {sub}")
if opcao == 3:
    mlt = n1*n2
    print(f"{n1} x {n2} = {mlt}")
if opcao == 4:
    div = n1/n2
    print(f"{n1} / {n2} = {div}")
else:
    print("Opcção invalida!")'''

'''6. Escreva um programa para aprovar o empréstimo
bancário para compra de uma casa. O programa deve
perguntar o valor da casa a comprar, o salário e a
quantidade de anos a pagar. O valor da prestação
mensal não pode ser superior a 30% do salário. Calcule
o valor da prestação como sendo o valor da casa a
comprar dividido pelo número de meses a pagar.

valor = float(input("Digite o valor do imóvel: "))
sal = float(input("Digite o valor do seu salário: "))
anos = int(input("Digite o periodo em anos a pagar o imóvel: "))

totMes = anos * 12
if valor / totMes < sal * 0.3:
    print("Valor aprovado!")
else:
    print("Valor reprovado!")'''

'''7. Escreva um programa que calcule o preço a pagar
pelo fornecimento de energia elétrica. Pergunte a
quantidade de kWh consumida e o tipo de instalação: R
para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a
seguir.

kwh =  int(input("Digite o valor em Kw/h: "))
print("Selecione o tipo da sua instalação elétrica: \nR - Residencia\nI - Industria\nC - Comércio")
typ = str(input("Digite o tipo da sua instalação: ")).upper()
if typ == "R":
    if kwh <= 500:
        valor = kwh * 0.40
        print(f"Valor para tipo {typ} x R$0,40 = R${valor:.2f}")
    else:
        valor = kwh * 0.65
        print(f"Valor para tipo {typ} x R$0,65 = R${valor:.2f}")
if typ == "I":
    if kwh <= 1000:
        valor = kwh * 0.55
        print(f"Valor para tipo {typ} x R$0,55 = R${valor:.2f}")
    else:
        valor = kwh * 0.60
        print(f"Valor para tipo {typ} x R$0,60 = R${valor:.2f}")
if typ == "C":
    if kwh <= 5000:
        valor = kwh * 0.55
        print(f"Valor para tipo {typ} x R$0,55 = R${valor:.2f}")
    else:
        valor = kwh * 0.60
        print(f"Valor para tipo {typ} x R$0,60 = R${valor:.2f}")
else:
    print("Opção inválida!")'''

'''8. Faça um programa que leia 2 notas de um aluno,
calcule a média e imprima aprovado ou reprovado (para
ser aprovado a média deve ser no mínimo 6).

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
 print("Aprovado!")
else:
 print("Reprovado!")'''

'''9. Refaça o exercício 8, identificando o conceito
aprovado (média superior ou igual a 6), exame (média
maior ou igual a 4 e menor que 6) ou reprovado (média
inferior a 4).

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
 print("Aprovado")
elif media >=4 and media <6:
 print("Exame")
else:
 print("Reprovado")'''

'''Aula 4'''

'''1. Faça um programa para exibir os números de 1 a 100.

n = 0
while n < 100:
    n = n+1
    print(f"{n} patinho")'''

'''2. Faça um programa para exibir os números de 50 a
100.

n = 50

while n <= 100:
    print(n)
    n = n + 1'''

'''3. Faça um programa para escrever a contagem
regressiva do lançamento de um foguete. O programa
deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! Na tela.

n = 10
while n > 0:
    print(f"{n}")
    n = n - 1
    sleep(1)
print("Manda o zap")'''

'''4. Faça um programa para imprimir de 1 até o número
digitado pelo usuário que mostre apenas os números
ímpares.

n = int(input("Digite um número: "))
ninit = 1
while ninit <= n:
    print(ninit)
    ninit = ninit + 1'''

'''5. Faça um programa para escrever os 10 primeiros
múltiplos de 3.

n = 3

while n <= 30:
    print(n)
    n = n + 3'''

'''6. Faça um programa para exibir os resultados de uma
tabuada no formato: 2 x 1 = 2, 2 x 2 = 4, ...

n1 = int(input("Digite um número da tabuada: "))

for i in range(10):
    result = n1 * i
    print(f"{i} x {n1} = {result}")'''

'''7. Modifique o programa interior de forma que o usuário
também digite o início e o fim da tabuada, em vez de
começar com 1 e 10.

n1 = int(input("Digite um número da tabuada: "))
n2 = int(input("Digite o número final da tabuada: "))
n2 = n2 + 1
for i in range(n2):
    result = n1 * i
    print(f"{i} x {n1} = {result}")'''
'''8. Escreva um programa que pergunte o depósito inicial
e a taxa de juros de uma poupança. Exiba os valores
mês a mês para os 24 primeiros meses. Escreva o total
do ganho com juros no período.

n1 = float(input("Digite o valor inicial: "))
juros = float(input("Taxa de juros: "))
periodo = 1
ganhoJuros = 0
ganhoTot = n1

while periodo != 25:
    ganhoJuros = ganhoTot * (juros / 100)
    ganhoTot = ganhoTot + ganhoJuros
    print(f"{periodo}º mês o ganho foi de R${ganhoJuros:.2f} totalizando: R${ganhoTot:.2f}")
    periodo = periodo + 1'''

'''9. Altere o programa anterior de forma a perguntar
também o valor depositado mensalmente. Esse valor
será depositado no início de cada mês e você deve
considerá-lo para o cálculo de juros do mês seguinte.

n1 = float(input("Digite o valor inicial: "))
juros = float(input("Taxa de juros: "))
periodo = 1
ganhoJuros = 0
ganhoTot = n1

while periodo != 25:
    qntMens = float(input(f"Quantia depositada no {periodo}º mês: "))
    ganhoJuros = (qntMens + ganhoTot) * (juros / 100)
    ganhoTot = ganhoTot + ganhoJuros + qntMens
    print(f"{periodo}º mês o ganho foi de R${ganhoJuros:.2f} totalizando: R${ganhoTot:.2f}")
    periodo = periodo + 1'''

'''10. Escreva um programa que
leia números inteiros do teclado.
O programa deve ler os números
até que o usuário digite 0 (zero).
No final da execução, exiba a
quantidade de números digitados,
assim como a soma e a média
aritmética.

n1 = int
soma = 0
cont = 0
while n1 != 0:
    n1 = int(input("Digite um número: "))
    if n1 == 0:
        break
    soma = soma + n1
    cont = cont + 1
    media = soma / cont
print(f"Números digitados: {cont}\nA soma de todos os números é = {soma}\nA média deles é = {media}")'''




