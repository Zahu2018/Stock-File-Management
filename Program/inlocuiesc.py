# Inlocuieste in fisele de magazie anumite lucruri
import tkinter

def citeste_fila(fila):  # for read and write
    with open(fila, 'r', encoding="utf-8") as f:
        continut = f.read()
        return continut
       
def scrie_fila(fila, rezu):  # rezu=rezultat
    with open(fila, 'w', encoding="utf-8") as f:
        f.write(rezu)

def inloc():
    ce_ = ce.get().strip()
    cu_ce = me.get().strip()
    dir = os.chdir('../FISE_MAGAZIE')
    for fila in os.listdir(dir):
        text = citeste_fila(fila)
        rezu = text.replace(ce, cu_ce)
        scrie_fila(fila, rezu)
    
def gui():
           
    inloc = tkinter.Tk()  # nf = new file
    inloc.title('Inlocuieste')
    cl = tkinter.Label(inloc, text='Inlocuieste ce:')
    cl.grid(row=0, column=0, sticky='w')
    ce = tkinter.Entry(inloc)
    ce.grid(row=0, column=1)
    ml = tkinter.Label(inloc, text='Inlocuieste cu ce:')
    ml.grid(row=1, column=0, sticky='w')
    me = tkinter.Entry(inloc)
    me.grid(row=1, column=1)
    bcf = tkinter.Button(inloc, text='Inlocuieste', command=inloc, fg='DodgerBlue2')
    bcf.grid(row=5, columnspan=2, sticky='we')
    inloc.mainloop()
        
#if __name__ == "__main__":
#    gui()
gui()