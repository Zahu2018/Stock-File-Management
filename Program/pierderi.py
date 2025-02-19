# Calculare pierderi de material si recalculeaza consumul
# calcul pierderi

"""      SCHEMA LOGICA

Legenda:
    (inceput/sfarsit)
    [proces, atribuire]
    <decizie>
    /input - intrare/
    \print - iesire\

"""


_author =  "Zah"

import tkinter

def af():  # Afiseaza formule
    t = """
    pp = (nrper_nef * 100) / nrper
    cc = ((ci*pp) / 100) + ci
    ----------------------------------
    nrper = numar perechi
    nrper_nef = numar perechi nefacute
    pp = pierdere procente
    ci = consum initial
    cc = consum corectat
    """
    afl.config(text=t)
    bf.config(text="Nu afisa formule")
    bf.config(command=naf)
    
    
def naf():  # Nu afisa formule (ascunde/restrange formule)
    afl.config(text="")
    bf.config(text="Afiseaza formule")
    bf.config(command=af)
    
def calculeaza():  # calculeaza piererile
    try:
        nrper = int(npe.get())  # numar perechi
        nrper_nef = int(npne.get())  # numar perechi nefacute
        pp = round((nrper_nef*100)/nrper, 2)  # pierderi in procente
        ppl.config(text=str(pp)+"%")
    except:
        afl.configure(text="Completati cel putin primele doua rubrici")
    try:
        ci = float(cie.get())  # consum initial
        cc = ((ci*pp/100)+ci)  # consum corectat
        ccl.config(text=str(cc))
    except:
        pass
    
    
    
def gui():
    global npe, npne, cie, ppl, ccl, afl, bf
    app = tkinter.Tk()
    app.title("Calcul pierderi")
    # Coloana din stanga (labels)
    npl = tkinter.Label(app, text="Numar perechi")
    npl.grid(row=0, column=0, sticky='w')
    npnl = tkinter.Label(app, text="Numar perechi nefacute")
    npnl.grid(row=1, column=0, sticky='w')
    ppl = tkinter.Label(app, text="Pierdere procentuala")
    ppl.grid(row=2, column=0, sticky='w')
    cil = tkinter.Label(app, text="Consum initial")
    cil.grid(row=3, column=0, sticky='w')
    ccl = tkinter.Label(app, text="Consum corectat")
    ccl.grid(row=4, column=0, sticky='w')
    
    # Coloana din dreapta (entry)
    npe = tkinter.Entry(app)
    npe.grid(row=0, column=1)
    npne = tkinter.Entry(app)
    npne.grid(row=1, column=1)
    ppl = tkinter.Label(app)
    ppl.grid(row=2, column=1)
    cie = tkinter.Entry(app)
    cie.grid(row=3, column=1)
    ccl = tkinter.Label(app)
    ccl.grid(row=4, column=1)
    
    # Buton "Calculeaza"
    bc = tkinter.Button(app, text="Calculeaza", command=calculeaza)
    bc.grid(row=5, columnspan=2, sticky='we')

    
    # Buton "Afiseaza formule"
    bf = tkinter.Button(app, text="Afiseaza formule", command=af, relief="flat")
    bf.grid(row=6, columnspan=2, sticky='we')
    
    # Afisare formule
    afl = tkinter.Label(app, text="")
    afl.grid(row=7, columnspan=2, sticky='we')
    
    app.mainloop()
    
if __name__ == "__main__":
    gui()