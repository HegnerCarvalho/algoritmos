#Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
a=input('Digite o valor de A:')
a=int(a)

b=input('Digite o valor de B:')
b=int(b)

c=input('Digite o valor de C:')
c=int(c)

if a>b:
    print('O maior número é',a)

if a>c:
    print('O maior número é',a)

if b>a:
    print('O maior número é',b)

if b>c:
    print('O maior número é',b)

if c>a:
    print('O maior número é',c)

if c>b:
    print('O maior número é',c)
