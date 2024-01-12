import math
cat = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hipo = math.hypot(cat, adj)
print('O valor da hipotenusa é de {}'.format(hipo))
