from datetime import *
from random import randint
import numpy as np
import time
from intervalo import *


class Aia:

    def __init__(self,janelaRelacao):
        self.janela = janelaRelacao
        self.arrayPontosTemporaisTimestamp = []
        self.timestampIntervalo = Interval()
        self.arrayIntervalosOrdenados = []
        lifetime = [] #é a lista de todas as datas onde os intervalos temporais se inciam




    def constroiTimeStamp(self,arrayDeTempos): # analisa todos os tempos dos intervalos e unifica em um lifetime
        self.arrayPontosTemporaisTimestamp = arrayDeTempos
        np.unique(self.arrayPontosTemporaisTimestamp).tolist() # numpy.unique remove os elementos duplicados (ja ordena tb)
        self.timestampIntervalo.t_i = arrayDeTempos[0]
        self.timestampIntervalo.t_f = arrayDeTempos[len(arrayDeTempos)-1]



    def listaRelacoesPossiveis(self):
        print("starts, overlaps, meets, before, finishes, equal, during")




    def geraUmaDataAleatoria(self,dataSeed = date.today(),range = 900):

        novaData = date.fromordinal(dataSeed.toordinal() + randint(-range, range))  # hoje + 45 dias</pre>
        return novaData


    def identificaRelacao(self,i1,i2):
        if  (   i1.t_i == i2.t_i
            and i1.t_f == i2.t_f   ):
            print("equal(1,2)")


        elif(   i1.t_i == i2.t_i
            and i1.t_f < i2.t_f    ):
            print("starts(1,2)")
        elif(   i1.t_i == i2.t_i
            and i1.t_f > i2.t_f    ):
            print("started_by(1,2)")


        elif(   i1.t_f == i2.t_f
            and i1.t_i > i2.t_i    ):
            print("finishes(1,2)")
        elif(   i1.t_f == i2.t_f
            and i1.t_i < i2.t_i    ):
            print("finished_by(1,2)")


        elif(   i1.t_f == i2.t_i   ):
            print("meets(1,2)")
        elif(   i1.t_i == i2.t_f   ):
            print("met_by(1,2)")


        elif(   i1.t_f <  i2.t_i   ):
            print("before(1,2)")
        elif (i1.t_f > i2.t_i):
            print("after(1,2)")


        elif(   i1.t_i < i2.t_i
            and i1.t_f >  i2.t_i
            and i1.t_f <  i2.t_f   ):
            print("overlaps(1,2)")
        elif(   i1.t_i < i2.t_i
            and i1.t_f >  i2.t_i
            and i1.t_f <  i2.t_f   ):
            print("is_overlapped_by(1,2)")


        elif(   i1.t_i > i2.t_i
            and i1.t_f < i2.t_f    ):
            print("during(1,2)")

        elif(   i1.t_i > i2.t_i
            and i1.t_f < i2.t_f    ):
            print("contains(1,2)")

        else:
            print("There is any relation between x and y!")



    def executaAIA(self):
        i1 = Interval()
        i2 = Interval()
        for int in self.arrayIntervalosOrdenados:#para cada um dos intervalos
            print("Data selecionada",date.fromordinal(int[0]))
            i1.t_i = date.fromordinal(int[0])
            i1.t_f = date.fromordinal(int[1])
            #procurar todos os intervalos que se iniciem em até 1 janela após ele.
            selecao = [elem for elem in self.arrayIntervalosOrdenados if (elem[0] >= int[0] and (elem[0]-self.janela) <= int[0]) ]
            for s in selecao:
                print(date.fromordinal(s[0]))
                i2.t_i = date.fromordinal(s[0])
                i2.t_f = date.fromordinal(s[1])
                self.identificaRelacao(i1,i2)


    def date(datestr="", format="%Y-%m-%d"):
        from datetime import datetime
        if not datestr:
            return datetime.today().date()
        return datetime.strptime(datestr, format).date()



    def ordenaIntervalos(self,arrayIntervalos):
        tempIntevarlosOrdenados = []
        for inter in arrayIntervalos:
            ti = inter.t_i.toordinal()
            tf = inter.t_f.toordinal()
            tempIntevarlosOrdenados.append([ti,tf])

        # a função sorted permite ordenar um array multidimensional por uma coluna deterinada
        self.arrayIntervalosOrdenados = sorted(tempIntevarlosOrdenados, key=lambda x: x[0]) #lambda é uma função anônima inline que retorna x[0]

        for i in range(len(self.arrayIntervalosOrdenados)):
            print(date.fromordinal(self.arrayIntervalosOrdenados[i][0]),date.fromordinal(self.arrayIntervalosOrdenados[i][1]))

    #a partir de aqui é preciso verificar se não se trata do mesmo intervalo (muitos equals) e tb conferir qual a relação da AIA presente


#RAfael Stoffalette JOão
