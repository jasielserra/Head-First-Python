# -*- coding: utf-8 -*-
'''
Implementa uma pilha  que herda da lista predefinida do Python.

'''



class StackList(list):
    
	def __init__(self, item=[]):
		list.__init__([])
		self.extend(item)
		
	def isEmpty(self):
		return (self == [])
