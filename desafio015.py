dias = float(input('Quantos dias ele foi alugado? '))
quant = float(input('Quantos km você percorreu? '))
prec = (dias  * 60) + (quant * 0.15)
print('O total é de R${:.2f}'.format(prec))
