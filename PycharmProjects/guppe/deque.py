"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.


"""

from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y')
print(deq)

deq.appendleft('y')  # Podemos adicionar elementos no inicio da lista
print(deq)

print(deq.pop())
print(deq)

print(deq.popleft())  # Podemos retirar elementos do inicio da lista
print(deq)

