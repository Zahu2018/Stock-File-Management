# Transformare din metrii patrati in picioare patrate :) ...
# Transform from square meters to square feet ...

#         37.0 = 37
#         37.1 = 37.25
#         37.2 = 37.50
#         37.3 = 37.75

#       ft = 0,3048 metri di lunghezza => ft2 = 0.09290304 m2

#       * 98_ = 0.98 * 10.764 => 10.548 ft2

#       m2 = ft2 * 0.0929  (square foot - en)
#       m2 = ft2 / 10.764  (square foot - en)
#       m2 = pq2 / 10.764  (piede quadrado - it)


_author =  "Zah"


import tkinter

#FACTOR = 10.764     # pt impartirea picioare cu factor => mp
FACTOR = 0.09290304  # pt inmultirea picioare cu factor => mp

OPTIONS_LIST = ["Square feet -> Square meters: ft2 -> m2", 
                "Square meters -> Square feet: m2 -> ft2"]  # lista optiuni
                
def ft2_m2(cantitate):
    rez_lab.config(text=str(cantitate*FACTOR)+" m2")
    
def m2_ft2(cantitate):
    rez_lab.config(text=str(cantitate/FACTOR)+" ft2")
    

def calculeaza():
    try:
        optiune = value_inside.get()
        if optiune == "Select an Option":
            rez_lab.configure(text="Selectati o optiune")
    except:
        rez_lab.configure(text="Nu pot prelua optiune")
        
    try:    
        cantitate = float(valoare.get())  # ia valoarea din entry  
        if optiune == "Square feet -> Square meters: ft2 -> m2":
            ft2_m2(cantitate)
        if optiune == "Square meters -> Square feet: m2 -> ft2":
            m2_ft2(cantitate)
    except:
        rez_lab.configure(text="Introduceti o valoare")
        
        

def gui():
    global rez_lab, valoare, value_inside
    app = tkinter.Tk()
    app.title("Transformari")
    value_inside = tkinter.StringVar(app)
    value_inside.set("Select an Option")
    question_menu = tkinter.OptionMenu(app, value_inside, *OPTIONS_LIST)
    question_menu.grid(row=0, column=0, sticky='ew')

    valoare = tkinter.Entry(app)
    valoare.grid(row=1, column=0, sticky='ew')
    
    bc = tkinter.Button(app, text="Calculeaza", command=calculeaza)
    bc.grid(row=2, column=0, sticky='we')
    
    rez_lab = tkinter.Label(app, text = "\nRezultat")
    rez_lab.grid(row=3, column=0, sticky='ew')
    
    app.mainloop()
    
if __name__ == "__main__":
    gui()