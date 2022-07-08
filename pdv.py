import tkinter as tk
from tkinter import ttk
import datetime as dt
from barcode import EAN13
import mysql.connector

##Categoria
categoria_nome = []
categoria_valor = []
text_categoria_nome = ""
label_categoria_nova_valor = 0
##############################
####SubCategoria##############
subcategoria_categoria_nome = []
subcategoria_valor = []
categoria_id = []
text_subcategoria_nome = ""
label_subcategoria_nova_valor = 0
##############################
####Produto##############
produto_categoria_nome = []
produto_subcategoria_nome = []
produto_valor = []
produto_categoria_id = []
produto_categoria_valor = []
produto_subcategoria_id = []
produto_subcategoria_valor = []
text_produto_nome = ""
label_produto_nova_valor = 0
##############################
janela = tk.Tk()

con = mysql.connector.connect(host='localhost',database='Produtos',user='Elamodas',password='elamodas10')

if con.is_connected():
    cursor = con.cursor()
# if con.is_connected():
#    cursor.close()
#    con.close()
#    print("Conexão ao MySQL foi encerrada")


########################Criar Categoria#############################################################
#Título da Janela
#Criação da função
def janela_categoria():
    categoria_nome = []
    categoria_valor = []
    text_categoria_nome = ""
    label_categoria_nova_valor = 0

    sql_select_Query = "select * from Categoria"
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for row in records:
        categoria_nome.append(row[1])
        categoria_valor.append(row[2])

    janela_categoria = tk.Toplevel()

    janela_categoria.title('Cadastro de categoria')
    
    label_categoria_nome = tk.Label(janela_categoria,text="Nome da Categoria")
    label_categoria_nome.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =1 )
    text_categoria_nome = tk.Entry(janela_categoria)
    text_categoria_nome.grid(row=1, column=1,padx = 10, pady=10, sticky='nswe', columnspan =3 )
    label_categoria_nova_valor = categoria_valor[-1] + 1  
    botao_cadastrar_categoria = tk.Button(janela_categoria,text="Salvar", command=lambda: [janela_categoria_sucesso(text_categoria_nome.get(),label_categoria_nova_valor), janela_categoria.destroy()])
    botao_cadastrar_categoria.grid(row=3,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)
    botao_voltar_categoria = tk.Button(janela_categoria,text="Voltar", command= janela_categoria.destroy)
    botao_voltar_categoria.grid(row=4,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)

def janela_categoria_sucesso(text_categoria_nome, label_categoria_nova_valor):
    val = (text_categoria_nome,label_categoria_nova_valor)
    sql_insert_categoria_Query = f"INSERT INTO Categoria (nome, valor) VALUES(%s,%s)"
    cursor.execute(sql_insert_categoria_Query,val)
    con.commit()
    janela_categoria_sucesso = tk.Toplevel()
    janela_categoria_sucesso.title('Categoria Cadastrada')
    label_categoria_sucesso = tk.Label(janela_categoria_sucesso,text="Categoria Criada com Sucesso")
    label_categoria_sucesso.grid(row=0, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    botao_categoria_sucesso = tk.Button(janela_categoria_sucesso,text="Voltar", command=janela_categoria_sucesso.destroy)
    botao_categoria_sucesso.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

################################################################################################################
########################Criar SubCategoria#############################################################
#Título da Janela
#Criação da função
def janela_subcategoria():
    subcategoria_categoria_nome = []
    subcategoria_valor = []
    categoria_id = []
    text_subcategoria_nome = ""
    label_subcategoria_nova_valor = 0
    sql_select_Query = "select * from Categoria"

    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for row in records:
        subcategoria_categoria_nome.append(row[1])
    
    sql_select_Query = "select * from SubCategoria"
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for row in records:
        subcategoria_valor.append(row[2])

    janela_subcategoria = tk.Toplevel()

    janela_subcategoria.title('Cadastro de SubCategoria')
    
    label_subcategoria_nome = tk.Label(janela_subcategoria,text="Nome da SubCategoria")
    label_subcategoria_nome.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =1 )
    text_subcategoria_nome = tk.Entry(janela_subcategoria)
    text_subcategoria_nome.grid(row=1, column=1,padx = 10, pady=10, sticky='nswe', columnspan =3 )
    label_subcategoria_nova_valor = subcategoria_valor[-1] + 1
    combobox_subcategoria_categoria = ttk.Combobox(janela_subcategoria, values=subcategoria_categoria_nome)  
    combobox_subcategoria_categoria.grid(row=2, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 4)
    botao_cadastrar_subcategoria = tk.Button(janela_subcategoria,text="Salvar", command=lambda: [janela_subcategoria_sucesso(text_subcategoria_nome.get(),label_subcategoria_nova_valor, combobox_subcategoria_categoria.get()),janela_subcategoria.destroy()])
    botao_cadastrar_subcategoria.grid(row=4,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)
    botao_voltar_subcategoria = tk.Button(janela_subcategoria,text="Voltar", command= janela_subcategoria.destroy)
    botao_voltar_subcategoria.grid(row=5,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)

