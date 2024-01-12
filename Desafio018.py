import math
an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
print('O ãngulo de {} tem o SENO de {:.2f}'.format(an,seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an,cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem de TANGENTE de {:.2f}'.format(an,tangente))


