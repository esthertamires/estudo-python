"""Classe é uma forma diferente de construir o codigo
Funciona quando esta se criando um sistema mais complexo"""


"""Geralmente começa com a letra maiscula"""
class Vendedor(): 
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
    
    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f"{self.nome} Bateu a meta")
        else:
            print(f"{self.nome} Não bateu a meta")

nome_vendedor = input("Qual o nome do vendedor? ")
vendedor1 = Vendedor(nome_vendedor)
vendas = int(input(f"Quanto o vendedor {nome_vendedor} vendeu? "))
vendedor1.vendeu(vendas)
vendedor1.bateu_meta(800)
"""print("EU VOU CONSEGUIR!!")"""
