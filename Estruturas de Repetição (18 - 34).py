#!/usr/bin/env python
# coding: utf-8

# # Estruturas de repetição

# #### 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

# In[ ]:


n = int(input('Informe quantos números terão seu conjunto: '))
numeros = []
for i in range(n):
    num = float(input('Insira um número: '))
    numeros.append(num)
print(f'Menor do conjunto: {min(numeros):.0f}')
print(f'Maior do conjunto: {max(numeros):.0f}')
print(f'Soma do menor e maior valor do conjunto: {min(numeros) + max(numeros):.0f}')


# #### 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

# In[ ]:


numeros = []
qtde = 0

n = int(input('Digite a quantiade de número que deseja digitar: '))
while n != qtde:
    numero = float(input('Digite um número: '))
    while numero > 1000 or numero < 0:
        numero = float(input('(Erro!)Valor inválido\nDigite um número: '))
    numeros.append(numero)
    qtde += 1

print(f'Menor do conjunto: {min(numeros):.0f}')
print(f'Maior do conjunto: {max(numeros):.0f}')
print(f'Soma do menor e maior valores do conjunto: {min(numeros) + max(numeros):.0f}')


# #### 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

# In[ ]:


import math
vezes = 0
n = int(input('Informe quantas vezes deseja calcular o fatorial: '))

while n != vezes:
    numero = int(input('Informe um número: '))
    while numero <= 0 or numero >= 16:
        numero = int(input('(Erro!) Informe um número entre 1 e 15: '))
    print(f'{numero}! = {math.factorial(numero)}')
    vezes += 1


# #### 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# In[ ]:


n = int(input('Insira um número inteiro: '))
multiplos = 0

for i in range(2, n):
    if n % i == 0:
        multiplos += 1
if multiplos == 0:
    print(f'{n} é número primo')
else:
    print(f'{n} não é número primo')


# #### 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

# In[ ]:


n = int(input('Insira um número inteiro: '))
multiplos = 0

for i in range(2, n):
    if n % i == 0:
        print(f'Múltiplo de {i}')
        multiplos += 1
if multiplos == 0:
    print(f'{n} é número primo')
else:
    print(f'{n} tem {multiplos} múltiplos, portanto não é número primo')


# #### 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# In[ ]:


n = int(input('Informe um número: '))
div = 0
primos = []

for i in range(1, n + 1):
    if i >= 1:
        for j in range(2, i):
            if (i % j == 0):
                div +=1
                break
        else:
            primos.append(i)
            div +=1
            print(f'{i} é número primo e foram realizadas {div} para descobrir isso')


# #### 24 . Faça um programa que calcule o mostre a média aritmética de N notas.

# In[ ]:


qtde_notas = int(input('Informe quantas notas serão processadas: '))
notas = 0

for i in range(1, qtde_notas + 1):
    nota = float(input(f'{i}° nota: '))
    notas += nota
media = notas / qtde_notas
print(f'Média: {media:.1f}')


# #### 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60 e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

# In[ ]:


qtde_pessoas = int(input('Informe a quantidade de pessoas que participarão do programa: '))
idades = 0

for i in range(1, qtde_pessoas + 1):
    idade = float(input(f'Idade da {i}ª pessoa: '))
    idades += idade
media_idade = idades / qtde_pessoas

if 0 <= media_idade <= 25:
    print(f'A média de idade entre os entrevistados é de {media_idade:.0f} anos')
    print('Esta turma é jovem')
elif 26 <= media_idade <= 60:
    print(f'A média de idade entre os entrevistados é de {media_idade:.0f} anos')
    print('Esta turma é adulta')
else:
    print(f'A média de idade entre os entrevistados é de {media_idade:.0f} anos')
    print('Esta turma é idosa')


# #### 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# In[ ]:


qtde_eleitores = int(input('Informe a quantidade de eleitores: '))
candidato1 = 0
candidato2 = 0
candidato3 = 0
nulo = 0

