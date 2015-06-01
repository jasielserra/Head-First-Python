# -*- coding: utf-8 -*-
'''
Implementa uma pilha com listas.
Esconde detalhes de implementação fornecendo
uma interface mais simples, ou mais padronizada.

'''
class Stack:
	def __init__(self):
		self.items = []
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	    
	def isEmpty(self):
		return (self.items == [])
