# stoc, stocuri, dictionar, fise magazie
# Face un dictionar din numele fisierelor si stocul actual
# 23.02.2022
# Florian Zah
# Data here is fictional and does not reflect the company operations.

# Il scrie in fila stocuri.csv pe Desktop
import os
import csv
import tkinter

header_nir = """Unitatea: SC SIMLEU SHOES SRL, Oradea, Calea Borsului 23 W, J05/33401/23/11/2021
CUI 12345678, Pct. lucru: Simleu Silvaniei, Simion Barnutiu, Nr 29 | Magazia

                NOTA DE INTRARE RECEPTIE SI CONSTATARE DIFERENTE
                
         Nr.: ______  Data: _____________ Factura/Aviz: ____________
         
Subsemnatii, membrii comisiei de receptie, am procedat la receptionarea valorilor
materiale furnizate de: ___________________________________, din: _______________,
cu auto/vagon: _______________, documente insotitoare: __________________________, 
delegat: ______________________, constatandu-se urmatoarele:
    
-------------------------------------------------------------------------------
|Nr. | Denumirea bunurilor receptionate        | UM | Cantitate  | Cantitate  |
|crt.|                                         |    |  conform   |            |
-------------------------------------------------------------------------------
"""

footer_nir = """
-------------------------------------------------------------------------------

Comisia de receptie                              Primit in gestiune
Nume, prenume si semnatura                       Data si semnatura
__________________________                       ___________________________          
"""

header_bc = """Unitatea: SC SIMLEU SHOES SRL, Oradea, Calea Borsului 23 W, J05/3436018/23/11/2021
CUI 12345678, Pct. lucru: Simleu Silvaniei, Simion Barnutiu, Nr 29 | Magazia

                             BON DE CONSUM (colectiv)

Produs/lucrare/lansare: _________________________________, Nr. comenzii: _____

-------------------------------------------------------------------------------
|Nr. | Denumirea materialelor inclusiv sort    | UM | Cantitate  | Cantitate  |
|crt.| marca dimensiune profil                 |    | necesara   | eliberata  |
-------------------------------------------------------------------------------                       
"""

footer_bc = """
-------------------------------------------------------------------------------

Data si semnatura   Sef compartiment      Gestionar            Primitor
_________________   _________________   _________________   _________________ 

"""
nr_crt = 0

def fa_lista_din_numele_fisierelor(dir):
    import os
    lista_file = []
    m = (os.listdir(dir))
    for x in m:
        if x[-4:] == ".csv":
            lista_file.append(x)
    #print(lista_file)
    return(lista_file)
    

def preia_stocul(fila, data):
    myfile = fila
    with open(myfile, 'r', encoding='utf8', errors='ignore') as f:
        lst = f.readlines()
        new_lst = []
        for i in lst:
            linie_split = i.split("|")
            new_lst.append(linie_split)
        for j in new_lst:
            if data in j[0]:
                cantitate_intrata = j[2]  # j[3] pentru iesiri
                return cantitate_intrata
            else:
                pass


def scrie_in_fila(tab):
    global nir, bc, nr_crt
    nr_crt += 1
    um = "mp"
    nul = ""
    nir = 'C:\\Users\\zahfl\\OneDrive\\Desktop\\nir.txt'
    with open(nir, 'w') as f:
        f.write(header_nir)
        for key in tab.keys():
            f.write(f"|{nr_crt:>4}|{key:<41}|{nul:>4}|{tab[key]:>12}|{tab[key]:>12}|")
        f.write(footer_nir)
        
    bc = 'C:\\Users\\zahfl\\OneDrive\\Desktop\\bc.txt'
    with open(bc, 'w') as f:
        f.write(header_bc)
        for key in tab.keys():
            f.write(f"|{nr_crt:>4}|{key:<41}|{nul:>4}|{nul:>12}|{tab[key]:>12}|")
        f.write(footer_bc)
        
    
            
def main():
    tex = """
    A fost creat fisierul "nir si bonuri consum"
        pe Desktop.
    """
    data = e_data.get()  # preia entry cu data
    l = fa_lista_din_numele_fisierelor('../FISE_MAGAZIE/')
    tabel = {}
    for fisa in l:
        stoc = preia_stocul('../FISE_MAGAZIE/'+fisa, data)
        if stoc is not None:
            nume_fila = fisa.replace('.csv', '').split("_")
            material = nume_fila[1] + ' ' + nume_fila[2]
            tabel[material] = stoc
    #for i in tabel:  # doar pt. verificare
    #    print(i, tabel[i])
    
    scrie_in_fila(tabel)
    l1.configure(text=tex)
            
def gui():
    global l1, e_data
    app = tkinter.Tk()
    app.title("NIR")
    app.geometry("300x200")
    text = """Face NIR si Bon de Consum       
pe o anumita data"""
    l = tkinter.Label(app, text=text)
    l.grid(row=0, columnspan=2, sticky='ew')
    l_data = tkinter.Label(app, text = "Data:")
    l_data.grid(row=1, column=0, sticky='w')
    e_data = tkinter.Entry(app)
    e_data.grid(row=1, column=1, sticky='w')
    b = tkinter.Button(app, text="Creaza NIR si BC", command=main)
    b.grid(row=2, columnspan=2, sticky='ew')
    l1 = tkinter.Label(app, text='')
    l1.grid(row=3, columnspan=2, sticky='ew')
    app.mainloop()

            

if __name__ == "__main__":
    gui()
