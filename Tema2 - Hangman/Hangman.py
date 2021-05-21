import random
lista_generala=['repetare','streptococ','piropopircanita','pepene','tamaduitoare']
def init(lista_principala):
    text=[]
    for i in range(len(lista_principala)):
        text.append('_')
    prima_litera=lista_principala[0]
    ultima_litera=lista_principala[-1]
    for i in range(len(lista_principala)):
        if prima_litera == lista_principala[i]:
            text[i] = prima_litera
        elif ultima_litera == lista_principala[i]:
            text[i] = ultima_litera
    lista_utilizata=[prima_litera,ultima_litera]
    return text,lista_utilizata

def joc(cuvant):
    lista_principala = list(cuvant)
    text,lista_utilizata = init(lista_principala)
    incercari = 7
    while incercari>0:
        print("".join(text))
        print(incercari)
        litera=input("introduceti litera")
        if litera not in lista_utilizata:
            lista_utilizata.append(litera)
        else:
            print("litera deja utilizata!")
            continue
        if litera not in lista_principala:
            incercari-=1
        else:
            for j in range(len(lista_principala)):
                if litera == lista_principala[j] and text[j] == "_":
                    text[j] = litera
                    if '_' not in text:
                        print("jcoul s-a terminat, ai castigat!")
                        return

    print("ai pierdut")
joc(random.choice(lista_generala))



