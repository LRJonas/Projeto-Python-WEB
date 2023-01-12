import csv
from dao import ProdutoDao
from entidades import Produto


with open ("lista-500.csv", "r") as arquivo:
   arquivo_csv =csv.reader(arquivo)
    
   dao=ProdutoDao()
   for i, linha in enumerate(arquivo_csv):
      if i == 0:
         print (linha)
         
      else:
         #print (linha)
         
         sku=linha[0]
         #print (sku)
         nome=linha[1]
         #print (nome)
         categoria=linha[2]
         #print (categoria)
         preco=linha[3]
         #print (preco)

         produto=Produto(sku, nome, categoria, preco)
         dao.save_csv(produto)
            
