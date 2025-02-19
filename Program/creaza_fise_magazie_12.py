# Creaza fise magazie

import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#

fise_noua = """
Unitatea: S.C. COMPANY 1 S.R.L., Oradea, Calea Borsului 100
          J05/3000/01/01/2024, C.U.I. 12345678
Punct de lucru: Simleu Silvaniei, Street, Nr. 0  |  Magazia

                             FISA DE MAGAZIE
-------------------------------------------------------------------------------
Cod: [{}]
Categorie: {}
Material: {} {}
U.M.: {}
-------------------------------------------------------------------------------
   Data     Felul si Numarul      Intrari     Iesiri      Stoc       Semnatura
              Documentului                                           de control 
-------------------------------------------------------------------------------
     -    |          -         |     -     |     -     |          0|           
"""

fise_noua_individual = """
Unitatea: S.C. COMPANY 1 S.R.L., Oradea, Calea Borsului 100
          J05/3000/01/01/2024, C.U.I. 12345678
Punct de lucru: Simleu Silvaniei, Street, Nr. 0  |  Magazia

                             FISA DE MAGAZIE
-------------------------------------------------------------------------------
Cod: [{}]
Categorie: {}
Material: {} {}
U.M.: {}
------------------------------------------------------------------------------
   Data     Felul si Numarul      Intrari     Iesiri      Stoc       Semnatura
              Documentului                                           de control 
-------------------------------------------------------------------------------
     -    |          -         |     -     |     -     |          0|           
{:>10}|{:<20}|{:>11}|{:>11}|{:>11}|{:>11} 
"""

fise_noua_individual_cu_scadere = """
Unitatea: S.C. COMPANY 1 S.R.L., Oradea, Calea Borsului 100
          J05/3000/01/01/2024, C.U.I. 12345678
Punct de lucru: Simleu Silvaniei, Street, Nr. 0  |  Magazia

                             FISA DE MAGAZIE
-------------------------------------------------------------------------------
Cod: [{}]
Categorie: {}
Material: {} {}
U.M.: {}
------------------------------------------------------------------------------
   Data     Felul si Numarul      Intrari     Iesiri      Stoc       Semnatura
              Documentului                                           de control 
-------------------------------------------------------------------------------
     -    |          -         |     -     |     -     |          0|           
{:>10}|{:<20}|{:>11}|{:>11}|{:>11}|{:>11}
{:>10}|{:<20}|{:>11}|{:>11}|{:>11}|{:>11}
"""

fisa_noua_necesar = """
Unitatea: S.C. COMPANY 1 S.R.L., Oradea, Calea Borsului 100
          J05/3000/01/01/2024, C.U.I. 12345678
Punct de lucru: Simleu Silvaniei, Street, Nr. 0  |  Magazia

                             SITUATIE NECESAR
-------------------------------------------------------------------------------
Cod: [0]
Categorie: A
Material: B C
U.M.: MP
-------------------------------------------------------------------------------
   Data     Felul si Numarul      Intrari     Necesar      Stoc                
              Documentului                                                     
-------------------------------------------------------------------------------
     -    |          -         |     -     |     -     |          0|           
{:>10}|{:<20}|{:>11}|{:>11}|{:>11}|{:>11}
"""

def creaza_fisa_necesar(fila_noua, cantitate, necesar, data_intrare, doc_intrare):
    _ = fila_noua.rstrip('.csv')
    nume_fisier = _ + '.nec'
    nume_fila_necesar ='../FISE_MAGAZIE/{}'.format(nume_fisier)
    stoc = float(cantitate) - float(necesar)
    nul = ''
    continut = fisa_noua_necesar.format(data_intrare, doc_intrare, cantitate, necesar, stoc, nul)
    
    with open(nume_fila_necesar, 'w') as f:
        f.write(continut)
   

