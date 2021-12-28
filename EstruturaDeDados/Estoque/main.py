# Marcelo Henrique de Sousa Pinheiro
# Por gentileza enviar falhas e erros encontrados no meu e-mail: marcelo.pinheiro@edu.udesc.br
from estoque import ListaEstoque

estoque = ListaEstoque()

while True:
    print("[0] - Sair")
    print("[1] - Inserir um alimento no estoque")
    print("[2] - Imprimir o atual estoque")
    print("[3] - Consumir determinado alimento em estoque")
    print("[4] - Imprimir estoque mínimo dos alimentos")
    print("[5] - Alterar estoque mínimo de determinado alimento")
    op = int(input("Digite uma opção do menu: "))
    if op == 0:
        print("Encerrando.")
        break
    elif op == 1:
        estoque.push()
    elif op == 2:
        estoque.printEstoque()
    elif op == 3:
        estoque.consurmirAlimento()
    elif op == 4:
        estoque.printEstoqueMinimo()
    elif op == 5:
        estoque.alterarEstoqueMinimo()
    else:
        print("Opção digitada inválida.")