import os.path
import json

def printarMenu():
    print("""
        Escolha sua opção:
        1. Cadastrar Livro
        2. Consulta Estoque (Busca por Título)
        3. Consulta Estoque (Busca por ISBN)
        4. Vender um Livro
        5. Consultar Saldo da loja
        6. Salvar Dados
        9. Sair
    """)

def cadastraLivro(titulo, isbn, valor, QuantidadeEstoque):
    livro = [titulo, isbn, valor, QuantidadeEstoque]
    base = ["Titulo", "ISBN", "Valor", "QuantidadeEstoque"]
    novolivro = dict(zip(base, livro))
    return novolivro

def consultaEstoqueTitulo(EstoqueLivros, titulo):
    alert = True
    for x in range(len(EstoqueLivros)):
        if titulo == EstoqueLivros[x]['Titulo']:
            print("ISBN: " + EstoqueLivros[x]['ISBN'])
            print("Título: " + EstoqueLivros[x]['Titulo'])
            print("Valor: " + str(EstoqueLivros[x]['Valor']))
            print("Quantidade em estoque: " + str(EstoqueLivros[x]['QuantidadeEstoque']))
            alert = False 
    if alert:
        print("Não foi encontrado um livro com o Título digitado!")

def consultaEstoqueISBN(EstoqueLivros, isbn):
    alert = True
    for x in range(len(EstoqueLivros)):
        if isbn == EstoqueLivros[x]['ISBN']:
            print("ISBN: " + EstoqueLivros[x]['ISBN'])
            print("Título: " + EstoqueLivros[x]['Titulo'])
            print("Valor: " + str(EstoqueLivros[x]['Valor']))
            print("Quantidade em estoque: " + str(EstoqueLivros[x]['QuantidadeEstoque']))
            alert = False 
    if alert:
        print("Não foi encontrado um livro com o ISBN digitado!")

def venderLivro(isbn, qtd, saldo):
    alert = True
    for x in range(len(EstoqueLivros)):
        if isbn == EstoqueLivros[x]['ISBN']:
            alert = False
            if qtd > EstoqueLivros[x]['QuantidadeEstoque']:
                print("A quantidade solicitada é maior que de estoque!")
            else:
                EstoqueLivros[x]['QuantidadeEstoque'] -= qtd
                saldo += (qtd*EstoqueLivros[x]['Valor'])
                return saldo
    if alert:
        print("Não foi encontrado um livro com o ISBN digitado!")

def consultaSaldo(saldo):
    print("Saldo = R$" + str(saldo))

def salvarDados(EstoqueLivros, saldo):
    salvarestoque = open("estoque.txt", "w")
    salvarestoque.write(json.dumps(EstoqueLivros))
    salvarestoque.close()
    salvarsaldo = open("saldo.txt", "w")
    salvarsaldo.write(str(saldo))
    salvarsaldo.close()

    print("Os dados foram salvos")

def verificaEstoque():
    if os.path.isfile('estoque.txt'):
        with open("estoque.txt") as leitura:
            estoque = json.load(leitura)
        return estoque

def verificaSaldo():
    if os.path.isfile('Saldo.txt'):
        saldo = open("Saldo.txt","r")
        saldo = saldo.read()
        saldo = float(saldo)
        return saldo

op = 0

try:
    estoque = verificaEstoque()
    EstoqueLivros = estoque
except:
    print ("Não foi detectado estoque!")
    EstoqueLivros = []

try:
    saldo = verificaSaldo()
except:
    print("Não foi detectado Saldo!")

while op != 9:
    printarMenu()
    try:
        op = int(input())
    except:
        print("Opção digitada inválida")
    if op == 1:
        isbn = input("Digite o ISBN do livro: ")
        titulo = input("Digite o Título do livro: ")
        valor = float(input("Digite o Valor unitário: "))
        qtd = int(input("Digite a quantidade em estoque: "))
        nexiste = True
        for x in range(len(EstoqueLivros)):
            if isbn in EstoqueLivros[x]['ISBN']:
                EstoqueLivros[x]['QuantidadeEstoque']+=qtd
                nexiste = False
        if nexiste:
            EstoqueLivros.append(cadastraLivro(titulo, isbn, valor, qtd))
    elif op ==2:
        titulo = input("Qual o título do livro? >>")
        consultaEstoqueTitulo(EstoqueLivros, titulo)
    elif op ==3:
        isbn = input("Qual o ISBN do livro? >>")
        consultaEstoqueISBN(EstoqueLivros, isbn)
    elif op ==4:
        isbn = input("Qual o ISBN do livro a ser vendido? >> ")
        qtd = int(input("Qual a Quantidade de livros a serem vendidos? >> "))
        saldo = venderLivro(isbn, qtd, saldo)
    elif op ==5:
        consultaSaldo(saldo)
    elif op ==6:
        salvarDados(EstoqueLivros, saldo)
    elif op ==9:
        print("Volte mais vezes!")
    else:
        print("opção digitada não confere!")
    
