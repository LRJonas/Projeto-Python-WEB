DROP TABLE IF EXISTS Produto;

CREATE TABLE Produto(
    sku varchar(150) PRIMARY KEY ,
    nome varchar(150),
    categoria varchar(255),
    preco varchar(50)
    
    );

INSERT INTO Produto (sku, nome, categoria, preco)
VALUES ("1", "teste", "Zé da Graça", "1");
