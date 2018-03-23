#Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
a=input('Digite a nota do trabalho:')
a=int(a)

b=input('Digite a nota da prova:')
b=int(b)

x=(a+b)/2

if x>=60:
    print('Aprovado')

else:
    print('Reprovado')