def creaza(lista_f, trad):
    categorie = ce.get().upper().strip()
    denumire = me.get().upper().strip()
    proprietati = pe.get().upper().strip()
    cod = code.get().upper().strip()
    um = ume.get().upper().strip()
    data = datae.get().lower().strip()
    document = doce.get().upper().strip()
    cantitate = cante.get().strip()
    necesar = necee.get().strip()
    ad_sc = adauga_scade.get()
    #print(categorie, denumire, proprietati, cod, um)
    
    if ad_sc == 1:  # Intrare
        if len(categorie) and len(denumire) and len(proprietati) and len(cod) and len(um) != 0:
            nume_fisier = '{}_{}_{}_{}.csv'.format(categorie, denumire, proprietati, cod)
            CATEGORIE = categorie.upper()
            Denumire = denumire.upper()
            Proprietati = proprietati.upper()
            nul = ''  # placeholder
            continut_fisier_nou = fise_noua_individual.format(cod, CATEGORIE, Denumire, Proprietati, um, data, document, cantitate, nul, cantitate, nul, nul, nul)
            n_f = '../FISE_MAGAZIE/{}'.format(nume_fisier)
            if nume_fisier not in lista_f:
                try: 
                    with open(n_f, 'w') as f:  # creaza fisier fisa magazie
                        f.write(continut_fisier_nou)
                    
                    creaza_fisa_necesar(nume_fisier, cantitate, necesar, document, data)
                    
                    t = trad['rez'] + f':\n{denumire.title()} {proprietati.title()}'
                    info = tkinter.Label(nf, text=t, fg='#ff6633')
                    info.grid(row=15, columnspan=2)
                    ce.delete(0, 'end')
                    me.delete(0, 'end')
                    pe.delete(0, 'end')
                    code.delete(0, 'end')
                    ume.delete(0, 'end')
                    cante.delete(0, 'end')
                    necee.delete(0, 'end')
                    ce.focus_set() #focalizeaza pe cantitate
                    
                except FileNotFoundError as e:
                    tkinter.messagebox.showinfo(trad['inf'], str(trad['su']))
            else: 
                tkinter.messagebox.showinfo(trad['inf'], trad['ex'])

        else:
            tkinter.messagebox.showinfo(trad['inf'], trad['cc'])

    elif ad_sc == 2:  # Intrare/Iesire
        if len(categorie) and len(denumire) and len(proprietati) and len(cod) and len(um) != 0:
            nume_fisier = '{}_{}_{}_{}.csv'.format(categorie, denumire, proprietati, cod)
            CATEGORIE = categorie.upper()
            Denumire = denumire.upper()
            Proprietati = proprietati.upper()
            nul = ''  # placeholder
            
            try:
                data_split = data.split('#$')
                doc_split = document.split('#$')
                data_intrare = data_split[0]
                doc_intrare = doc_split[0]
                data_iesire = data_split[1]
                doc_iesire = doc_split[1]
            except IndexError as e:
                tkinter.messagebox.showinfo(trad['inf'], trad['adsc'])  
                
            stoc_zero = 0.00
            
            continut_fisier_nou = fise_noua_individual_cu_scadere.format(cod, CATEGORIE, Denumire, Proprietati, um, data_intrare, doc_intrare, cantitate, nul, cantitate, nul, data_iesire, doc_iesire, nul, cantitate, stoc_zero, nul)
            n_f = '../FISE_MAGAZIE/{}'.format(nume_fisier)
            if nume_fisier not in lista_f:
                try: 
                    with open(n_f, 'w') as f:
                        f.write(continut_fisier_nou)
                        
                    creaza_fisa_necesar(nume_fisier, cantitate, necesar, data_intrare, doc_intrare)
                       
                    t = trad['rez'] + f':\n{denumire.title()} {proprietati.title()}'
                    info = tkinter.Label(nf, text=t, fg='#ff6633')
                    info.grid(row=15, columnspan=2)
                    ce.delete(0, 'end')
                    me.delete(0, 'end')
                    pe.delete(0, 'end')
                    code.delete(0, 'end')
                    ume.delete(0, 'end')
                    cante.delete(0, 'end')
                    necee.delete(0, 'end')          
                    ce.focus_set() #focalizeaza pe cantitate
                    
                except FileNotFoundError as e:
                    tkinter.messagebox.showinfo(trad['inf'], str(trad['su']))
            else: 
                tkinter.messagebox.showinfo(trad['inf'], trad['ex'])

        else:
            tkinter.messagebox.showinfo(trad['inf'], trad['cc'])
        


