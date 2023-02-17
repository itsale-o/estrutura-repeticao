#!/usr/bin/env python
# coding: utf-8

# # Estruturas de repetição

# #### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# In[ ]:


nota = float(input('Insira uma nota entre 0 e 10: '))

while not (0 <= nota <= 10):
    print('Nota inválida')
    nota = float(input('Insira uma nota entre 0 e 10: '))


# #### 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# In[ ]:


usuario = input('Nome de usuário: ')
senha = input('Senha: ')

while senha == usuario:
    print('Verifique se as informações estão corretas.\nInsira nome de usuário e senha novamente:')
    usuario = input('Nome de usuário: ')
    senha = input('Senha: ')


# #### 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
# 
# - ##### Nome: maior que 3 caracteres;
# - ##### Idade: entre 0 e 150;
# - ##### Salário: maior que zero;
# - ##### Sexo: 'f' ou 'm';
# - ##### Estado Civil: 's', 'c', 'v', 'd';

# In[ ]:


nome = input('Nome: ')
while len(nome) < 4:
    print('Nome inválido')
    nome = input('Nome: ')
    
idade = float(input('Idade: '))
while not (0 <= idade <= 150):
    print('Insira um valor válido para a idade')
    idade = float(input('Idade: '))
    
salario = float(input('Salário: R$ '))
while not salario > 0:
    print('Valor inválido para salário')
    salario = float(input('Salário: R$ '))

genero = input('Gênero (m ou f): ')
while not (genero == 'm' or genero == 'f'):
    print('Gênero inválido')
    genero = input('Gênero (m ou f): ')

estado_civil = input('Estado civil (s, c, d, v): ')
while not (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'd' or estado_civil == 'v'):
    print('Entrada inválida')
    estado_civil = input('Estado civil (s, c, d, v): ')


# #### 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# In[ ]:


a = 80000
b = 200000
tempo = 0

while a < b:
    a = a + (0.03 * a)
    b = b + (0.015 * b)
    tempo += 1
print(f'Serão necessário {tempo:.0f} anos para que a população do país A se iguale ou ultrapasse a população do país B')


# #### 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

# In[ ]:


a = float(input('População do país A: '))
taxa_a = float(input('Taxa de crescimento anual do país A (%): '))
b = float(input('População do país B: '))
taxa_b = float(input('Taxa de crescimento anual do país B (%): '))
tempo = 0

if a == b:
    print('A população dos dois países atualmente é a mesma')
else:
    if a < b:
        while a < b:
            a = a + ((taxa_a / 100) * a)
            b = b + ((taxa_b / 100) * b)
            tempo += 1
        print(f'Serão necessário {tempo:.0f} anos para que a população do país A se iguale ou ultrapasse a população do país B')
    else:
        while b < a:
            a = a + ((taxa_a / 100) * a)
            b = b + ((taxa_b / 100) * b)
            tempo += 1
        print(f'Serão necessário {tempo:.0f} anos para que a população do país B se iguale ou ultrapasse a população do país A')


# #### 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

# In[ ]:


for i in range (1,21):
    print (i)
for j in range (1, 21):
    print (j, end = ' ')


# #### 7. Faça um programa que leia 5 números e informe o maior número.

# In[ ]:


numeros = []
while len(numeros) < 5:
    num = float(input('Informe um número: '))
    numeros.append(num)
print(f'O maior número é o {max(numeros):.0f}')


# #### 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

# In[ ]:


numeros = []
while len(numeros) < 5:
    num = float(input('Informe um número: '))
    numeros.append(num)
soma = sum(numeros)
media = sum(numeros) / len(numeros)
print(f'Soma: {soma:.0f}\nMédia: {media:.0f}')


# #### 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# In[ ]:


for i in range(1, 51, 2):
    print(i, end = ' ')


# #### 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# In[ ]:


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

for i in range(num1 + 1, num2):
    print(i, end = ' ')


# #### 11. Altere o programa anterior para mostrar no final a soma dos números.

# In[ ]:


intervalo_numeros = []
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

for i in range(num1 + 1, num2):
    intervalo_numeros.append(i)
print(f'Soma do intervalo: {sum(intervalo_numeros)}')


# #### 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# 
# <pre>
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
# </pre>

# In[ ]:


numero = int(input('Informe um número de 1 a 10: '))

print(f'Tabuada de {numero}:')
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')


# #### 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

# In[ ]:


base = int(input('Base: '))
exp = int(input('Expoente: '))
potencia = 1

for i in range(exp):
    potencia *= base
    i += 1
print(f'{base} ^ {exp} = {potencia}')


# #### 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

# In[ ]:


par = 0
impar = 0

for i in range(10):
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'{par} números pares e {impar} números ímpares')


# #### 15. A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Faça um programa capaz de gerar a série até o n−ésimo termo.

# In[ ]:


n = int(input('Informe o termo da sequência de Fibonacci que deseja encontrar: '))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print(f'{n}° termo da sequência de Fibonacci: 1')
else:
    for i in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        i += 1
    print(f'{n}° termo da sequência de Fibonacci: {termo}')


# #### 16. A série de Fibonacci é formada pela seqüência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Faça um programa que gere a série até que o valor seja maior que 500

# In[ ]:


ultimo = 1
penultimo = 1
print(ultimo, end = ' ')
print(penultimo, end = ' ')
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo, end = ' ')
    else:
        print('\nO proximo valor será maior que 500')


# #### 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# 
# Ex.: 5! = 5.4.3.2.1 = 120

# In[ ]:


num = int(input('Informe um número para o cálculo de seu fatorial: '))
print(f'{num}! =', end = ' ')
for i in range(1, num):
    result = i * num
    num = result
print(result)

