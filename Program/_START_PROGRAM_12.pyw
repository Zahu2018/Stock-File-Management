# SIMLEU SHOES - program fise magazie, etc.
#fise_magazie, #raport_adezivi, #stocuri
""" Program fabrica

python -u -m pylint "$(FULL_CURRENT_PATH)"   pt. linter F6 (Sublime Text Editor)

Model nume fisier: categorie_nume_proprietati_cod.csv
"""


import collections
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import subprocess
from datetime import datetime
import time
from PIL import Image, ImageTk

# Modulele mele
import pierderi
import creaza_fise_magazie
import helpz
import stocuri
import transformari
import firme
import poze
import opereaza_necesar
import ni_bon_consum as nir_bc

_VERSION = 12  # fise necesar
_STATUS = 'OK'
_AUTOR = "Zah"

class FiseDeMagazie():
    '''Working with classes.'''
    def __init__(self, app):  # app = tkinter.Tk()
        self.app = app
        app.title('SIMLEU SHOES')
        #app.geometry('1300x550')

        self.d = {}

        app.iconbitmap('storage_icon.ico')

        ###          Job before GUI
        ### ---------------------------------
        #citeste fise de magazie
        #os.chdir('../FISE_MAGAZIE')
        #lista = os.listdir()  # lista cu fise de magazie
        #self.lista = []
        #for _ in sorted(lista):
        #    __ = _.rstrip('.csv').split('_')
        #    self.lista.append(__)
        #cat = set()
        #for i in sorted(lista):
        #    n = i.split('_')
        #    cat.add(n[0])
        #cat.add('Toate')
        #self.list_cat = list(cat)
        self.list = self.refresh()


        ##############    MENU    ############
        bara_meniu = tkinter.Menu(self.app, fg='red')  # bara meniu

        desfasurator_fise = tkinter.Menu(bara_meniu, tearoff = 0)
        desfasurator_calcule = tkinter.Menu(bara_meniu, tearoff = 0)
        desfasurator_ajutor = tkinter.Menu(bara_meniu, tearoff = 0)

        bara_meniu.add_cascade(label = "Fise magazie", menu=desfasurator_fise)
        bara_meniu.add_cascade(label = "Calcule", menu=desfasurator_calcule)
        bara_meniu.add_cascade(label = "Ajutor", menu=desfasurator_ajutor)



        ### Fise magazie +
        ###              |- Creaza fise magazie
        ###              |- Creaza raport adezivi
        ###              |- Creaza raport stocuri
        desfasurator_fise.add_command(label="Creaza fise magazie",
                                    command=self.creaza_fise_magazie)
        #desfasurator_fise.add_command(label="Inlocuieste in fise mag",
        #                           command=self.inlocuieste)
        desfasurator_fise.add_command(label="Creaza raport adezivi")
        desfasurator_fise.add_command(label="Creaza raport stocuri",
                                    command=self.creaza_raport_stocuri)
        desfasurator_fise.add_command(label="Creaza NIR si BC",
                                    command=self.creaza_nir_bc)


        ### Calcule +
        ###             |- Calcule pierderi
        ###             |- Transformari
        desfasurator_calcule.add_command(label="Calcul pierderi",
                                    command=self.calcul_pierderi)
        desfasurator_calcule.add_command(label="Transformari",
                                    command=self.transform)



        ### Ajutor +
        ###        |- Contabilitate
        ###        |- Dictionar
        ###        |- Ordin 2634 din 2015
        ###        |- Trimis inapoi
        desfasurator_ajutor.add_command(label="Contabilitate",
                                    command=self.contabilitate)
        desfasurator_ajutor.add_command(label="Dictionar",
                                    command=self.dictionar)
        desfasurator_ajutor.add_command(label="Ordin 2634 din 2015",
                                    command=self.ordin)
        desfasurator_ajutor.add_command(label="Trimis inapoi",
                                    command=self.sendback)
        desfasurator_ajutor.add_command(label="Contacte",
                                    command=self.contacte)
        desfasurator_ajutor.add_command(label="Intrare/Iesire",
                                    command=self.intrare_iesire_help)
        self.app.config(menu=bara_meniu)


        ##################  FRAME   ##################
        ### +--------+---------------------+---------+
        ### |        |                     |         |
        ### | frame  |        frame        | frame   |
        ### | stanga |        mijloc       | dreapta |
        ### |        |                     |         |
        ### +--------+---------------------+---------+

        self.frame_stanga = tkinter.LabelFrame(self.app, text='Stanga',
                                            fg='DodgerBlue2')
        self.frame_stanga.grid(row=0, column=0, stick='nsew')
        self.frame_mijloc = tkinter.LabelFrame(self.app, text='Mijloc',
                                            fg='DodgerBlue2')
        self.frame_mijloc.grid(row=0, column=1, stick='nsew')
        self.frame_dreapta = tkinter.LabelFrame(self.app, text='Dreapta',
                                            fg='DodgerBlue2')
        self.frame_dreapta.grid(row=0, column=2, stick='nsew')

        ###--------------------------------
        ###      FRAME STANGA
        ###--------------------------------

        ###    Combobox Categorii Materiale
        sc = tkinter.StringVar()
        self.categorii = ttk.Combobox(self.frame_stanga, width=29, textvariable=sc)
        self.categorii['values'] = self.list_cat
        self.categorii['state'] = 'readonly'
        self.categorii.current(0)
        self.categorii.grid(row=0, column=0, sticky='w')
        self.categorii.bind('<<ComboboxSelected>>', self.populeaza_cu_categorii)

        ###    Combobox Categorii Firme
        fi = tkinter.StringVar()
        self.firme = ttk.Combobox(self.frame_stanga, width=29, textvariable=fi)
        self.firme['values'] = firme.firme  #[key for key in firme.firme] = originalul
        self.firme['state'] = 'readonly'
        self.firme.current(0)
        self.firme.grid(row=1, column=0, sticky='w')
        self.firme.bind('<<ComboboxSelected>>', self.populeaza_cu_firme)

        refresh = tkinter.Button(self.frame_stanga, text='Refresh',
                                command=self.refresh, fg='DodgerBlue2')
        refresh.grid(row=0, column=1)

        ###    Entry Search + List Box
        #self.lista = lista  # ar fi lista cu nume
        self.entry = tkinter.Entry(self.frame_stanga, width=38)
        self.entry.grid(row=2, column=0, sticky='w')
        self.entry.bind('<KeyRelease>', self.Scankey)

        self.buton = tkinter.Button(self.frame_stanga, text='   x   ',
                            relief="solid", fg='red', command=self.but)
        self.buton.grid(row=2, column=1)


        self.listbox = tkinter.Listbox(self.frame_stanga, width=38)
        self.listbox.grid(row=3, columnspan=2, sticky='nsew')

        self.da = []
        for item in self.lista:
            txt = (item[0] + '_' + item[1] + '_' + item[2] + '_' + item[3]).upper()
            # => txt = ADEZIV_MASTICE MASPREN_C 3935L_3935
            self.da.append(txt)

        self.Update(self.da)
        self.listbox.bind("<<ListboxSelect>>", self.callback)



        ###--------------------------------
        ###      FRAME MIJLOC
        ###--------------------------------

        ###     Randul I si II
        ###     Data
        data_label = tkinter.Label(self.frame_mijloc, text='Data')
        data_label.grid(row=0, column=0)
        self.data_entry = tkinter.Entry(self.frame_mijloc)
        self.data_entry.grid(row=1, column=0, padx=3)
        ###     Document
        document_label = tkinter.Label(self.frame_mijloc, text='Document')
        document_label.grid(row=0, column=1)
        self.document_entry = tkinter.Entry(self.frame_mijloc)
        self.document_entry.grid(row=1, column=1, padx=3)
        ###     Intrare/Iesire
        self.adauga_scade = tkinter.IntVar()
        #self.adauga_scade.set(1)

        self.intrare_radiobutton = tkinter.Radiobutton(self.frame_mijloc,
                text='Intrare', variable = self.adauga_scade, value = 1)
        self.iesire_radiobutton = tkinter.Radiobutton(self.frame_mijloc,
                text='Iesire', variable = self.adauga_scade, value = 2)

        self.intrare_radiobutton.grid(row=0, column=2, sticky='w', padx=3)
        self.iesire_radiobutton.grid(row=1, column=2, sticky='w', padx=3)
        # preia o optiune sau alta = self.adauga_scade.get()
        #  if valoare == "1" ... if valoare == "2" ...

        ###      Cantitate
        cantitate_label = tkinter.Label(self.frame_mijloc, text='Cantitate')
        cantitate_label.grid(row=0, column=3)
        self.cantitate_entry = tkinter.Entry(self.frame_mijloc)
        self.cantitate_entry.grid(row=1, column=3, padx=3)
        ###      Salveaza - OK
        salveaza_label = tkinter.Label(self.frame_mijloc, text='Salveaza')
        salveaza_label.grid(row=0, column=4)
        salveaza_buton = tkinter.Button(self.frame_mijloc, text='OK',
                relief='solid', command=self.salveaza)
        salveaza_buton.grid(row=1, column=4, ipadx=10, padx=3)
        ###      Deschide fisa
        deschide_fila_but_text = tkinter.Button(self.frame_mijloc,
                text='Deschide fisa', command=self.deschide_fila_cu_notepad,
                borderwidth=0 , fg='DodgerBlue2')
        deschide_fila_but_text.grid(row=0, column=5, padx = 3, sticky='w')
        ###      Deschide dosarul
        deschide_fila_buton = tkinter.Button(self.frame_mijloc,
                text='Deschide folder', command=self.deschide_director_cu_fm,
                fg='DodgerBlue2', borderwidth=0)
        deschide_fila_buton.grid(row=1, column=5, padx=3, sticky='w')

        ###      Randul III
        ###      Vezi poza
        self.open_imagine = tkinter.Button(self.frame_mijloc,
                text="Vezi poza", command=self.open_img, border=0, fg='DodgerBlue2')
        self.open_imagine.grid(row=2, column=0, sticky='w')
        ###      Deschide necesar
        self.deschide_necesar_but_text = tkinter.Button(self.frame_mijloc,
                text='Deschide necesar', command=self.deschide_necesar_cu_notepad,
                borderwidth=0 , fg='DodgerBlue2')
        self.deschide_necesar_but_text.grid(row=2, column=1, sticky='w')

        ###      RadioButton Intrare/Iesire
        self.iesire_radiobutton = tkinter.Radiobutton(self.frame_mijloc,
                text='Intrare/Iesire', variable = self.adauga_scade, value = 3)
        self.iesire_radiobutton.grid(row=2, column=2, sticky='w')
        self.necesar = tkinter.Entry(self.frame_mijloc)
        self.necesar.grid(row=2, column=3)
        self.necesar.insert(0, "Necesar")
        self.necesar.config({"background": "DodgerBlue2"})
        self.necesar.config({"foreground": "White"})
        ###      Deschide fisa
        deschide_fila_but_com = tkinter.Button(self.frame_mijloc, text='Comenzi',
                command=self.deschide_director_comenzi, borderwidth=0 , fg='DodgerBlue2')
        deschide_fila_but_com.grid(row=2, column=5, padx = 3, sticky='w')

        ###      Randul IV
        ###      Titlu fise de magazie
        self.titlu_fise_magazie_label = tkinter.Label(self.frame_mijloc,
                text='', font=("Times New Roman", 12, "bold"))
        self.titlu_fise_magazie_label.grid(row=3, column=0, columnspan=4)




        ###      Continut fise de magazie
        frame_text = tkinter.Frame(self.frame_mijloc)
        frame_text.grid(row=4, columnspan=6)
        self.continut_fise = tkinter.Text(frame_text, height=25, width=85)
        self.continut_fise.grid(row=0, column=0, sticky='w')
        self.continut_fise.insert('end', '')
        vsb_text = tkinter.Scrollbar(frame_text)
        vsb_text.grid(row=0, column=1, sticky='ns')
        self.continut_fise.config(yscrollcommand=vsb_text.set)
        vsb_text.config(command=self.continut_fise.yview)
        self.continut_fise.yview_moveto(1.0)
        self.ultima_linie = tkinter.Label(frame_text, text='\n\n',
                font=('Courier', '10'))
        self.ultima_linie.grid(row=1, column=0, sticky='nw')

        ###       Materiale lipsa
        with open('../Program/lipsuri.txt', 'r+', encoding="utf-8") as c:
            continut = c.read()


        ###--------------------------------
        ###      FRAME DREAPTA
        ###--------------------------------
        ### aici apar poze cu materiale, TO DO, etc.

        ###      Ziua, data, ora, saptamana
        self.ziua_data = tkinter.Label(self.frame_dreapta, text='',
                fg='#c10000', font=('Courier', '10', 'bold'))
        self.ziua_data.grid(row=0, column=0, sticky='nw')
        self.ora = tkinter.Label(self.frame_dreapta, text='',
                fg='#c10000', font=('Courier', '10', 'bold'))
        self.ora.grid(row=0, column=1, sticky='nw')
        self.ora.after(1000, self.update_label_ora)
        #self.saptamana = tkinter.Label(self.frame_dreapta,
        #       text='', fg='#c10000', font=('Courier', '10', 'bold'))
        #self.saptamana.grid(row=0, column=2, sticky='nw')
        self.afiseaza_data_timpul()

        ###       Lista Lipsuri
        with open('../Program/todo.txt', 'r+', encoding="utf-8") as c:
            continut = c.read()
        self.todo = tkinter.Text(self.frame_dreapta, width=26)
        self.todo.grid(row=1, column=0, sticky='nswe')
        self.todo.insert('end', continut)
        s = tkinter.Scrollbar(self.frame_dreapta, orient='vertical', bg='white')
        s.grid(row=1, column=1, sticky='ns')
        self.todo.configure(yscrollcommand=s.set)
        s.configure(command=self.todo.yview)
        ###       Buton Save / Deschide fila
        deschide_fila_but_text = tkinter.Button(self.frame_dreapta,
                text='Deschide fisa', command=self.deschide_todo, borderwidth=0 , fg='DodgerBlue2')
        deschide_fila_but_text.grid(row=2, column=0, padx = 3, sticky='w')
        save_fila_but_text = tkinter.Button(self.frame_dreapta,
                text='Save', command=self.save_todo, borderwidth=0 , fg='DodgerBlue2')
        save_fila_but_text.grid(row=2, column=1, padx = 3, sticky='w')


