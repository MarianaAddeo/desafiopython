dia = float(input('Quantos dias você alugou o carro? '))
quant = float(input('Quantos km você andou? '))
valor = dia * 60
andar = quant * 0.15
preco = valor + andar
print('O total é de R%{:.2f}'.format(preco))
