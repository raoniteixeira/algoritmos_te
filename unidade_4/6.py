''''
Universiade Aberta do Brasil
Tecnologias Educacionais
Introducao a algoritmos - 2019
autor: Raoni F. S. Teixeira

Este programa le n numeros e encontra e imprime o maior deles
Observe a estrutura repetitiva da solução'''

n = int(input('Quantos números serão lidos? '))
num = int(input('Informe um número: '))
maior = num;
i = 1
while i <= n-1:
    num = int(input('Informe um número: '))
    if maior < num:
        maior = num
    i = i + 1

print("O maior número é: ", maior);
