# crea griglia
import time

griglia = []
posizione_auto = []
posizione_arrivi = []

colonne = int(input('colonne: '))
righe = int(input('righe: '))
colonne += 1
righe += 1
auto = int(input("N di auto: "))
y=0
while y < auto:
    a = int(input(f"Pos auto {y} : "))
    posizione_auto.append(a)
    y +=1
arrivi = auto
y=0
while y < arrivi:
    a = int(input(f"Pos arrivi {y} : "))
    posizione_arrivi.append(a)
    y +=1
def creazionegriglia(colonne,righe):
    global griglia
    x = 0

    while x < righe:
        griglia.append('x')
    #print(griglia)
        x+=1
    x=0
    col = griglia.copy()
#print(col)
    while x < colonne -1:
        for i in col:
            griglia.append(i)
        x+=1

    #print(griglia)
    #print(len(griglia))

def aggiunta_macchine(righe,colonne):
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
    numeri = ["0","1","2","3","4","5","6","7","8","9"]
    global griglia
    global posizione_auto

    #inserimento arrivi
    elemento = 0

    for i in posizione_arrivi:
        griglia.pop(i)
        griglia.insert(i, numeri[elemento])
        elemento += 1
    # inserimento macchine
    elemento = 0
    for i in posizione_auto:
        griglia.pop(i)
        griglia.insert(i, alfabeto[elemento])
        elemento += 1


def movimento_macchine(righe,colonne,auto):

    global griglia
    global posizione_auto
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
    numeri = ["0","1","2","3","4","5","6","7","8","9"]
    posizione_arrivi = []
    posizione_auto.reverse()
    ultimo_elem = len(griglia) -1
    num_slice = ultimo_elem-(colonne-1)
    # while le macchine non saranno arrivate a destinazione
    ultima_riga = griglia[num_slice:]
    num_x = []
    for i in range(righe-2):
        num_x.append("x")
    prima_riga = griglia[:colonne]
    prima_riga.reverse()
    lista_movimento =ultima_riga+num_x+prima_riga
    #print(lista_movimento)
    lista_movimento.reverse()
    for i in lista_movimento:
        if i in numeri:
            posizione_arrivi.append(str(lista_movimento.index(i)))
    print(lista_movimento)
    x = 0
    while x < auto:
        for i in lista_movimento:
            #time.sleep(0.5)
            if i in alfabeto:
                lettera = i
                posizione = lista_movimento.index(i)
                print(f'auto: {lettera}')
                print(f'posizione: {posizione}')
                print(f'griglia: {lista_movimento}')
                print(f'pos arrivi: {posizione_arrivi}')
                if posizione-1 == len(posizione_arrivi)-1:
                    lista_movimento.pop(posizione)
                    posizione_arrivi.pop(posizione-1)
                    lista_movimento.pop(posizione-1)
                    x += 1
                    print(f'eliminazione {lettera}')
                    print(f'mov: {lista_movimento}')
                else:
                    lista_movimento.pop(posizione)
                    lista_movimento.insert(posizione-1,lettera)
                    print(f'avanzamento {lettera}')


    print(lista_movimento)
creazionegriglia(colonne,righe)
aggiunta_macchine(righe,colonne)
print(griglia)
movimento_macchine(righe,colonne,auto)
print(griglia)
