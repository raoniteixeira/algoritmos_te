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
