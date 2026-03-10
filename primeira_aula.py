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