for i in range(qtde_eleitores):
    voto = int(input('1 - Candidato 1\n2 - Candidato 2\n3 - Candidato 3\nInforme seu voto: '))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        nulo += 1
print(f'O Candidato 1 recebeu {candidato1} votos')
print(f'O Candidato 2 recebeu {candidato2} votos')
print(f'O Candidato 3 recebeu {candidato3} votos')
print(f'Houveram {nulo} votos anulados')


# #### 27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

# In[ ]:


qtde_turmas = int(input('Informe a quantidade de turmas: '))
total_alunos = 0

for i in range(qtde_turmas):
    qtde_alunos = int(input(f'Quantidade de alunos na turma {i + 1}: '))
    total_alunos += qtde_alunos
media_alunos = total_alunos / qtde_turmas
print(f'Média de alunos por turma: {media_alunos:.1f}')


# #### 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

# In[ ]:


qtde_cds = int(input(f'Informe a quatidade de CDs: '))
total = 0

for i in range(qtde_cds):
    valor = float(input(f'Informe o preço do {i + 1}º CD: '))
    total += valor
media_valor = total / qtde_cds
print(f'Média por CD: R$ {media_valor:.2f}')


# #### 29. O Sr. Manoel Joaquim possui uma grande loja de artigos de R\\$ 1,99, com cerca de 10 caixas. 
# 
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
# <pre>
# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50
# </pre>

# In[ ]:


print('Loja Quase Dois - Tabela de preços')

for i in range(50):
    precos = (i + 1) * 1.99
    print(f'{i + 1} - R$ {precos:.2f}')


# #### 30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de R\\$ 1,99. 
# 
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# <pre>
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.0
# </pre>
# 

# In[ ]:


preco = float(input('Preço do pão: R$ '))

print('Panificadora Pão de Ontem - Tabela de preços')
for i in range(50):
    preco_por_qtde = (i + 1) * preco
    print(f'{i + 1} - R$ {preco_por_qtde:.2f}')


# #### 31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
# 
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# 
# <pre>
# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...
# </pre>

# In[ ]:


valor_produto = float(input('Informe o valor do produto: R$ '))
produtos = 1
valores = [valor_produto]

while valor_produto != 0:
    valor_produto = float(input('Informe o valor do produto: R$ '))
    valores.append(valor_produto)
    produtos +=1
print(f'Total a pagar: R${sum(valores):.2f}')
dinheiro = float(input('Total recebido: R$ '))
troco = dinheiro - sum(valores)

print('-------------------------')
print('Lojas Tabajara')
for i in range(produtos):
    print(f'Produto {i + 1}: R$ {valores[i]:.2f}')
print(f'Total: R$ {sum(valores):.2f}')
print(f'Dinheiro: R$ {dinheiro:.2f}')
print(f'Troco: R$ {troco:.2f}')


# #### 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# <pre>
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120
# </pre

# In[ ]:


import math
numero = int(input('Informe um número para que seja calculado o seu fatorial: '))
numeros = numero
fatorial = math.factorial(numero)

print(f'{numero}! = ', end = '')
for i in range(numero - 1):
    print(numeros, end = ' x ')
    numeros -= 1
print('1 =', fatorial)


# #### 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas e informe, ao final, a menor e a maior temperaturas informadas, bem como a média das temperaturas.

# In[ ]:


n = int(input('Quantidade de entradas: '))
temperaturas = []

for i in range(n):
    temp = float(input('Informe a temperatura: '))
    temperaturas.append(temp)
media = sum(temperaturas) / n
print(f'A maior temperatura informada é: {max(temperaturas):.1f} °C')
print(f'A menor temperatura informada é: {min(temperaturas):.1f} °C')
print(f'A média de temperatura entre as temperaturas informadas é: {media:.1f} °C')


# #### 34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# In[ ]:


n = int(input('Insira um número inteiro: '))
multiplos = 0

for i in range(2, n):
    if n % i == 0:
        multiplos += 1
if multiplos == 0:
    print(f'{n} é número primo')
else:
    print(f'{n} não é número primo')

