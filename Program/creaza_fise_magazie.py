# Creaza fise magazie

import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#

fise_noua = """
Unitatea: S.C. COMPANY 1 S.R.L., Oradea, Calea Borsului 23 W
          J05/3018/23/11/2021, C.U.I. 45264444
Punct de lucru: Simleu Silvaniei, Simion Barnutiu, Nr. 29  |  Magazia

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
Unitatea: S.C. COMPANY 1 S.R.L., Oradea, Calea Borsului 23 W
          J05/3018/23/11/2021, C.U.I. 45264444
Punct de lucru: Simleu Silvaniei, Simion Barnutiu, Nr. 29  |  Magazia

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
{:>10}|{:<20}|{:>11}|{:>11}|{:>11}|{:>11} 
"""

def creaza(lista_f, trad):
    categorie = ce.get().upper().strip()
    denumire = me.get().upper().strip()
    proprietati = pe.get().upper().strip()
    cod = code.get().upper().strip()
    um = ume.get().upper().strip()
    data = datae.get().lower().strip()
    document = doce.get().upper().strip()
    cantitate = cante.get().strip()
    #print(categorie, denumire, proprietati, cod, um)
    if len(categorie) and len(denumire) and len(proprietati) and len(cod) and len(um) != 0:
        nume_fisier = '{}_{}_{}_{}.csv'.format(categorie, denumire, proprietati, cod)
        CATEGORIE = categorie.upper()
        Denumire = denumire.upper()
        Proprietati = proprietati.upper()
        nul = ''  # placeholder
        continut_fisier_nou = fise_noua_individual.format(cod, CATEGORIE, Denumire, Proprietati, um, data, document, cantitate, nul, cantitate, nul)
        n_f = '../FISE_MAGAZIE/{}'.format(nume_fisier)
        if nume_fisier not in lista_f:
            try: 
                with open(n_f, 'w') as f:
                    f.write(continut_fisier_nou)
                t = trad['rez'] + f':\n{denumire.title()} {proprietati.title()}'
                info = tkinter.Label(nf, text=t, fg='#ff6633')
                info.grid(row=11, columnspan=2)
                ce.delete(0, 'end')
                me.delete(0, 'end')
                pe.delete(0, 'end')
                code.delete(0, 'end')
                ume.delete(0, 'end')
                cante.delete(0, 'end')
                ce.focus_set() #focalizeaza pe cantitate
                
            except FileNotFoundError as e:
                tkinter.messagebox.showinfo(trad['inf'], str(trad['su']))
        else: 
            tkinter.messagebox.showinfo(trad['inf'], trad['ex'])

    else:
        tkinter.messagebox.showinfo(trad['inf'], trad['cc'])

def gui(l_f, trad): 
    global nf, ce, me, pe, code, ume, datae, cante, doce
    nf = tkinter.Tk()  # nf = new file
    nf.title(trad['cfm'])
    cl = tkinter.Label(nf, text=trad['cat'])
    cl.grid(row=0, column=0, sticky='w')
    ce = tkinter.Entry(nf)
    ce.grid(row=0, column=1)
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
    sep2 = ttk.Separator(nf, orient='horizontal')
    sep2.grid(row=7, columnspan=2, sticky="ew")
    datal = tkinter.Label(nf, text=trad['dat'])
    datal.grid(row=8, column=0, sticky='w')
    datae = tkinter.Entry(nf)
    datae.grid(row=8, column=1)
    docl = tkinter.Label(nf, text=trad['doc'])
    docl.grid(row=9, column=0, sticky='w')
    doce = tkinter.Entry(nf)
    doce.grid(row=9, column=1)
    
    bcf = tkinter.Button(nf, text=trad['bcf'], command=lambda l_f=l_f: creaza(l_f, trad), fg='DodgerBlue2')
    bcf.grid(row=10, columnspan=2, sticky='we')
    nf.mainloop()
    
if __name__ == "__main__":
    l = [1,2]  # lista pt test
    gui(l)