''''
Universiade Aberta do Brasil
Tecnologias Educacionais
Introducao a algoritmos - 2019
autor: Raoni F. S. Teixeira

Este programa le tres numeros e ordena '''

a = int(input('Informe um número: '))
b = int(input('Informe um número: '))
c = int(input('Informe um número: '))

if a < b:
   mais_leve = a
   mais_pesada = b
else:
   mais_leve = b
   mais_pesada = a

if c < mais_leve:
   print(c, mais_leve, mais_pesada)
else:
   if(c < mais_pesada):
      print(mais_leve, c, mais_pesada)
   else:
      print(mais_leve, mais_pesada, c)
