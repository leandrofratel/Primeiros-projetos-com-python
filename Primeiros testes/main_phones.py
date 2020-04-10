import time

telefone = []

with open('telefones.txt') as tel:
    for t in tel:
        telefone.append(t)
        
nova_lista = []


def entrada(telefone, nova_lista):
    
    #Recebe uma lista de telefones
    #Transfere cada número para uma nova lista e limpa os números

    while telefone:
        lista = telefone.pop()

        #Remove caracteres estranhos de cada telefone
        #time.sleep(0.1)
        print("Tratando os numeros: " + lista.rstrip(), flush=True)
        tratado = lista.replace('-','').replace('.','').replace(")",'').replace('(','').replace('ï¿½','').replace(' ','').replace('/','').replace('�','')
        nova_lista.append(tratado)

def lista_limpa(nova_lista):
        #Mostra todos os números de telefone sem os erros de caracter
    print('\nSegue lista de números:')
    for n in nova_lista:
        #time.sleep(0.1)
        print(n.rstrip(), flush=True)


entrada(telefone, nova_lista)
lista_limpa(nova_lista)