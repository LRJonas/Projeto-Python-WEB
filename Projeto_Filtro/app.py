from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from entidades import Produto
from dao import ProdutoDao

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastrar", methods=["GET"])
def cadastrar():
    
    return render_template('cadastro.html')

@app.route("/cadastrar/new", methods=["POST"])
def produto_create():
    #id=request.form.get("id")
    sku=request.form.get("sku")
    nome=request.form.get("nome")
    categoria=request.form.get("categoria")
    preco=request.form.get("preco")

    produto = Produto(sku, nome, categoria, preco)

    dao = ProdutoDao()
    dao.save(produto)

    return render_template('index.html')

@app.route("/listar", methods=["GET"])
def listar():
    dc = ProdutoDao()
    produtos = dc.find_all()
    return render_template("cadastro_list.html", produtos=produtos)

@app.route("/update", methods=["GET"])
def update():
    
    return render_template('update.html')

@app.route("/update/new", methods=["POST"])
def produto_update():
    sku=request.form.get("sku")
    nome=request.form.get("nome")
    categoria=request.form.get("categoria")
    preco=request.form.get("preco")
    

    produto = Produto(sku, nome, categoria, preco)
    
    dao=ProdutoDao()
    dao.update(produto)

    return render_template("sucesso.html")

@app.route("/deletar", methods=["GET"])
def produto_delete():

    return render_template("deletar.html")

@app.route("/deletar/delete", methods=["POST"])
def produto_deletar():

    sku=request.form.get("sku")

    #produto=Produto(id)
    

    dao = ProdutoDao()
    dao.delete(sku)

    return render_template("sucesso.html")

@app.route("/buscar", methods=["GET"])
def produto_busca():

    return render_template("busca_produto.html")

@app.route("/busca/nome", methods=["POST"])
def busca_nome():
    produtos=Produto()
    nome=request.form.get("nome")
    
    dao=ProdutoDao()
    produtos= dao.busca_nome(nome)
    contador=len(produtos)

    return render_template("busca_list.html", produtos=produtos, contador=contador)

@app.route("/busca/preco", methods=["POST"])
def busca_preco():
    produtos=Produto()
    preco=request.form.get("preco")
    
    
    dao=ProdutoDao()
    produtos= dao.busca_preco(preco)
    contador=len(produtos)


    return render_template("busca_list.html", produtos=produtos, contador=contador)

@app.route("/busca/sku", methods=["POST"])
def busca_sku():
    produtos=Produto()
    sku=request.form.get("sku")
    
    
    dao=ProdutoDao()
    produtos= dao.busca_sku(sku)

    return render_template("busca_list.html", produtos=produtos)

@app.route("/busca/categoria", methods=["POST"])
def busca_categoria():
    produtos=Produto()
    categoria=request.form.get("categoria")
    
    
    dao=ProdutoDao()
    produtos= dao.busca_categoria(categoria)
    contador=len(produtos)


    return render_template("busca_list.html", produtos=produtos, contador=contador)


if __name__ == "__main__":
    app.run(debug=True)