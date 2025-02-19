# Afiseaza ajutor la conta si lb. italiana din meniul "Help"

import tkinter

#def save_send_back():
#   "Functie save in send_back; dezactivata"
#    with open("D:\\SIMLEU SHOES\\PROGRAM\\send_back.txt", 'w', encoding="utf-8") as f:
#        f.write(c.get('1.0', 'end'))


def contabilitate():
    """Definitii de termeni de contabilitate."""
    
    with open('../Program/conta.txt', 'r', encoding="utf-8") as c:
        continut = c.read()
    co = tkinter.Tk()  # co = contabilitate
    co.title('Contabilitate')
    c = tkinter.Text(co, width=100)
    c.grid(row=0, column=0, sticky='nswe')
    c.insert('end', continut)
    s = tkinter.Scrollbar(co, orient='vertical', bg='white')
    s.grid(row=0, column=1, sticky='ns')
    c.configure(yscrollcommand=s.set)
    s.configure(command=c.yview)
    co.mainloop()
    
def dictionar():
    """Definitii de termeni tehnici italiana."""
    
    with open('../Program/dictionar.txt', 'r', encoding="utf-8") as c:
        continut = c.read()
    co = tkinter.Tk()  # co = contabilitate
    co.title('Dictionar italian de termeni tehnici')
    c = tkinter.Text(co, width=40)
    c.grid(row=0, column=0, sticky='nswe')
    c.insert('end', continut)
    s = tkinter.Scrollbar(co, orient='vertical', bg='white')
    s.grid(row=0, column=1, sticky='ns')
    c.configure(yscrollcommand=s.set)
    s.configure(command=c.yview)
    co.mainloop()
    
def sendback():
    """Ce trebuie trims inapoi la finalul articolului."""
    
    global co
    with open('../Program/send_back.txt', 'r', encoding="utf-8") as c:
        continut = c.read()
    co = tkinter.Tk()  # co = contabilitate
    co.title('Send-back')
    c = tkinter.Text(co, width=40)
    c.grid(row=0, column=0, sticky='nswe')
    c.insert('end', continut)
    #save = tkinter.Button(co, text = "Save", border=0, fg='DodgerBlue2', command=save_send_back)
    #save.grid(row=0, column=2 ,sticky='ne')
    s = tkinter.Scrollbar(co, orient='vertical', bg='white')
    s.grid(row=0, column=1, sticky='ns')
    c.configure(yscrollcommand=s.set)
    s.configure(command=c.yview)
    co.mainloop()
    
def contacte():
    """Ce trebuie trims inapoi la finalul articolului."""
    
    with open('../Program/contacte.csv', 'r', encoding="utf-8") as c:
        continut = c.read()
    co = tkinter.Tk()  # co = contabilitate
    co.title('Contacte')
    c = tkinter.Text(co, width=40)
    c.grid(row=0, column=0, sticky='nswe')
    c.insert('end', continut)
    s = tkinter.Scrollbar(co, orient='vertical', bg='white')
    s.grid(row=0, column=1, sticky='ns')
    c.configure(yscrollcommand=s.set)
    s.configure(command=c.yview)
    co.mainloop()
    
def iih():
    """Cum se foloseste intrare iesire deodata."""
    
    continut = """
    Cand se face Intrare/Iesire, 
    se introduce data de intrare urmata 
    de combinatia de litere "#$" urmata 
    de cea de-a doua data (de iesire)
    fara a lasa nici un spatiu liber
    intre data de intrare combinatia de 
    litere si data de iesire.
    
    Exemplu data:
    01.02.2023#$02.02.2023
    
    La fel si la document.
    
    Exemplu document:
    NIR 45#$BC 7
    """
    co = tkinter.Tk()  # co = contabilitate
    co.title('Intrare / Iesire')
    c = tkinter.Text(co, width=40)
    c.grid(row=0, column=0, sticky='nswe')
    c.insert('end', continut)
    #save = tkinter.Button(co, text = "Save", border=0, fg='DodgerBlue2', command=save_send_back)
    #save.grid(row=0, column=2 ,sticky='ne')
    s = tkinter.Scrollbar(co, orient='vertical', bg='white')
    s.grid(row=0, column=1, sticky='ns')
    c.configure(yscrollcommand=s.set)
    s.configure(command=c.yview)
    co.mainloop()
    
    
    
if __name__ == "__main__":
    sendback()  # sau contabilitate() - pt. test