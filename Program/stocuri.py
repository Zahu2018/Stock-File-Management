# stoc, stocuri, dictionar, fise magazie
# Face un dictionar din numele fisierelor si stocul actual
# 23.02.2022
# Florian Zah

# Il scrie in fila stocuri.csv pe Desktop
import os
import csv
import tkinter


def fa_lista_din_numele_fisierelor(dir):
    import os
    lista_file = []
    m = (os.listdir(dir))
    for x in m:
        if x[-4:] == ".csv":
            lista_file.append(x)
    #print(lista_file)
    return(lista_file)
    

def preia_stocul(fila):
    myfile = fila
    myvar = open(myfile, 'r', encoding='utf8', errors='ignore')
    lst = myvar.readlines()
    ll = len(lst)
    myva = lst[ll-1] # ultima linie unde e stocul
    a = myva.split('|')
    stoc = a[-2].strip() # -2 = pe a doua coloana de la dreapta este stocul
    myvar.close()
    return(stoc)


def scrie_in_fila(tab):
    global nf
    nf = 'C:\\Users\\User\\Desktop\\stocuri.csv'
    with open(nf, 'w') as f:
        for key in tab.keys():
            #f.write("%s,%s\n" % (key,tab[key]))
            f.write(f"{key},{tab[key]}\n")
            
def main():
    tex = """
    A fost creat fisierul "stocuri.csv"
        pe Desktop.
    """
    l = fa_lista_din_numele_fisierelor('../FISE_MAGAZIE/')
    tabel = {}
    for fisa in l:
        stoc = preia_stocul('../FISE_MAGAZIE/'+fisa)
        nume_fila = fisa.replace('.csv', '')
        tabel[nume_fila] = stoc
    #for i in tabel:  # doar pt. verificare
    #    print(i, tabel[i])
    scrie_in_fila(tabel)

    l1.configure(text=tex)
            
def gui():
    global l1
    app = tkinter.Tk()
    app.title("Stocuri")
    #app.geometry("300x200")
    text = """
            Programul extrage stocurile       
            din fisele de magazie si le       
            scrie in fisierul "stocuri.csv"       
            pe Desktop.       
    """
    l = tkinter.Label(app, text=text)
    l.grid(row=0, column=0, sticky='ew')
    b = tkinter.Button(app, text="Extrage stocuri", command=main)
    b.grid(row=1, column=0, sticky='ew')
    l1 = tkinter.Label(app, text='')
    l1.grid(row=2, column=0, sticky='ew')
    app.mainloop()

            

if __name__ == "__main__":
    gui()
