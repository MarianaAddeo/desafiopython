cat = float(input('Comrpimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hipo =  (cat ** 2 + adj ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
