# Marcelo Henrique de Sousa Pinheiro (c) <marcelo.pinheiro@edu.udesc.br>

class NodeEstoqueMinimo():
    def __init__(self):
        self.__nomeAlimento = None
        self.__estoqueMinimo = 0
        self.__proxAlimento = None
    
    def setNomeAlimento(self, nome):
        self.__nomeAlimento = nome
    def getNomeAlimento(self):
        return self.__nomeAlimento
    def setEstoqueMinimo(self, estoqueMin):
        self.__estoqueMinimo = estoqueMin
    def getEstoqueMinimo(self):
        return self.__estoqueMinimo
    def setProxAlimento(self, proxAlimento):
        self.__proxAlimento = proxAlimento
    def getProxAlimento(self):
        return self.__proxAlimento

class ListaEstoqueMinimo():
    def __init__(self):
        self.__inicioLista = None
        self.__fimLista = None

    def pushEstoqueMinimo(self, alimento):
        novoEstoqueMinimo = NodeEstoqueMinimo()
        if novoEstoqueMinimo:
            novoEstoqueMinimo.setNomeAlimento(alimento)
            novoEstoqueMinimo.setEstoqueMinimo(int(input("Digite o estoque mínimo para o alimento: ")))
            if not self.__inicioLista:
                self.__inicioLista = novoEstoqueMinimo
                self.__fimLista = novoEstoqueMinimo
            elif novoEstoqueMinimo.getNomeAlimento() < self.__inicioLista.getNomeAlimento():
                novoEstoqueMinimo.setProxAlimento(self.__inicioLista)
                self.__inicioLista = novoEstoqueMinimo
            elif novoEstoqueMinimo.getNomeAlimento() > self.__fimLista.getNomeAlimento():
                self.__fimLista.setProxAlimento(novoEstoqueMinimo)
                novoEstoqueMinimo.setProxAlimento(None)
                self.__fimLista = novoEstoqueMinimo
            else:
                ref_anterior = self.__inicioLista
                while True:
                    if novoEstoqueMinimo.getNomeAlimento() < ref_anterior.getProxAlimento().getNomeAlimento():
                        novoEstoqueMinimo.setProxAlimento(ref_anterior.getProxAlimento())
                        ref_anterior.setProxAlimento(novoEstoqueMinimo)
                        break
                    ref_anterior = ref_anterior.getProxAlimento()

    def verificaNecessidadeDeCompra(self, alimento, quantidadeDisponivel):
        temp = self.__inicioLista
        while temp:
            if temp.getNomeAlimento().lower() == alimento.lower():
                if temp.getEstoqueMinimo() > quantidadeDisponivel:
                    print("Necessário comprar " + str(temp.getEstoqueMinimo() - quantidadeDisponivel) + " de " + temp.getNomeAlimento())
                else:
                    return
            temp = temp.getProxAlimento()

    def alterarQuantidadeMinima(self, alimento):
        temp = self.__inicioLista
        while temp:
            if temp.getNomeAlimento().lower() == alimento.lower():
                temp.setEstoqueMinimo(int(input(f"Digite a nova quantidade do alimento [{str(temp.getNomeAlimento())}]: ")))
            temp = temp.getProxAlimento()
        self.printAll()
    
    def printAll(self):
        strEstoque = " ________________________________________________\n"
        strEstoque += "|                 ESTOQUE MÍNIMO                 |\n"
        strEstoque += "|________________________________________________|\n"
        strEstoque += "| [nome/tipo]                   [Estoque Mínimo] |\n"
        strEstoque += "|________________________________________________|\n"
        temp = self.__inicioLista
        while temp:
            strEstoque += f"|   {temp.getNomeAlimento()}                     {temp.getEstoqueMinimo()}\n"
            temp = temp.getProxAlimento()
        print(strEstoque)