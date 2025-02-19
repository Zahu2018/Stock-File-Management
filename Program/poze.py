# Arata poze in window
# Tags = #picture, #display\
'''text here'''
import tkinter
from PIL import Image, ImageTk


class MARE:
    ...
def imag_size_original():  # deschide imaginea la marimea originala
    ...
    return 
 
def gui(path_poza_material, app):
    foto = Image.open(path_poza_material)
    h = foto.height
    w = foto.width
    foto_resized = foto.resize((int(w/2), int(h/2)))
    x = 7
    
    
    
    a = tkinter.Toplevel(app)
    img = ImageTk.PhotoImage(foto_resized)
    l = tkinter.Label(image=img)
    l.grid()
   
    a.mainloop()
    

if __name__ == "__main__":
    gui('D:\SIMLEU SHOES\POZE_MATERIALE\BANDA_LYCRA_384+LEDIA BORDINO NERO 9265 H.16MM IDRO_LYL NE16I.jpg', app)