def janela_subcategoria_sucesso(text_subcategoria_nome, label_subcategoria_nova_valor, label_categoria_valor):
    categoria_id = []
    janela_subcategoria_sucesso = tk.Toplevel()
    janela_subcategoria_sucesso.title('SubCategoria Cadastrada')
    sql_select_Query = f"select * from Categoria Where nome=%s"
    val=(label_categoria_valor,)
    cursor.execute(sql_select_Query,val)
    # get all records
    records = cursor.fetchall()
    for row in records:
        categoria_id.append(row[0])
    print(categoria_id[0])
    val = (text_subcategoria_nome,label_subcategoria_nova_valor, categoria_id[0])
    sql_insert_subcategoria_Query = f"INSERT INTO SubCategoria (nome, valor, categoria_id) VALUES(%s,%s,%s)"
    cursor.execute(sql_insert_subcategoria_Query,val)
    con.commit()
    label_subcategoria_sucesso = tk.Label(janela_subcategoria_sucesso,text="SubCategoria Criada com Sucesso")
    label_subcategoria_sucesso.grid(row=0, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    botao_subcategoria_sucesso = tk.Button(janela_subcategoria_sucesso,text="Voltar", command=janela_subcategoria_sucesso.destroy)
    botao_subcategoria_sucesso.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
##############################################################################################################
########################Criar Produto#############################################################
#Título da Janela
#Criação da função
def janela_produto():
    produto_categoria_nome = []
    produto_subcategoria_nome = []
    produto_valor = []
    produto_categoria_id = []
    produto_categoria_valor = []
    produto_subcategoria_id = []
    produto_subcategoria_valor = []
    text_produto_nome = ""
    label_produto_nova_valor = 0

    sql_select_Query = "select * from Categoria"
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for row in records:
        produto_categoria_nome.append(row[1])
    
    janela_produto = tk.Toplevel()

    janela_produto.title('Cadastro de Produto - Categoria')
    
    label_produto_nome = tk.Label(janela_produto,text="Nome do Produto")
    label_produto_nome.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =1 )
    text_produto_nome = tk.Entry(janela_produto)
    text_produto_nome.grid(row=1, column=1,padx = 10, pady=10, sticky='nswe', columnspan =3 )
    combobox_produto_categoria = ttk.Combobox(janela_produto, values=produto_categoria_nome)  
    combobox_produto_categoria.grid(row=2, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 4)
    botao_continuar_produto = tk.Button(janela_produto,text="Salvar", command=lambda: [janela_produto_subcategoria(text_produto_nome.get(), combobox_produto_categoria.get()),janela_produto.destroy()])
    botao_continuar_produto.grid(row=4,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)
    botao_voltar_produto = tk.Button(janela_produto,text="Voltar", command= janela_produto.destroy)
    botao_voltar_produto.grid(row=5,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)

def janela_produto_subcategoria(text_produto_nome, label_categoria_nome):
    produto_subcategoria_nome = []
    produto_categoria_id = []
    produto_categoria_valor = []
    produto_subcategoria_nome = []
    janela_produto_subcategoria = tk.Toplevel()
    janela_produto_subcategoria.title('Cadastrar Produto - SubCategoria')
    sql_select_Query = f"select * from Categoria Where nome=%s"
    val=(label_categoria_nome,)
    cursor.execute(sql_select_Query,val)
    # get all records
    records = cursor.fetchall()
    print(label_categoria_nome)

    for row in records:
        produto_categoria_id.append(row[0])
        produto_categoria_valor.append(row[2])
    print(produto_categoria_id[0])
    sql_select_Query = f"select * from SubCategoria Where categoria_id=%s"
    val=(produto_categoria_id[0],)
    cursor.execute(sql_select_Query,val)
    # get all records
    records = cursor.fetchall()
    for row in records:
        produto_subcategoria_nome.append(row[1])
    combobox_produto_subcategoria = ttk.Combobox(janela_produto_subcategoria, values=produto_subcategoria_nome)  
    combobox_produto_subcategoria.grid(row=2, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 4)
    label_quantidade_variacao = tk.Label(janela_produto_subcategoria,text="Quantidade de Variação")
    label_quantidade_variacao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =1 )
    text_quantidade_variacao = tk.Entry(janela_produto_subcategoria)
    text_quantidade_variacao.grid(row=1, column=1,padx = 10, pady=10, sticky='nswe', columnspan =3 )
    botao_sucesso_produto = tk.Button(janela_produto_subcategoria,text="Salvar", command=lambda: [janela_produto_sucesso(text_produto_nome,produto_categoria_id[0],combobox_produto_subcategoria.get(),text_quantidade_variacao.get(),produto_categoria_valor[0]),janela_produto_subcategoria.destroy()])
    botao_sucesso_produto.grid(row=3,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)
    botao_produto_subcategoria = tk.Button(janela_produto_subcategoria,text="Voltar", command=janela_produto_subcategoria.destroy)
    botao_produto_subcategoria.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

