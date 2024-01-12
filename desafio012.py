prod = float(input('Digite o valor do produto: R$ '))
desc = prod - (prod * 5 / 100)
print('O Valor do produto sem desconto é {} e com desconto fica em {}'.format(prod,desc))