########################################################################################
#                        F U N C T I I   P T    G U I                                  #
########################################################################################
    def _on_mousewheel(self, event):
        '''Mouse wheel'''
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def populeaza_cu_categorii(self, event):
        '''Populare cu categorii de mat.'''
        for widget in self.listbox.winfo_children():
            widget.destroy()
        # resize canvas sau frame_canvas
        categorie = self.categorii.get()  # categoria: ata, banda, ...
        #print(self.lista)
        if categorie != 'TOATE':
            lista_categorie = []
            for _ in self.lista:
                if categorie == _[0]:
                    lista_categorie.append(_)
            dc = {}  # dictionar categorie
            for item in lista_categorie:
                it =  '_'.join(item) + '.csv' # it=nume_fila.csv
                text = (item[3] + " | " + item[1][:10] + ' ' + item[2][:15]).upper()
                dc[text] = it
            dc_list = sorted(dc)

            for key in dc_list:
                bu = tkinter.Button(self.listbox, text=key,
                                    command=lambda it=dc[key]: self.deschide_fila(it),
                                    background = "white", borderwidth = 0,
                                    activeforeground = 'DodgerBlue3')
                bu.grid(sticky='w')
        else:
            self.populeaza_cu_nume()

    def populeaza_cu_nume(self):
        '''Populare cu nume mat.'''
        for widget in self.listbox.winfo_children():
            widget.destroy()

        # Cu dictionar
        d = {}  # dictionar toate fm
        print('self.lista = ', self.lista)
        for item in self.lista:
            it =  '_'.join(item) + '.csv' # it=nume_fila.csv
            text = (item[3] + " | " + item[1][:10] + ' ' + item[2][:15]).upper()
            d[text] = it
        print('d[text] = ', d[text])
        d_list = sorted(d)
        print('d_list = ', d_list)


        for key in d_list:
            bu = tkinter.Button(self.listbox, text=key,
                                command=lambda it=d[key]: self.deschide_fila(it),
                                background = "white", borderwidth = 0,
                                activeforeground = 'DodgerBlue3')
            bu.grid(sticky='w')
            #print(key)
    def populeaza_cu_firme(self, arg):
        '''Populeaza cu firme'''
        for widget in self.listbox.winfo_children():
            widget.destroy()
        categorie = self.firme.get()  # Decathlon, Fendi, etc
        firma = firme.firme  # dictionarul cu firme
        d_firma = firma[categorie]
        for k, v in sorted(d_firma.items()):
            bu = tkinter.Button(self.listbox, text=k,
                                command=lambda it=v: self.deschide_fila(it),
                                background = "white", borderwidth = 0,
                                activeforeground = 'DodgerBlue3')
            bu.grid(sticky='w')

    def refresh(self):
        '''Refresh panel'''
        os.chdir('../FISE_MAGAZIE')
        self.lista_f= os.listdir()  # self.lista_f cu fise de magazie
        for file_name in self.lista_f:
            if file_name.endswith('.nec'):
                self.lista_f.remove(file_name)
        self.lista = []

        for _ in sorted(self.lista_f):
            __ = _.rstrip('.csv').split('_')
            self.lista.append(__)
        cat = set()

        for i in sorted(self.lista_f):
            n = i.split('_')
            var = n[0]
            cat.add(var)
        cat.add('TOATE')
        self.list_cat = sorted(list(cat))

    def salveaza(self):
        '''Salveaza.'''
        data = str(self.data_entry.get())
        document = str(self.document_entry.get())
        doc = document.upper()
        _cantitate = self.cantitate_entry.get()
        ad_sc = self.adauga_scade.get()
        nul = ''  # placeholder

        try:
            self.cantitate = float(_cantitate)
            stoc_vechi = float(self.stoc)
            # ADUNARE
            if ad_sc == 1:
                stoc_nou = self.cantitate + stoc_vechi
                linia = '{:>10}|{:<20}|{:>11.2f}|{:>11}|{:>11.2f}|{:>11}\n'.format(data, doc,self.cantitate, nul,stoc_nou, nul)
                self.fila_deschisa.write(linia)
                e = '{}\n{}\n-----\n{}'.format(self.stoc,_cantitate,stoc_nou)
                self.ultima_linie.configure(text=linia)
                self.entry.delete(0, 'end')
                self.Update(self.da)
                necesar = self.necesar.get()
                opereaza_necesar.opereaza_necesar(self.item, data, doc,
                        self.cantitate, necesar)

            # SCADERE
            elif ad_sc == 2:
                stoc_nou = stoc_vechi - self.cantitate
                linia = '{:>10}|{:<20}|{:>11}|{:>11.2f}|{:>11.2f}|{:>11}\n'.format(data, doc, nul, self.cantitate,stoc_nou, nul)
                self.fila_deschisa.write(linia)
                e = '{}\n{}\n-----\n{}'.format(self.stoc,_cantitate,stoc_nou)
                self.ultima_linie.configure(text=linia)
                self.entry.delete(0, 'end')
                self.Update(self.da)

            # ADUNARE/SCADERE
            elif ad_sc == 3:
                # preia din entry-uri; TOKEN
                try:
                    data_split = data.split('#$')
                    doc_split = doc.split('#$')
                    data_intrare = data_split[0]
                    doc_intrare = doc_split[0]
                    data_iesire = data_split[1]
                    doc_iesire = doc_split[1]
                except IndexError as e:
                    tkinter.messagebox.showinfo('Informare', 'Introduceti:\n2 date si \n2 documente separate de "#$".')
                stoc_nou = self.cantitate + stoc_vechi
                stoc_zero = 0
                linia = '{:>10}|{:<20}|{:>11.2f}|{:>11}|{:>11.2f}|{:>11}\n{:>10}|{:<20}|{:>11}|{:>11.2f}|{:>11.2f}|{:>11}\n'.format(data_intrare,doc_intrare, self.cantitate, nul, stoc_nou, nul, data_iesire, doc_iesire, nul, stoc_nou, stoc_zero, nul)
                self.fila_deschisa.write(linia)
                # afisare ultima linie
                e = '{}\n{}\n-----\n{}'.format(self.stoc,_cantitate,stoc_nou)
                self.ultima_linie.configure(text=linia)
                self.entry.delete(0, 'end')
                self.Update(self.da)
                necesar = self.necesar.get()
                opereaza_necesar.opereaza_necesar(self.item, data, doc, self.cantitate, necesar)

            else:
                tkinter.messagebox.showinfo('Informare', 'Alege o optiune:\nINTRARE sau IESIRE\nsau\nINTRARE/IESIRE')


        except ValueError as e:
            tkinter.messagebox.showinfo('Informare', 'Introduceti Cantitatea (doar cifre)!\nFolositi  "." (punct)  pentru zecimale.')
            self.cantitate_entry.delete(0, 'end') # clear entry
            self.cantitate_entry.focus_set() #focalizeaza pe cantitate


    def afiseaza_data_timpul(self):
        '''Afiseaza data si ora.'''
        self.now = datetime.now()
        d = {'Sunday':'Duminica', 'Monday':'Luni', 'Tuesday':'Marti',
            'Wednesday':'Miercuri', 'Thursday':'Joi', 'Friday':'Vineri',
            'Saturday':'Sambata',}
        ziua = d[self.now.today().strftime('%A')]
        data = self.now.strftime("%d.%m.%Y")
        ziua_data = f'{ziua} - {data}'
        self.ziua_data.configure(text=ziua_data)
        #ora = self.now.strftime("%H:%M")
        #saptamana = f"Saptamana: {self.now.date().isocalendar().week}"
        #self.saptamana.configure(text=saptamana)
        self.update_label_ora()

    def update_label_ora(self):
        '''Update ora'''
        ora = time.strftime('%H:%M')
        self.ora.configure(text = ora)
        self.ora.after(30000, self.update_label_ora)

    def close_windows(self):
        '''close windows'''
        self.fila_deschisa.close()
        self.app.destroy()

    def deschide_todo(self):
        #self.fila_deschisa.close()
        subprocess.call(['notepad.exe', "todo.txt"])

    def save_todo(self):
        '''Save todo'''
        with open("todo.txt", 'w', encoding="utf-8") as f:
            f.write(self.todo.get('1.0', 'end'))

    def deschide_fila_cu_notepad(self):
        '''Deschide fila cu Notepad'''
        self.fila_deschisa.close()
        subprocess.call(['notepad.exe', self.item])  # self.item = fisierul

    def deschide_necesar_cu_notepad(self):
        '''Deschide necesar cu Notepad'''
        self.fila_necesar = self.item.rstrip(".csv") + (".nec")
        print(self.fila_necesar)
        subprocess.call(['notepad.exe', self.fila_necesar])  # self.item = fisierul

    def deschide_director_cu_fm(self):
        '''Deschide folder cu fise magazie.'''
        os.startfile('..\\FISE_MAGAZIE')

    def deschide_director_comenzi(self):
        '''Deschide folderul cu comenzi.'''
        os.startfile('..\\COMENZI')

    def actualizari(self):
        '''Actualizari - Info.'''
        tkinter.messagebox.showinfo('Informare', "Nu este implementat inca")

    def deschide_fila(self, item):
        '''Deschide fisierul.'''
        self.it = item  # face disponibil self.it pt. poze
        # Seteaza ultima_linie la ''
        self.ultima_linie.configure(text='')
        # Citeste fila
        self.item = item
        self.fila_deschisa = open(item, 'r+')
        self.fila = self.fila_deschisa.readlines()
        # Entry cantitate clear/ Clear text widget
        self.cantitate_entry.delete(0, 'end') # clear entry
        self.necesar.delete(0, 'end')
        self.cantitate_entry.focus_set() #focalizeaza pe cantitate
        self.continut_fise.delete(1.0, 'end')
        # Titlu fise magazie
        _titlu = item.rstrip('.csv').split('_')
        titlu = ' '.join(_titlu[1:3]).upper()[:80]
        self.titlu_fise_magazie_label.config(text=titlu)
        # Continut fise afisare
        self.continut_fise.insert(1.0, "".join(self.fila))
        self.continut_fise.yview_moveto(1.0)
        # Citeste ultimul rand
        last_line = self.fila[-1]
        lista_last_line = last_line.split('|')
        self.stoc = lista_last_line[4].strip()


    def but(self):  # LISTBOX DERULARE
        # Lucreaza impreuna cu: but, callback, Scankey, Update
        """Button 'x' clear entry and repopulate listbox"""
        self.entry.delete(0, 'end')
        self.Update(self.da)

    # Callback event - when click the item in list
    def callback(self, event):  # LISTBOX DERULARE
         # Lucreaza impreuna cu: but, callback, Scankey, Update

        selection = event.widget.curselection()
        # selection = (0, ) a cata din lista
        #if selection:
        index = selection[0]
        data = event.widget.get(index)
        it = self.d[data]
        self.deschide_fila(it)
        print(it)


    # Scankey
    def Scankey(self, event):  # LISTBOX DERULARE
        # Lucreaza impreuna cu: but, callback, Scankey, Update

        val = event.widget.get()
        #print(val)  # show printed value (for test)
        if val == '':
            data = self.da
        else:
            data = []
            self.d = {}
            for it in self.da:
                fila = it + ".csv"
                self.d[it] = fila
            self.de_list = sorted(self.d)  # o lista cu keys
            for item in self.de_list:
                if val.lower() in item.lower():
                    #print(val, ' ->', item)
                    data.append(item)

        self.Update(data)
        #print(data)  # ['ADEZIV_ADESIVO UNIFLEX_622_AD 622', ...

    # Update
    def Update(self, data):  # LISTBOX DERULARE
        # Lucreaza impreuna cu: but, callback, Scankey, Update
        # data = [['ADEZIV', 'ADESIVO UNIFLEX', '622', 'AD 622'], ['ADEZIV', ...


        self.listbox.delete(0, 'end')
        self.entry.focus()
        # put new data in listbox
        for item in data:
            self.listbox.insert('end', item)
            #print(item)




