USE Produtos;

CREATE TABLE Categoria (
    id integer not null auto_increment,
    nome varchar(200),
    valor integer,
    PRIMARY KEY (id)
);

CREATE TABLE SubCategoria (
    id integer not null auto_increment,
    nome varchar(200),
    valor integer,
    categoria_id integer not null,
    PRIMARY KEY (id),
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

CREATE TABLE Produto (
    id integer not null auto_increment,
    categoria_id integer not null,
    subcategoria_id integer not null,
    sku          varchar(100),
    barcode      varchar(15),
    nome         varchar(200),
    ultimo_valor bigint,
    PRIMARY KEY (id),
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id),
    FOREIGN KEY (subcategoria_id) REFERENCES SubCategoria(id)
);


INSERT INTO Categoria (nome, valor) VALUES('Blusa',01);
INSERT INTO SubCategoria (nome, valor, categoria_id) VALUES('Blusa Cropped',01, 01);