def gui(l_f, trad): 
    global nf, ce, me, pe, code, ume, datae, cante, doce, necee, adauga_scade
    nf = tkinter.Tk()  # nf = new file
    nf.title()
    cl = tkinter.Label(nf, text=trad['cat'])
    cl.grid(row=0, column=0, sticky='w')
    ce = tkinter.Entry(nf)
    ce.grid(row=0, column=1)
    ce.focus()
    ml = tkinter.Label(nf, text=trad['den'])
    ml.grid(row=1, column=0, sticky='w')
    me = tkinter.Entry(nf)
    me.grid(row=1, column=1)
    pl = tkinter.Label(nf, text=trad['pro'])
    pl.grid(row=2, column=0, sticky='w')
    pe = tkinter.Entry(nf)
    pe.grid(row=2, column=1)
    codl = tkinter.Label(nf, text=trad['cod'])
    codl.grid(row=3, column=0, sticky='w')
    code = tkinter.Entry(nf)
    code.grid(row=3, column=1)
    uml = tkinter.Label(nf, text=trad['um'])
    uml.grid(row=4, column=0, sticky='w')
    ume = tkinter.Entry(nf)
    ume.grid(row=4, column=1)
    sep1 = ttk.Separator(nf, orient='horizontal')
    sep1.grid(row=5, columnspan=2, sticky="ew")
    cantl = tkinter.Label(nf, text=trad['can'])
    cantl.grid(row=6, column=0, sticky='w')
    cante = tkinter.Entry(nf)
    cante.grid(row=6, column=1)
    necel = tkinter.Label(nf, text=trad['nece'])
    necel.grid(row=7, column=0, sticky='w')
    necee = tkinter.Entry(nf)
    necee.grid(row=7, column=1)
    sep2 = ttk.Separator(nf, orient='horizontal')
    sep2.grid(row=8, columnspan=2, sticky="ew")
    datal = tkinter.Label(nf, text=trad['dat'])
    datal.grid(row=9, column=0, sticky='w')
    datae = tkinter.Entry(nf)
    datae.grid(row=9, column=1)
    docl = tkinter.Label(nf, text=trad['doc'])
    docl.grid(row=10, column=0, sticky='w')
    doce = tkinter.Entry(nf)
    doce.grid(row=10, column=1)
    sep3 = ttk.Separator(nf, orient='horizontal')
    sep3.grid(row=11, columnspan=2, sticky="ew")
    
    adauga_scade = tkinter.IntVar()    
    intrare_radiobutton = tkinter.Radiobutton(nf, text=trad['intr'], variable = adauga_scade, value = 1)
    intrare_iesire_radiobutton = tkinter.Radiobutton(nf, text=trad['ii'], variable = adauga_scade, value = 2)
    intrare_radiobutton.grid(row=12, column=0, sticky='w')
    intrare_iesire_radiobutton.grid(row=12, column=1, sticky='w')
    
    sep4 = ttk.Separator(nf, orient='horizontal')
    sep4.grid(row=13, columnspan=2, sticky="ew")
    bcf = tkinter.Button(nf, text=trad['bcf'], command=lambda l_f=l_f: creaza(l_f, trad), fg='DodgerBlue2')
    bcf.grid(row=14, columnspan=2, sticky='we')
    nf.mainloop()
    
if __name__ == "__main__":
    l = [1,2]  # lista pt test
    gui(l)