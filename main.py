from datetime import *
from aia import *

start = time.time() #start stores the procedure starting time point

aia = Aia(45)                   # aia is an  AIA object
aia.listaRelacoesPossiveis()    # printing of all possible relations by AIA


arrayIntervalos = [] # arrayIntervalos stores the set of intervals used to determine AIA relations


for i in range(10):
    i1 = Interval()
    dtRand = aia.geraUmaDataAleatoria()
    dtRand2 = aia.geraUmaDataAleatoria(dtRand,79)

    if(dtRand < dtRand2):
        i1.t_i = dtRand
        i1.t_f = dtRand2

    else:
        i1.t_i = dtRand2
        i1.t_f = dtRand

    arrayIntervalos.append(i1)


aia.ordenaIntervalos(arrayIntervalos)
aia.executaAIA()






oldIntervalo = arrayIntervalos[0]
for int in arrayIntervalos:
    aia.identificaRelacao(oldIntervalo,int)
    oldIntervalo = int


print("Tempo total de execução: %.3f segundos " %(time.time() - start))
#for i in range(190):
#    arrayDatas.append(aia.geraUmaDataAleatoria())


#aia.constroiTimeStamp(arrayDatas)
#aia.executaAIA()

