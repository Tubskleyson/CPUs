#importações e funções úteis
from random import random
from time import sleep

def d(v):
    
    return int(v,16)

def h(v):
    if v < 0:
        x = '-'+hex(v)[3:]
    else:
        x = hex(v)[2:]
    x = x.upper()
    return x

class MP:

    def __init__(self):

        self.celulas = []
        
        #gerando células aleatórias
        l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        for i in range(256):
            celula = ''
            for j in range(3):
                x = random()
                y = int(x//0.0625)
                z = l[y]
                celula += z
            self.celulas += [celula]
            
        
        #Instruções para paridade(para teste)
        paridade = ['9FF','1FF','407','602','2FF','AFF','000','002']
        
        #instruções paa potência geral
        exp = ['9EF','9EE','1EE','529','1EF','52B','2ED','1EE','42D','527','2EE','1ED','2EC',
               '1EF','2EB','1EB','42D','517','2EB','1ED','3EC','2ED','81F','AED','000','A2D',
               '000','AEF','000','001']
        
        #instruções para quadrado
        exp2 = ['9DF','1DF','55D','2DD','2DE','1DE','461','55F','2DE','1DD','3DF','2DD','855',
                'ADF','000','ADD','000','001']
        
        #a paridade vai no ínicio
        for i in range(len(paridade)):
            self.celulas[i] = paridade[i]
            
        #a exponencial começa na célula 16
        for i in range(len(exp)):
            self.celulas[i+16] = exp[i]
        
        #0 quadrado começa na célula 80
        for i in range(len(exp2)):
            self.celulas[i+80] = exp2[i]

    
    #função para exibir MP
    def show(self):
        for i in self.celulas:
            print('-',i,'-')
    
    #função WRITE
    def busca(self, pos):
        try:
            i = pos-7
            i = pos
        except:
            i = d(pos)
            
        return(self.celulas[i])
    
    #função READ
    def inserir(self, x, pos):
        self.celulas[pos] = x
        print('> Inserindo', x, 'na célula',pos)

class CPU:

    def __init__(self):

        self.ci = '00'
        self.r0 = '000'
        self.ri = '000'


        self.m = MP()
    
    #execução de sequência de instruções baseado na posição inicial
    def exe(self,e):
        self.ci = e
        self.ri = self.m.busca(self.ci)

        c = self.ri[0]
        e = d(self.ri[1:])

        while c != '0':
            print('[%s] ' %self.ci, end='')

            jump = False
            
            #---------------Verificação da instrução na vez-----------#
            
            if c == '1':
                self.r0 = self.m.busca(e)
                print('> Buscando célula',e)
                
            elif c == '2':
                self.m.inserir(self.r0,e)
                
                
            elif c == '3':
                x = d(self.m.celulas[e])
                self.r0 = d(self.r0)
                self.r0 = h(self.r0 + x)
                print('> Somando...')
                
            elif c == '4':
                x = d(self.m.celulas[e])
                self.r0 = d(self.r0)
                self.r0 = h(self.r0 - x)
                print('> Subtraindo...')

            elif c == '5':
                print('> Verificando se o valor é nulo')
                if d(self.r0) == 0:
                    jump = True
                    self.ci = h(e)
                    

            elif c == '6':
                print('> Verificando se o valor é positivo')
                if d(self.r0) > 0:
                    jump = True
                    self.ci = h(e)
                    

            elif c == '7':
                print('> Verificando se o valor é negativo')
                if d(self.r0) < 0:
                    jump = True
                    self.ci = h(e)
                    

            elif c == '8':
                jump = True
                self.ci = h(e)

            elif c == '9':
                while True:
                    x = input('< Digite o valor hex: ')
                    x = x.upper()
                    l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
                    if any((i not in l) for i in x): print('[Valor não hexadecimal digitado]\n')
                    else: break
                self.m.inserir(x,e)
                

            elif c == 'A':
                v = self.m.busca(e)
                print('\n\n<-------------------------------------->\n')
                print('> Hex -',v,'\n> Dec -',d(v))
                print()
            
            #-----------------Houve Jump?------------------------#
            
            if not jump:
                x = d(self.ci)
                x += 1
                self.ci = h(x)
            else:
                print('> Jump')

            self.ri = self.m.busca(self.ci)
            c = self.ri[0]
            e = d(self.ri[1:])
            sleep(.1)


#Criação do objeto

pc = CPU()

#Menu Principal
while True:
    x = input('> Que operação deseja efetuar?\n> 1 - paridade\n> 2 - a ^ b\n> 3 - a ^ 2 \n> 4 - Sair\n< ')
    print()
    if x == '1': pc.exe('00')
    elif x == '2': pc.exe('10')
    elif x == '3': pc.exe('50')
    elif x == '4': break
    else: print('\n [Comando Inválido] \n')
