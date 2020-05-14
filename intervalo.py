# encoding: utf-8
from datetime import date
from random import randint

class Interval:
    def __init__(self):
        self.t_i = ""                               # initial interval's time point
        self.t_f = ""                               # final interval's time point
        self.listaDePontosTemporaisAleatorios = []  # set of random time points (dates)
        self.listaDePontosTemporais = []            # set of deterministic time points (dates)
        self.listaDeIntervalos = []                 # set of intervals



    def incluiPonto(self,ponto): #  method to include a new time point (date) to a specific interval
        if(self.t_i > ponto):
            self.t_i = ponto
        elif(self.t_f < ponto):
            self.t_f = ponto
        self.listaDePontosTemporais.append(ponto)


    def get_inicio(self):       # get the starting point (date) of an interval
        return self.t_i

    def get_Fim(self):          # get the finishing point (date) of an interval
        return self.t_f

    def get_ListadePontosTemporais(self): # get the set of time points (dates) covered by an interval
        return self.listaDePontosTemporais


    def geraUmaDataAleatoria(self,seed=900):  # generating a random time point (date)
        hj = date.today()  # today
        novaData = date.fromordinal(hj.toordinal() + randint(-seed, seed))  # hoje + seed days (default = 900 days)
        return novaData


    def geraDatasAleatorias(self,quantidade):
        for i in range(quantidade):
            novaData = date.fromordinal(self.hj.toordinal() + randint(-900,900))  # hoje + 45 dias</pre>
            self.listaDePontosTemporaisAleatorios.append(novaData)
            self.listaDePontosTemporaisAleatorios.sort()


    def imprimeIntervalos(self):
        print("\n Intervalo: ", self.t_i, self.t_f) #printing intervals

        for i in self.listaDePontosTemporais:
            print(i)


    def constroiIntervalos(self,janelaParaIntervalo):

      for ponto in self.listaDePontosTemporaisAleatorios:
        if (len(self.listaDeIntervalos) == 0):
            inter = Interval()
            inter.t_f = inter.t_i = ponto
            inter.listaDePontosTemporais.append(ponto)
            self.listaDeIntervalos.append(inter)

        else:

            inseriu = False

            for intervalo in self.listaDeIntervalos:  # para cada intervalo de interesse no array de intervalos do atributo

                if (intervalo.t_i <= ponto and ponto <= intervalo.t_f):
                    intervalo.listaDePontosTemporais.append(ponto)

                else:

                    diferenca = abs(intervalo.t_i - ponto)

                    if (
                            diferenca.days < janelaParaIntervalo and intervalo.t_i > ponto):  # temos um novo ponto de inicio
                        intervalo.t_i = ponto
                        intervalo.listaDePontosTemporais.append(ponto)
                        inseriu = True
                        break

                    else:
                        diferenca = abs(intervalo.t_f - ponto)

                        if (
                                diferenca.days < janelaParaIntervalo and intervalo.t_f < ponto):  # temos um novo ponto de termino
                            intervalo.t_f = ponto
                            intervalo.listaDePontosTemporais.append(ponto)
                            inseriu = True
                            break
            if (inseriu):
                inseriu = False

            else:
                inter = Interval()
                inter.t_f = inter.t_i = ponto
                inter.listaDePontosTemporais.append(ponto)
                self.listaDeIntervalos.append(inter)



