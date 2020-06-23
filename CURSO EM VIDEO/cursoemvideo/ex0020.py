from math import radians, sin, cos, tan
a = float(input('Informe o valor do ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O ângulo {:.2f} possui Seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f}'. format(a, sen, cos, tan))