#######################################################################
#   F U N C T I I    P E R S O N A L E    D I N    M O D U L E        #
#######################################################################


    def calcul_pierderi(self):
        '''calculeaza consum gresit'''
        pierderi.gui()

    def transform(self):
        '''transformari m2 -> ft2 -> m2'''
        transformari.gui()

    def creaza_fise_magazie(self):
        '''creaza fise de magazie'''
        creaza_fise_magazie.gui(self.lista_f)

    def creaza_nir_bc(self):
        '''creaza nir si bon consum'''
        nir_bc.gui()

    def contabilitate(self):
        '''afiseaza termeni de conta'''
        helpz.contabilitate()

    def dictionar(self):
        '''afiseaza termeni tehnici italiana'''
        helpz.dictionar()

    def ordin(self):
        '''ordin ministru interne'''
        subprocess.Popen(["C:\\Users\\zahfl\\AppData\\Local\\SumatraPDF\\SumatraPDF.exe",
        "../Program/Ordin 2634_2015.pdf"])

    def sendback(self):
        '''Materiale de trimis inapoi'''
        helpz.sendback()

    def contacte(self):
        '''Contacte'''
        helpz.contacte()

    def intrare_iesire_help(self):
        '''Intrare & Iesire'''
        helpz.iih()

    def inlocuieste(self):
        '''Inlocuieste o expresie in fisele de magazie'''
        inlocuiesc.gui()

    def creaza_raport_adeziv(self):
        '''Raport adeziv'''
        pass

    def creaza_raport_stocuri(self):
        '''Raport stocuri'''
        stocuri.gui()

    def open_img(self):
        '''Open image'''
        global a, mat
        radacina = '../POZE_MATERIALE/'
        material = self.it.rstrip('.csv')
        mat = radacina + material + '.jpg'


        def mareste():
            '''Mareste imaginea'''
            global a, mat,b
            a.destroy()
            a = tkinter.Toplevel()
            a.title('Foto')
            try:
                foto = Image.open(mat)
            except FileNotFoundError:
                mat = radacina + "no_image_available" + '.jpg'
                foto = Image.open(mat)
            h = foto.height
            w = foto.width
            foto_resized = foto
            img = ImageTk.PhotoImage(foto_resized)
            l = tkinter.Label(a, image=img)
            l.grid(row=1)
            b = tkinter.Button(a, text='Micsoreaza imaginea', command=micsoreaza)
            b.grid(row=0, sticky='we')
            a.mainloop()


        def micsoreaza():
            '''Micsoreaza imaginea'''
            global a, mat, b
            a.destroy()
            a = tkinter.Toplevel()
            a.title('Foto')
            try:
                foto = Image.open(mat)
            except FileNotFoundError:
                mat = radacina + "no_image_available" + '.jpg'
                foto = Image.open(mat)
            h = foto.height
            w = foto.width
            foto_resized = foto.resize((int(w/2), int(h/2)))
            img = ImageTk.PhotoImage(foto_resized)
            l = tkinter.Label(a, image=img)
            l.grid(row=1)
            b = tkinter.Button(a, text='Mareste imaginea', command=mareste)
            b.grid(row=0, sticky='we')
            a.mainloop()


        # Display image - initial view
        a = tkinter.Toplevel()
        a.title('Foto')
        try:
            foto = Image.open(mat)
        except FileNotFoundError:
            mat = radacina + "no_image_available" + '.jpg'
            foto = Image.open(mat)
        h = foto.height
        w = foto.width
        foto_resized = foto.resize((int(w/2), int(h/2)))
        img = ImageTk.PhotoImage(foto_resized)
        l = tkinter.Label(a, image=img)
        l.grid(row=1)
        b = tkinter.Button(a, text='Mareste imaginea', command=mareste)
        b.grid(row=0, sticky='we')
        a.mainloop()


if __name__ == '__main__':
    root = tkinter.Tk()
    app = FiseDeMagazie(root)
    root.mainloop()
