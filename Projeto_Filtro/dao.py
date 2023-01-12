from database import Database
from entidades import Produto
from flask import render_template

class ProdutoDao:
    def save (self, produto):
        conn= Database.get_conection()
        conn.execute(
            f"""
            INSERT INTO Produto(sku, nome, categoria, preco )
            VALUES (?, ?, ?, ?)
            """,
            (
                
                produto.sku,
                produto.nome,
                produto.categoria,
                produto.preco
            )
        )
        conn.commit()
        conn.close()

    def update(self, produto):
        
        conn = Database.get_conection()
        conn.execute(
            f"""
            UPDATE Produto SET nome = ?, categoria = ?, preco = ?
            WHERE sku = ?
            """,
            (
                produto.nome,
                produto.categoria,
                produto.preco,
                produto.sku
                
            )
        )
        conn.commit()
        conn.close()

   

    def find_all(self):
        conn = Database.get_conection()
        res = conn.execute("""
        SELECT sku, nome, categoria, preco FROM Produto
        """
        )
        
        results = res.fetchall()
        
        results = [
            { 
                "sku": produto[0], 
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]
                
            } for produto in results]

        conn.close()
        return results

    def delete(self,sku):
       
        conn = Database.get_conection()
        conn.execute(
            
            f"""
            DELETE FROM Produto WHERE sku = {sku}
            """
        )
        conn.commit()
        conn.close()

    def get_produto(self, sku):
        conn = Database.get_conection()
        res = conn.execute(f"""SELECT sku, nome, categoria, preco FROM Produto WHERE sku = {sku}""")
        row = res.fetchone()
        
       
        produto = produto( 
            row[1],
            row[2],
            sku = row[0],
            nome = row[3],
            categoria = row[4],
            preco = row[5]  
            
        )
        conn.close()

    def busca_sku(self, sku):
        conn= Database.get_conection()
        res = conn.execute(f"""SELECT * FROM Produto WHERE sku LIKE '{sku}'""")
       
        results = res.fetchall()
        
        results = [
            { 
                "sku": produto[0], 
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]
                
            } for produto in results]

        conn.close()
        
        return results

    def busca_nome(self, nome):
        conn= Database.get_conection()
        res = conn.execute(f"""SELECT * FROM Produto WHERE nome LIKE '%{nome}%'""")
        
        results = res.fetchall()
        
        
        results = [
            { 
                "sku": produto[0], 
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]

            } for produto in results]



        conn.close()
        
        return results

    def busca_preco(self, preco):
        conn= Database.get_conection()
        res = conn.execute(f"""SELECT * FROM Produto WHERE preco LIKE '{preco}'""")
        results = res.fetchall()
        
        results = [
            { 
                "sku": produto[0], 
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]

            } for produto in results]

        conn.close()
        
        return results

    def busca_categoria(self, categoria):
        conn= Database.get_conection()
        res = conn.execute(f"""SELECT * FROM Produto WHERE categoria LIKE '%{categoria}%'""")
        results = res.fetchall()
        
        results = [
            { 
                "sku": produto[0], 
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]

            } for produto in results]

        conn.close()
        
        return results

    def save_csv(self, produto):
        conn= Database.get_conection()
        conn.execute(
            f"""
            INSERT INTO Produto(sku, nome, categoria, preco)
            VALUES (?, ?, ?, ?)
            """,
            (
                
                produto.sku,
                produto.nome,
                produto.categoria,
                produto.preco
                
            )
        )
        conn.commit()
        conn.close()




    
    if __name__ == '__main__':
        from entidades import Produto
        from dao import ProdutoDao

        dao= ProdutoDao()
        teste= Produto(1, "teste","teste", 1)
        dao.save(teste)
