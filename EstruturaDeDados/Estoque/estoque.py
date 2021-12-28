#****      Marcelo Henrique de Sousa Pinheiro                                         ****#
#*******                                                                           *******#

from datetime import datetime as dt
from estoqueMinimo import ListaEstoqueMinimo

class Node:
    """Nó de implementação estoque alimentício."""
    def __init__(self):
        self.__nomeAlimento = None
        self.__quantidade = 0
        self.__validade = None
        self.__proximoAlimento = None

    def setNomeAlimento(self, nome_tipo):
        self.__nomeAlimento = nome_tipo
    def getNomeAlimento(self):
        return self.__nomeAlimento
    
    def setQuantidade(self, q):
        self.__quantidade = q
    def getQuantidade(self):
        return self.__quantidade
    
    def setValidade(self, validade):
        self.__validade = validade
    def getValidade(self):
        return self.__validade
    
    def setProximoAlimento(self, prox):
        self.__proximoAlimento = prox
    def getProximoAlimento(self):
        return self.__proximoAlimento
    
class ListaEstoque:
    """Classe que implementa a lista que conterá o estoque. Uma lista a parte está ancorada pela variável (atributo) estoqueMinimo"""
    def __init__(self):
        self.__inicioLista = None
        self.__fimLista = None
        self.estoqueMinimo = ListaEstoqueMinimo()

    def push(self):
        """Cadastro de um novo alimento em estoque."""
        novoAlimento = Node()
        if novoAlimento:
            novoAlimento.setNomeAlimento(input("Digite o nome/tipo do alimento: "))
            novoAlimento.setQuantidade(int(input("Digite a quantidade do alimento: ")))
            dataValidade = input("Digite a data de validade no formato DD/MM/YYYY: ")
            novoAlimento.setValidade(dt.strptime(dataValidade, "%d/%m/%Y"))
            if not (self.verificaAlimentoEmEstoque(novoAlimento.getNomeAlimento().lower())):
                self.estoqueMinimo.pushEstoqueMinimo(novoAlimento.getNomeAlimento())
            if not self.__inicioLista:
                novoAlimento.setProximoAlimento(None)
                self.__inicioLista = self.__fimLista = novoAlimento
            elif novoAlimento.getNomeAlimento().lower() <= self.__inicioLista.getNomeAlimento().lower():
                if novoAlimento.getNomeAlimento().lower() == self.__inicioLista.getNomeAlimento().lower():
                    if novoAlimento.getValidade() <= self.__inicioLista.getValidade():
                        novoAlimento.setProximoAlimento(self.__inicioLista)
                        self.__inicioLista = novoAlimento
                    else:
                        novoAlimento.setProximoAlimento(self.__inicioLista.getProximoAlimento())
                        self.__inicioLista.setProximoAlimento(novoAlimento)
                else:
                    novoAlimento.setProximoAlimento(self.__inicioLista)
                    self.__inicioLista = novoAlimento
            elif novoAlimento.getNomeAlimento().lower() >= self.__fimLista.getNomeAlimento().lower():
                if novoAlimento.getNomeAlimento().lower() == self.__fimLista.getNomeAlimento().lower():
                    if novoAlimento.getValidade() <= self.__fimLista.getValidade():
                        temp = self.__inicioLista
                        while temp.getProximoAlimento() != self.__fimLista:
                            temp = temp.getProximoAlimento()
                        temp.setProximoAlimento(novoAlimento)
                        novoAlimento.setProximoAlimento(self.__fimLista)
                        self.__fimLista = novoAlimento.getProximoAlimento()
                    else:
                        self.__fimLista.setProximoAlimento(novoAlimento)
                        self.__fimLista = novoAlimento
                else:
                    self.__fimLista.setProximoAlimento(novoAlimento)
                    self.__fimLista = novoAlimento
            else:
                ref_ant = self.__inicioLista
                while True:
                    if novoAlimento.getNomeAlimento().lower() <= ref_ant.getProximoAlimento().getNomeAlimento().lower():
                        if novoAlimento.getNomeAlimento().lower() == ref_ant.getProximoAlimento().getNomeAlimento().lower():
                            if novoAlimento.getValidade() < ref_ant.getProximoAlimento().getValidade():
                                novoAlimento.setProximoAlimento(ref_ant.getProximoAlimento())
                                ref_ant.setProximoAlimento(novoAlimento)
                                break
                            else:
                                novoAlimento.setProximoAlimento(ref_ant.getProximoAlimento().getProximoAlimento())
                                ref_ant.getProximoAlimento().setProximoAlimento(novoAlimento)
                                break
                        else:
                            novoAlimento.setProximoAlimento(ref_ant.getProximoAlimento())
                            ref_ant.setProximoAlimento(novoAlimento)
                            break
                    ref_ant = ref_ant.getProximoAlimento()
    
    def consurmirAlimento(self):
        """Consome/Reduz quantidade de determinado alimento em estoque."""
        if not self.__inicioLista:
            print("Estoque vazio.")
            return

        self.printEstoque()
        alimento = input("Digite o alimento que deseja consumir: ")
        quantidade = int(input("Digite a quantidade de [" + alimento + "] que deseja consumir: "))
        if quantidade > self.verificaQuantidadeDisponivel(alimento):
            print("Quantidade não disponível do alimento selecionado.")
        else:
            temp = self.__inicioLista
            if temp.getNomeAlimento().lower() == alimento.lower():
                if temp.getQuantidade() - quantidade < 0:
                    resto = (temp.getQuantidade() - quantidade) * -1
                    self.__inicioLista = self.__inicioLista.getProximoAlimento()
                    self.__inicioLista.setQuantidade(self.__inicioLista.getQuantidade() - resto)
                    if self.__inicioLista.getQuantidade() == 0:
                        self.__inicioLista = self.__inicioLista.getProximoAlimento()
                    if not self.__inicioLista:
                        self.__fimLista = self.__inicioLista
                    return
                elif (temp.getQuantidade() - quantidade) == 0:
                    print("Alimento " + self.__inicioLista.getNomeAlimento() + " consumido totalmente [Necessário repor estoque].")
                    self.__inicioLista = self.__inicioLista.getProximoAlimento()
                    return
                else:
                    temp.setQuantidade(temp.getQuantidade() - quantidade)
                    self.estoqueMinimo.verificaNecessidadeDeCompra(temp.getNomeAlimento(), temp.getQuantidade())
                    return
            while temp.getProximoAlimento():
                if temp.getProximoAlimento().getNomeAlimento().lower() == alimento.lower():
                    if (temp.getProximoAlimento().getQuantidade() - quantidade) < 0:
                        resto = (temp.getProximoAlimento().getQuantidade() - quantidade) * -1
                        temp.setProximoAlimento(temp.getProximoAlimento().getProximoAlimento())
                        temp.getProximoAlimento().setQuantidade(temp.getProximoAlimento().getQuantidade() - resto)
                        self.estoqueMinimo.verificaNecessidadeDeCompra(temp.getNomeAlimento(), temp.getQuantidade())
                    elif (temp.getProximoAlimento().getQuantidade() - quantidade) == 0:
                        print("Alimento " + temp.getProximoAlimento().getNomeAlimento() + " consumido totalmente [Necessário repor estoque].")
                        temp.setProximoAlimento(temp.getProximoAlimento().getProximoAlimento())
                    else:
                        temp.getProximoAlimento().setQuantidade(temp.getProximoAlimento().getQuantidade() - quantidade)
                        self.estoqueMinimo.verificaNecessidadeDeCompra(temp.getProximoAlimento().getNomeAlimento(), temp.getProximoAlimento().getQuantidade())
                    break
                temp = temp.getProximoAlimento()
    
    def verificaQuantidadeDisponivel(self, alimento):
        """Retorna um inteiro contendo a quantidade total de determinado alimento no estoque."""
        temp = self.__inicioLista
        quantidadeDisponivel = 0
        while temp:
            if temp.getNomeAlimento().lower() == alimento.lower():
                quantidadeDisponivel += temp.getQuantidade()
            temp = temp.getProximoAlimento()
        return quantidadeDisponivel

    def alterarEstoqueMinimo(self):
        """Faz a chamada da variável estoqueMinimo invocando a função de alteração da quantidade mínima."""
        if not self.__inicioLista:
            print("Estoque vazio.")
            return
        self.estoqueMinimo.printAll()
        alimento = input("Digite o alimento que deseja alterar o estoque mínimo: ")
        if not self.verificaAlimentoEmEstoque(alimento.lower()):
            print("Alimento inválido.")
            return
        self.estoqueMinimo.alterarQuantidadeMinima(alimento)
    
    def printEstoqueMinimo(self):
        if not self.__inicioLista:
            print("Estoque vazio.")
        self.estoqueMinimo.printAll()

    def verificaAlimentoEmEstoque(self, alimento):
        temp = self.__inicioLista
        estoque = []
        while temp:
            estoque.append(self.__inicioLista.getNomeAlimento().lower())
            temp = temp.getProximoAlimento()
        return alimento in estoque

    def printEstoque(self):
        if not self.__inicioLista:
            print("Estoque vazio.")
            return
        temp = self.__inicioLista
        strEstoque = " ________________________________________________\n"
        strEstoque += "|                 ESTOQUE                        |\n"
        strEstoque += "|________________________________________________|\n"
        strEstoque += "|[nome/tipo]        [Qnt.]        [validade]     |\n"
        strEstoque += "|________________________________________________|\n"
        while temp:
            strEstoque += '  ->  ' + temp.getNomeAlimento() + '      '
            strEstoque +=  str(temp.getQuantidade()) + '      '
            strEstoque +=  str((temp.getValidade())) + '\n'
            temp = temp.getProximoAlimento()
        print(strEstoque)