def janela_produto_sucesso(text_produto_nome, categoria_id, subcategoria_nome, text_quantidade_variacao,produto_categoria):
    codigo_barras_list = []
    produto_subcategoria_id = []
    produto_subcategoria_valor = []
    produto_valor = []
    janela_produto_sucesso = tk.Toplevel()
    janela_produto_sucesso.title('Cadastro do Produto com Sucesso')
    sql_select_Query = f"select * from SubCategoria Where nome=%s"
    val=(subcategoria_nome,)
    cursor.execute(sql_select_Query,val)
    # get all records
    records = cursor.fetchall()
    for row in records:
        produto_subcategoria_id.append(row[0])
        produto_subcategoria_valor.append(row[2])
    sql_select_Query = f"select * from Produto Where categoria_id=%s AND subcategoria_id=%s"
    val=(categoria_id, produto_subcategoria_id[0])
    cursor.execute(sql_select_Query,val)
    # get all records
    records = cursor.fetchall()
    sku = 0
    if len(records) ==0:
        produto_valor.append(int("200"+str(produto_categoria).zfill(3)+str(produto_subcategoria_valor[-1]).zfill(3)+"000"))
        sku = produto_valor[0]
    else:
        for row in records:
            produto_valor.append(row[6])
        sku = produto_valor[-1]+1
    codigo_barras = str(EAN13(str(sku)))
    if len(text_quantidade_variacao) == 0:
        val = (categoria_id,produto_subcategoria_id[0], sku, codigo_barras, text_produto_nome, sku)
        sql_insert_produto_Query = f"INSERT INTO Produto (categoria_id, subcategoria_id, sku, barcode, nome, ultimo_valor) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql_insert_produto_Query,val)
        codigo_barras_list.append(codigo_barras)
    else:
        quantidade_variacao = int(text_quantidade_variacao)
        while(int(quantidade_variacao) > 0):
            codigo_barras_list.append(codigo_barras)
            val = (categoria_id,produto_subcategoria_id[0], sku, codigo_barras, text_produto_nome, sku)
            sql_insert_produto_Query = f"INSERT INTO Produto (categoria_id, subcategoria_id, sku, barcode, nome, ultimo_valor) VALUES(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql_insert_produto_Query,val)
            quantidade_variacao = quantidade_variacao - 1
            sku = sku + 1
            codigo_barras = str(EAN13(str(sku)))
    con.commit()
    label_subcategoria_sucesso = tk.Label(janela_produto_sucesso,text="Produto Criado com Sucesso")
    label_subcategoria_sucesso.grid(row=0, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    label_codigo_barras = tk.Label(janela_produto_sucesso,text="Código de Barras")
    label_codigo_barras.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    listbox_codigo_barras = tk.Listbox(janela_produto_sucesso)
    listbox_codigo_barras.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    for codigo_barras_item in codigo_barras_list:
        listbox_codigo_barras.insert(tk.END,codigo_barras_item)
    botao_subcategoria_sucesso = tk.Button(janela_produto_sucesso,text="Voltar", command=janela_produto_sucesso.destroy)
    botao_subcategoria_sucesso.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

##############################################################################################################








botao_criar_categoria = tk.Button(janela,text="Criar Categoria", command=janela_categoria)
botao_criar_categoria.grid(row=0,column=0,padx = 10, pady=10,sticky='nswe', columnspan =4)

botao_criar_subcategoria = tk.Button(janela,text="Criar Subcategoria", command=janela_subcategoria)
botao_criar_subcategoria.grid(row=1,column=0,padx = 10, pady=10,sticky='nswe', columnspan =4)

botao_criar_subcategoria = tk.Button(janela,text="Criar Produto", command=janela_produto)
botao_criar_subcategoria.grid(row=2,column=0,padx = 10, pady=10,sticky='nswe', columnspan =4)

janela.title('Ferramenta de cadastro de materiais')
janela.mainloop()