#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome
#separadamente

r = str(input('Digite o seu nome completo: ')).strip()
nome = r.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é{}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
