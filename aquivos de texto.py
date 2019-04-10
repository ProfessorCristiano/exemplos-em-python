# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:22:10 2019

@author: cristiano_001325
"""

arq = open('arquivo1.txt', 'w')
texto = """
Lista de Alunos
---
João da Silva
José Lima
Maria das Dores
"""
arq.write(texto)
arq.close()

'''Se usar o tipo 'w' novamente ele subistitui o arquivo inteiro'''

arq = open('arquivo1.txt', 'w')
texto = []
texto.append('---\n')
texto.append('Nova Lista\n')
texto.append('---\n')
texto.append('Adilson\n')
texto.append('Kaique\n')
texto.append('---\n')
arq.writelines(texto)
arq.close()




'''Metodo alternativo de trabalhar com arquivos, 
   Este não precisa fechar o arquivo.
   Quando voltamos o recuo ele fecha automaticamente'''
   
'''OBS: Se usar o tipo 'a' ele Acrecenta informação ao arquivo'''

with open('arquivo1.txt', 'a') as arq:
    texto = []
    texto.append('---\n')
    texto.append('Mais alguns\n')
    texto.append('---\n')
    texto.append('Pedro Rodrigues Filho\n')
    texto.append('João Acácio Pereira da Costa\n')
    texto.append('Francisco de Assis Pereira\n')
    texto.append('---\n')
    arq.writelines(texto)
    

print("\n\n\nPrimeira Exibição\n\n\n")

arq = open('arquivo1.txt', 'r')
texto = arq.read()
print(texto)
arq.close()

print("\n\n\nSegunda Exibição\n\n\n")

arq = open('arquivo1.txt', 'r')
texto = arq.readlines()
for linha in texto :
    print(linha)
arq.close()


print("\n\n\nExibe Só as Três primeiras Linhas\n\n\n")

arq = open('arquivo1.txt', 'r')
linha=arq.readline()
print(linha)
linha=arq.readline()
print(linha)
linha=arq.readline()
print(linha)
arq.close()


print("\n\n\nExibe Só a Quinta Linha\n\n\n")

arq = open('arquivo1.txt', 'r')
texto = arq.readlines()
n=0
for linha in texto :
    n=n+1
    if(n==4):
        print(linha)
arq.close()

