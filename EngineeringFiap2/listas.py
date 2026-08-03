'''compras = ["Arroz", "Feijão", "Frango", "Batata"]

compras_novo = compras.copy()

print(compras_novo)

compras.append("Nutella")
compras_novo.append("Salada")

print(compras_novo)

print(compras[0:2])

n_compras = len(compras)

print(n_compras)

print(compras_novo[1])'''

'''compras = []
compras += ["Polia"]
compras += ["Roda", "Fuso trapezoidal"]
compras.extend(["Pablo", "Boiola"])
print(compras)'''

'''lista1 = ["Pepino", "Brócolis", "Cenoura", "Caju"]
lista2 = ["Geléia", "Maionese", "Manteiga", "Mostarda", "Katchup"]

lista3 = lista1 + lista2

opcao = str(input("Digite o produto desejado: "))
for i in lista3:
    if opcao == i:
        print(f'O produto {i} foi encontrado!')
        break
else:
    print("Produto não encontrado")'''

'''lista1 = [4, 68, 10, 2, 31, 24, 1]

minimo = lista1[0]

for i in lista1:
    if minimo > i:
        minimo = i

print(minimo)'''

listaT = [-10, -8, 0, ]