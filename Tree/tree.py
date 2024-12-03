class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
            # print('?')

    def busca(self, valor): # Busca e imprime o caminho da raiz até o nó!
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    
    def busca_caminho_inverso(self, valor): # Busca e imprime o caminho da raiz até o nó, MAIS INVERTIDA!
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca_caminho_inverso(valor)
    
    def busca_nivel_no(self, valor): # Busca o nivel do Nó!
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca_nivel_no(valor)
    
    def busca_soma_no(self, valor): # Retorna a soma da raiz até o determinado Nó!
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca_soma_no(valor)
    
    # InOrdem
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
    
    # PreOrdem
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()

    # PosOrdem
    def posOrdem(self):
            if self.raiz != None:
                self.raiz.posOrdem()
    
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
    
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()
    
    def altura(self): # Mostra a altura da árvore!
        if self.raiz != None:
            return self.raiz.altura()
    
    def h(self,valor): # Mostra a altura de um determinado nó!
        if self.raiz != None:
            return self.raiz.h(valor)
        
    def nivel(self, valor): # O nível ou profundidade, de um nó é o número de nós do caminho da raiz até o nó. O nível da raiz, é portanto, 1. 
         if self.raiz != None:
            return self.raiz.nivel(valor)
    
    def quant(self, valor): # Retornar a quantidade de nós com aquele elemento!
        if self.raiz != None:
            return self.raiz.quant(valor)
    
    def maisDir(self): # Retorna o maior valor da árvore, maior a direita!
        if self.raiz != None:
            return self.raiz.maisDir()
    
    def printCaminho(self, valor): # Busca e imprime o caminho da raiz até o nó!
        if self.raiz != None:
            return self.raiz.printCaminho(valor)

class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
                # print('*')
            else:
                self.esq.insere(valor)
                # print('+')
        else:
            if self.dir == None:
                self.dir = No(valor)
                # print('-')
            else:
                self.dir.insere(valor)        
                # print('#')
    
    def busca(self, valor): # Busca e imprime o caminho da raiz até o nó!
        if valor == self.info:
            print(self.info)
            return True
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                print(self.info)
                return self.esq.busca(valor)
        else:
            if self.dir is None:
                return False
            else:
                print(self.info)
                return self.dir.busca(valor)
    
    def busca_caminho_inverso(self, valor): # Busca e imprime o caminho da raiz até o nó, MAIS INVERTIDA!
        if valor == self.info:
            print(self.info)
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                self.esq.busca_caminho_inverso(valor)
                print(self.info)
        else:
            if self.dir is None:
                return False
            else:
                self.dir.busca_caminho_inverso(valor)
                print(self.info)
    
    def busca_com_validacao(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq is None:
                return 0
            else:
                aux = self.esq.busca(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
        else:
            if self.dir is None:
                return 0
            else:
                aux = self.dir.busca(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
                
    def busca_nivel_no(self, valor): # Busca o nivel do Nó!
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                return 1 + self.esq.busca_nivel_no(valor)
        else:
            if self.dir is None:
                return False
            else:
                return 1 + self.dir.busca_nivel_no(valor)
    
    def busca_soma_no(self, valor): # Retorna a soma da raiz até o determinado Nó!
        if valor == self.info:
            return self.info
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                return self.info + self.esq.busca_soma_no(valor)
        else:
            if self.dir is None:
                return False
            else:
                return self.info + self.dir.busca_soma_no(valor)
    
    def busca_descedentes(self, valor): # Retorna os descedentes de um determinado Nó!
        if valor == self.info:
            if self.esq != None:
                self.esq.inOrdem()
            if self.dir != None:
                self.dir.inOrdem()
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                print(self.info)
                return self.esq.busca_descedentes(valor)
        else:
            if self.dir is None:
                return False
            else:
                print(self.info)
                return self.dir.busca_descedentes(valor)
    
    def busca_descedentes_valor(self, valor): # Retorna o valor e todos seus descendentes!
        if valor == self.info:
            self.inOrdem()
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                print(self.info)
                return self.esq.busca_descedentes_valor(valor)
        else:
            if self.dir is None:
                return False
            else:
                print(self.info)
                return self.dir.busca_descedentes_valor(valor)
    
    # InOrdem
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end=" ")
        if self.dir != None:
            self.dir.inOrdem()
    
    def inOrdem_pares(self): # Retorna apenas os números pares!
        if self.esq != None:
            self.esq.inOrdem_pares()
        if self.info % 2 == 0:
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem_pares()
    
    def inOrdem_folhas(self): # Retorna apenas as folhas!
        if self.esq != None:
            self.esq.inOrdem_folhas()
        if self.dir == None and self.esq == None:
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem_folhas()
    
    # PreOrdem
    def preOrdem(self):
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()
    # PosOrdem
    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end=" ")
    
    # Ordem Inversa
    def qualOrdem(self):
        if self.dir is not None:
            self.dir.qualOrdem()
        print(self.info, end=" ")
        if self.esq is not None:
            self.esq.qualOrdem()

    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()
        
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
    
    def somaFolhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
    
    def altura(self): # Mostra a altura da árvore!
        hesq = hdir = -1
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)
    
    def h(self, valor): # Mostra a altura de um determinado nó!
        if valor == self.info:
             return self.altura()
        elif valor < self.info:
            if self.esq == None:
                 return False
            else:
                 return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)

    def nivel(self, valor): # O nível ou profundidade, de um nó é o número de nós do caminho da raiz até o nó. O nível da raiz, é portanto, 1.
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.nivel(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.nivel(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0

    def quant(self, valor): # Retornar a quantidade de nós com aquele elemento!
        if self.info == valor:
            total = 1
        else:
            total = 0

        if self.esq != None:
            total += self.esq.quant(valor)
        if self.dir != None:
            total += self.dir.quant(valor)

        return total
    
    def maisdir(self):
        if self.dir!=None:
            return self.dir.maisdir()
        else:
            return self.info
    
    def printCaminho(self,valor): # Busca e imprime o caminho da raiz até o nó!
        if valor == self.info:
            print(self.info)
            return True
        elif valor < self.info:
            if self.esq is None:
                return False
            else:
                print(self.info)
                return self.esq.printCaminho(valor)
        else:
            if self.dir is None:
                return False
            else:
                print(self.info)
                return self.dir.printCaminho(valor)