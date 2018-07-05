from os import system
from time import sleep

class MP:

    def __init__(self):

        self.linhas = list(range(10))

        for i in range(10):
            self.linhas[i] = list(range(10))
            for j in range(10):
                self.linhas[i][j] ='     0'


    def show(self):
        print(' >  ', end='')
        for i in range(10):
            print('      %d' %i, end='')
        print('\n >')
        for i in range(10):
            print(' >',i, end=' ')
            for j in self.linhas[i]:
                print(j,end=' ')
            print('\n >')
        print('\n >------------------------------------------------------------------------\n')

    def coo(self, y):
        y = str(y)
        if len(y)==1: y = '0'+ y
        
        l = int(y[0])
        c = int(y[1])

        return l,c

    def insere(self, x, y):
        l,c = self.coo(y)

        x = str(x)
        while len(x)<6: x = ' '+ x

        self.linhas[l][c] = x

    def pega(self, p):
        l,c = self.coo(p)
        return int(self.linhas[l][c])

        

class CPU:

    def __init__(s):

        s.acc = 0
        s.ci  = 0
        s.ri  = 0
        s.ins = 0
        s.op  = 0
        s.m   = MP()

    def jump(s):
        s.ci = int(s.op)
        s.jumped = True

    def status(s):
        print('\n > Acumulador           %5d <' %s.acc,
              '\n > Contador             %5d <' %s.ci,
              '\n > RI                   %5s <' %s.ri,
              '\n > Código de Instrução  %5d <' %s.ins,
              '\n > Operando             %5s <' %s.op,
              '\n \n > MEMÓRIA ---------------------------------------------------------------\n')
        s.m.show()

    def exe(s, l, oC):
        s.ci = oC

        s.flag = ' < Código vazio >'
        if l != None:
            for i in l:
                s.m.insere(i,oC)
                oC += 1
        w = 0

        while True:
            s.ri  = str(s.m.pega(s.ci))
            s.ins = int(s.ri[:-2])
            s.op  = s.ri[-2:]

            s.jumped = False

            
            if s.ins == 10:
                while True:
                    x = input(' < Digite o valor: ')
                    try: int(x); break
                    except: print('\n > Eu lido apenas com números inteiros \n')
                s.m.insere(x,s.op)

            elif s.ins == 11: print('\n >',s.m.pega(s.op))

            elif s.ins == 20: s.acc = s.m.pega(s.op)

            elif s.ins == 21: s.m.insere(s.acc,s.op)

            elif s.ins == 30: s.acc += s.m.pega(s.op)

            elif s.ins == 31: s.acc -= s.m.pega(s.op)

            elif s.ins == 32:
                s.flag = ' < Divisão por zero >'
                s.acc = int(s.acc // s.m.pega(s.op))

            elif s.ins == 33: s.acc *= s.m.pega(s.op)

            elif s.ins == 40: s.jump()

            elif s.ins == 41:
                if s.acc<0 : s.jump()

            elif s.ins == 42:
                if s.acc==0: s.jump()

            elif s.ins == 43: break

            else:
                s.flag = ' < Comando inválido na célula %s >' %str(s.ci)
                int('a')

            if not s.jumped: s.ci += 1

            w += 1
            if w == 3000:
                s.flag = ' < Loop infinito >'
                int('a')
        print('\n [ Fim da Execução ] ')
        s.status()

            
class Prog:

    def __init__(p):

        p.cpu = CPU()
        p.cel = 0
        potencia = [1099,1098,2098,4225,2099,4227,2197,2098,3129,4223,2198,2097,2196,2099,2195,
            2095,3129,4207,2195,2097,3096,2197,4015,1197,4300,1129,4300,1199,4300,1]

        for i in range(len(potencia)):
            x = str(potencia[i])
            p.cpu.m.insere(x,i)

        quad = [1089,2089,4263,2187,2186,2086,3167,4265,2186,2087,3089,2187,4055,1189,4300,1187,
                4300,1]

        for i in range(len(quad)):
            x = str(quad[i])
            p.cpu.m.insere(x,i+50)

        print(' >>>>>>>>>>>>>>> Simulador Simpletom <<<<<<<<<<<<<<<\n')
        print(' > Por favor, digite um instrução por vez.         <\n',
              '> Cada instrução deve conter no máximo 4 dígitos. <\n',
              '> Os dois primeiros dígitos informam o comando.   <\n',
              '> Os dois últimos indicam a célula a ser usada.   <\n',
              '> Digite "fim" quando terminar seu código.        <\n',
              '> Você tambémpode digitar "<" para apagar e       <\n',
              '> substituir a instrução anterior.                <\n',
              '> Eu indicarei do lado esquerdo em que célula     <\n',
              '> você está escrevendo.                           <\n')

        p.menu()

    def menu(p):

        print('\n >>>>>>>>>>>>>>>>>>>>>> Menu <<<<<<<<<<<<<<<<<<<<<<<',
              '\n > a - Começar o código!                           <',
              '\n > b - Executar código já escrito                  <',
              '\n > c - Ajuda                                       <',
              '\n > d - Exibir status                               <',
              '\n > e - Limpar memória                              <'
              '\n > f - Encerrar execução                           <')

        a = input('\n < ')

        if a == 'a':
            system('cls')
            try: p.run()
            except: print('\n [ Execução finalizada com 1 erro%s ] \n' %p.cpu.flag)
        elif a == 'b':
            c = 0
            while c < 3:
                b = input('\n > Em que célula começa este código? \n < ')
                try:
                    if len(b) > 2 or b == '' or p.cpu.m.pega(b) == 0: print(' [ Célula inválida ] ')

                    else:
                        print('\n [ Executando ] \n')
                        sleep(1)
                        try: p.cpu.exe(None,int(b)); break
                        except: print('\n [ Execução finalizada com 1 erro%s ] \n' %p.cpu.flag); break

                    c += 1
                except:
                    print('\n > A posição da célula deve ser um número inteiro')
            if c == 3:
                sleep(1)
                print('\n > ...')
                sleep(1)
                print(' > Eu acho que não é isso o que você quer, melhor eu voltar pro menu')
                sleep(2)
        elif a == 'c': p.ajuda()
        elif a == 'd': p.cpu.status()
        elif a == 'e': p.clean()
        elif a == 'f': print('\n > Ok, até mais'); sleep(2); return

        else: print(' [ Opção inválida ] ')

        p.menu()

        

    def run(p):
        print()
        l = []
        i = None
        j = 0
        while p.cpu.m.pega(j) != 0:
            if j == 99:
                sleep(2)
                print('\n > Memória cheia ')
                sleep(2)
                return
            j += 1
        p.cel = j
        oldC = p.cel
        
        while i != 'fim':
            i = input(' < %2d? ' %p.cel)
            try:
                int(i)
                if len(i)<=4:
                    l += [i]
                    p.cel += 1
                else:
                    print('\n > Já falei, suas intryções devem ter no máximo 4 dígitos\n')
            except:
                if i == '<':
                    if p.cel == 0: print('\n > Mas você acabou de começar\n')
                    else:
                        del l[-1]
                        p.cel -= 1
                        if p.cel < oldC: oldC = p.cel
                elif i != 'fim': print('\n > Seus comandos devem conter apenas números inteiros\n')

        print( '\n [ Executando ]\n')

        p.cpu.exe(l,oldC)
        p.reset()

    def reset(p):
        while True:
            w = input(' > Deseja criar outro código? [s/n] \n < ')
            w = w.lower()

            if w == 's':
                p.clean()
                print('\n > Reiniciando')
                break
                
            elif w == 'n':
                print('\n\n > OK, voltando para o menu')
                sleep(3)
                system('cls')
                return

            else:
                print('\n > Desculpa, não entendi', end='')

        system('cls')
        print(' > ------------------------------------------------------------- <')
        p.run()

    def clean(p):
        while True:
            z = input('\n > Deseja limpar a memória? [s/n] \n < ')
            z = z.lower()
            
            if z == 's':
                while True:
                    z = input('\n > Tem certeza? Todos os códigos serão perdidos. [s/n] \n < ')

                    if z == 's':
                        print('\n > OK, mas foi você que pediu')
                        p.cpu.m = MP(); p.cel = 0; break
                    elif z == 'n': print('\n > Ok então, vou mantwr a memória intacta');break
                    else: print('\n > Desculpa, não entendi', end='')
                break
            elif z == 'n': break
            else: print('\n > Desculpa, não entendi', end='')
        sleep(3)
        system('cls')


    def ajuda(p):
        print('\n > A ajuda está a caminho!')
        sleep(2)
        system('cls')
        print('\n <----------------------Comandos---------------------->',
              '\n <- 10        Pede um valor e insere ele numa célula ->',
              '\n <- 11      Printa o valor de uma determinada célula ->',
              '\n <- 20      Carrega o valor de uma célula para o ACC ->',
              '\n <- 21             Guarda o valor do ACC numa célula ->',
              '\n <- 30             Soma o valor de uma célula ao ACC ->',
              '\n <- 31          Subtrai o valor de uma célula do ACC ->',
              '\n <- 32         Divide o ACC pelo valor de uma célula ->',
              '\n <- 33     Multiplica o ACC pelo valor de uma célula ->',
              '\n <- 40      Pula para a instrução de uma dada célula ->',
              '\n <- 41           Pula se o valor do ACC for negativo ->',
              '\n <- 42               Pula se o valor do ACC for zero ->',
              '\n <- 43                Encerra a execução do programa ->')
        sleep(3)
        input('\n > Pronto para codificar agora? \n < ')
        print('\n > Não se preocupe, eu vou deixar essa lista aqui pra você')
        sleep(2)
        print(' > ------------------------------------------------------------- <')
        p.run()
        
p = Prog()


            
