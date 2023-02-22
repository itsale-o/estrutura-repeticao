#!/usr/bin/env python
# coding: utf-8

# # Estruturas de Repetição

# #### 35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

# In[1]:


n = int(input('Informe um número: '))
primos = []

for i in range(1, n + 1):
    if i >= 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            primos.append(i)
            print(f'{i} é número primo')


# #### 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# <pre>
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
# 
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# </pre>
# 
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

# In[13]:


num = int(input('Montar a tabuada de: '))
comeca = int(input('Começa: '))
termina = int(input('Termina: '))

if termina < comeca:
    while termina < comeca:
        print('O valor final deve ser maior que o valor inicial')
        comeca = int(input('Começa: '))
        termina = int(input('Termina: '))
        print(f'Vou montar a tabuada de {num} começando por {comeca} e terminando em {termina}: ')
        for i in range(comeca, termina + 1):
            print(f'{num} x {i} = {num * i}')
else:
    print(f'Vou montar a tabuada de {num} começando por {comeca} e terminando em {termina}: ')
    for i in range(comeca, termina + 1):
        print(f'{num} x {i} = {num * i}')


# #### 37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
# 

# In[35]:


# códigos:
codigo_mais_gordo = 0
codigo_mais_magro = 0
codigo_mais_alto = 0
codigo_mais_baixo = 0

# peso das pessoas:
peso_mais_gordo = 0
peso_mais_magro = 1000
# altura das pessoas
altura_mais_alto = 0
altura_mais_baixo = 500  

pesos = 0
alturas = 0
clientes = 0

while True:
    codigo = int(input('Código do cliente: '))
    if codigo == 0:
        break

    clientes += 1
    altura = float(input('Altura do cliente (em cm): '))
    peso = float(input('Peso do cliente: '))

    pesos += peso
    alturas += altura

    if altura > altura_mais_alto:
        altura_mais_alto = altura
        codigo_mais_alto = codigo

    if altura < altura_mais_baixo:
        altura_mais_baixo = altura
        codigo_mais_baixo = codigo

    if peso > peso_mais_gordo:
        peso_mais_gordo = peso
        codigo_mais_gordo = codigo

    if peso < peso_mais_magro:
        peso_mais_magro = peso
        codigo_mais_magro = codigo

media_alturas = alturas / clientes
media_pesos = pesos / clientes


print('---RELAÇÃO DOS CLIENTES---')
print(f'Cliente mais alto:\nCódigo: {codigo_mais_alto}\nAltura: {altura_mais_alto / 100:.2f} m')
print(f'Cliente mais baixo:\nCódigo: {codigo_mais_baixo}\nAltura: {altura_mais_baixo / 100:.2f} m')     
print(f'Cliente mais gordo:\nCódigo: {codigo_mais_gordo}\nPeso: {peso_mais_gordo:.0f} kg')
print(f'Cliente mais magro:\nCódigo: {codigo_mais_magro}\nPeso: {peso_mais_magro:.0f} kg')   
print(f'Média de altura entre os clientes: {media_alturas / 100:.2f} m')  
print(f'Média de peso entre os clientes: {media_pesos:.0f} kg')


# #### 38. Um funcionário de uma empresa recebe aumento salarial anualmente: 
# 
# Sabe-se que:
# - Esse funcionário foi contratado em 1995, com salário inicial de R\$ 1.000,00;
# - Em 1996 recebeu aumento de 1,5\% sobre seu salário inicial;
# - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
# 
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

# In[129]:


ano_0 = 1995
ano = int(input('Ano atual: '))
salario = float(input('Salário do funcionário em 1995: R$ '))
aumento = 0.015

while ano_0 < ano:
    ano_0 += 1
    salario = salario + (aumento * salario)
    aumento *= 2
print(f'O salário do funcionário em {ano} é de: R$ {salario:.2f}')   


# #### 39. Faça um programa que leia dez conjuntos de dois valores
# 
# o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

# In[133]:


altura_mais_alto = 0
num_mais_alto = 0
altura_mais_baixo = 200
num_mais_baixo = 0

for i in range(1, 11):
    altura = int(input(f'Altura do aluno {i} em (cm): '))
    if altura > altura_mais_alto:
        num_mais_alto = i
        altura_mais_alto = altura
    if altura < altura_mais_baixo:
        num_mais_baixo = i
        altura_mais_baixo = altura

print(f'Aluno mais alto:\nNúmero: {num_mais_alto}\nAltura: {altura_mais_alto / 100:.2f} m')
print(f'Aluno mais baixo:\nNúmero: {num_mais_baixo}\nAltura: {altura_mais_baixo / 100:.2f} m')


# #### 40.Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# <pre>
# Foram obtidos os seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). 
# 
# Deseja-se saber:
# - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
# </pre>

# In[141]:


codigo = int(input('Código da cidade: '))
carros = int(input('Quantidade de veículos de passeio na cidade em 1999: '))
acidentes = float(input('Quantidade de acidentes de trânsito com vítimas em 1999: '))


indice_acidentes = acidentes / carros
maior_indice = indice_acidentes
codigo_maior_indice = codigo
menor_indice = indice_acidentes
codigo_menor_indice = codigo
soma = carros
soma_menos_2000_carros = 0
divisor_media_2000 = 1

if carros < 2000:
    soma_menos_2000_carros += acidentes
    divisor_media_2000 += 1 
a = 1
while (a < 5):
    codigo = int(input('Código da cidade: '))
    carros = int(input('Quantidade de veículos de passeio na cidade em 1999: '))
    acidentes = float(input('Quantidade de acidentes de trânsito com vítimas em 1999: '))
    indice_acidentes = acidentes / carros
    soma += carros
    if indice_acidentes > maior_indice:
        maior_indice = indice_acidentes
        codigo_maior_indice = codigo
    if indice_acidentes < menor_indice:
        menor_indice = indice_acidentes
        codigo_menor_indice = codigo
    if carros < 2000:
        soma_menos_2000_carros += acidentes
        divisor_media_2000 += 1

    a += 1
    media_carros = soma / a
    media_acidentes_menos_2000 = soma_menos_2000_carros / divisor_media_2000
print('--- REALAÇÃO DE VEÍCULOS E ACIDENTES EM 1999 ---')
print(f'Cidade com o menor índice de acidentes de trânsito:\nCódigo da cidade: {codigo_menor_indice}\nÍndice: {menor_indice * 100:.0f}%')
print(f'Cidade com o maior índice de acidentes de trânsito:\nCódigo da cidade: {codigo_maior_indice}\nÍndice: {maior_indice * 100:.0f}%')   
print(f'Média de veículos entre as 5 cidades: {media_carros:.1f}')
print(f'Média de acidentes em cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.1f}')

