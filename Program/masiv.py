#masiv, #adauga, #scade, #fise magazie
# Adauga in fisele de magazie masiv
# inclusiv cu creare de noi fise de magazie

import tkinter
import os
from creaza_fise_magazie import fise_noua as fn

nul = ''

def listeaza_fm():  # preia toate fisele de magazie
    global lista_fm
    os.chdir('../FISE_MAGAZIE')
    lista_fm = os.listdir()
    return lista_fm
    
def citeste_csv(csv):  # citeste csv intr-o lista
    with open(csv, 'r') as csv:
        materiale = csv.readlines()
    return materiale

def ordoneaza_nume(mat): 
    global fise_noua
    split_mat = mat.split(',')
    categorie = split_mat[0]
    cod = split_mat[1]
    nume = split_mat[2]
    parametrii = split_mat[3]
    cantitate = split_mat[4]
    um = split_mat[5]
    nume_corect = (f'{categorie}_{nume}_{parametrii}_{cod}.csv').replace('/', ' ')
    fise_noua = fn.format( cod, categorie, nume, parametrii, um)
    return nume_corect, cantitate
    
def scrie_in_fm(nume_corect_fm_cantitate):  # daca fila exista: ADAUGA
    nume = nume_corect_fm_cantitate[0]
    cantitate = float(nume_corect_fm_cantitate[1])
    with open(nume, 'r+') as fila:
        linii = fila.readlines()
        last_line = linii[-1]
        lista_last_line = last_line.split('|')
        _stoc = lista_last_line[4].strip()
        stoc = float(_stoc) + float(cantitate)
        linia = '{:>10}|{:<20}|{:>11.2f}|{:>11}|{:>11.2f}|{:>11}\n'.format(data, doc, cantitate, nul,stoc, nul)
        print(f'OK - {nume:40} | Cantitate = {_stoc:>11} | TOTAL = {stoc:>11}')
        fila.write(linia)
        
def scrie_in_fm_scade(nume_corect_fm_cantitate):  # daca fila exista: SCADE
    nume = nume_corect_fm_cantitate[0]
    cantitate = float(nume_corect_fm_cantitate[1])
    with open(nume, 'r+') as fila:
        linii = fila.readlines()
        last_line = linii[-1]
        lista_last_line = last_line.split('|')
        _stoc = lista_last_line[4].strip()
        if float(_stoc) == 0:
            stoc = 0
            print(f"S0 - {nume:40} | Cantitate = {_stoc:>11} | TOTAL = {stoc:>11}")
        else:
            stoc = float(_stoc) - float(cantitate)
            linia = '{:>10}|{:<20}|{:>11}|{:>11.2f}|{:>11.2f}|{:>11}\n'.format(data, doc, nul, cantitate,stoc, nul)
            print(f'OK - {nume:40} | Cantitate = {_stoc:>11} | TOTAL = {stoc:>11}')
            fila.write(linia)
        
def scrie_in_noua_fm(nume_corect_fm_cantitate):  # daca fila NU exista
    nume = nume_corect_fm_cantitate[0]
    cantitate = float(nume_corect_fm_cantitate[1])
    #print(nume)
    with open(nume, 'w') as fila:
        stoc = float(cantitate)
        linia = '{:>10}|{:<20}|{:>11.2f}|{:>11}|{:>11.2f}|{:>11}\n'.format(data, doc, cantitate, nul, cantitate, nul)
        text = fise_noua +  linia
        print(f'OK - {nume:40} | Cantitate = {stoc:>11} | TOTAL = {stoc:>11}')
        fila.write(text)
        
def adauga():
    global data, doc
    data = input("Introduceti data: ")
    doc = input("Introduceti documentul: ")
    csv = citeste_csv('../de_scris.csv')
    lista_fm = listeaza_fm()
    for i in csv:
        nc = ordoneaza_nume(i) #nc = nume corect, retuneaza nc, cantitate
        #print(nc)
        if nc[0] in lista_fm:
            scrie_in_fm(nc)
            #break
        else:
            scrie_in_noua_fm(nc)
            #break
            
def scade():
    global data, doc
    data = input("Introduceti data: ")
    doc = input("Introduceti documentul: ")
    csv = citeste_csv('../de_scris.csv')
    lista_fm = listeaza_fm()
    for i in csv:
        nc = ordoneaza_nume(i) #nc = nume corect, retuneaza nc, cantitate
        #print(nc)
        if nc[0] in lista_fm:
            scrie_in_fm_scade(nc)
        else:
            print(f'\nNE - {nc[0]:40} | NU exista; nu am din ce scade.\n')

def main():
    print("categorie | cod | material | proprietate | cantitate | um")
    print("Legenda: OK; S0 = Stoc 0; NE = Fisa nu exista\n")
    a_s = input("Introdu adauga sau scade: ")
    if a_s == 'adauga':
        adauga()
    elif a_s == 'scade':
        scade()
    else:
        print('Introduceti doar adauga sau scade')
    
if __name__ == "__main__":
    main()
    
        