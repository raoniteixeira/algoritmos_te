''''
Universiade Aberta do Brasil
Tecnologias Educacionais
Introducao a algoritmos - 2019
autor: Raoni F. S. Teixeira

Este programa le tres nuneros e encontra e imprime o maior deles
Observe a estrutura repetitiva da solução'''

num = int(input('Informe um número: '))
maior = num;

num = int(input('Informe um número: '))
if maior < num:
    maior = num

num = int(input('Informe um número: '))
if maior < num:
    maior = num

print("O maior número é: ", maior);
