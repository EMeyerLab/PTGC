import PTGC as tc

import PIL.Image
from PIL import ImageTk

from math import log
import os
from tkinter import *

def get_q(Un, n, U0):
    return log(Un/U0) / (n*log(2))

def get_n(Un, U0, q):
    return log(Un/U0) / (q*log(2))

def get_U0(Un, n, q):
    return Un/(2**(n*q))

def get_Un(U0, q, n):
    return U0*(2**(n*q))

def calculer(U0, n, q, Un, fields):
    # print(U0,n,q,Un)

    vU0 = U0.get()
    vn = n.get()
    vq = q.get()
    vUn = Un.get()


    missings = []
    answer = ""
    output = "When we have the followings : "

    if not vU0:
        missings.append("U0")
    else:
        output = output+" U0={} ".format(vU0)
    if not vn:
        missings.append("n")
    else:
        output = output+" n={} ".format(vn)
    if not vq:
        missings.append("q")
    else:
        output = output+" q={} ".format(vq)
    if not vUn:
        missings.append("Un")
    else:
        output = output+" Un={} ".format(vUn)

    if len(missings) > 1:
        answer = " --> Then we don't have enough information to compute anything"
    elif len(missings) == 0:
        answer = " --> Then nothing needs to be computed"
    elif len(missings) == 1:
        if missings[0] == "U0":
            answer = ", then we can guess that {} = {}".format("U0",str(get_U0(float(vUn), float(vn),float(vq))))
        if missings[0] == "n":
            answer = ", then we can guess that {} = {}".format("n",str(get_n(float(vUn), float(vU0),float(vq))))
        if missings[0] == "q":
            answer = ", then we can guess that {} = {}".format("q",str(get_q(float(vUn), float(vn), float(vU0))))
        if missings[0] == "Un":
            answer = ", then we can guess that {} = {}".format("Un",str(get_Un(float(vU0),float(vq),float(vn))))
    output = output + answer

    U0.set("")
    n.set("")
    q.set("")
    Un.set("")


    champs5 = Label(fields,text="{}".format(output))
    champs5.config(font=("Times New Roman", 15))
    champs5.pack()
    fields.pack()



def PTGC_GUI():
    fenetre = Tk()
    fenetre.title("PTGC")
    fenetre.resizable(height = None, width = None)

    # img_path = os.path.abspath(os.path.dirname(__file__)+"/../../images/")
    # imgicon = PhotoImage(file=os.path.join(img_path,'icone.ppm'))
    # fenetre.tk.call('wm', 'iconphoto', fenetre._w, imgicon)

    fenetre.geometry('800x480')
    ############


    fields = Frame(fenetre)

    top_msg = Label(fields,text="""
    Enter 3 parameters among those 4:
    """)
    top_msg.config(font=("Arial",22))
    top_msg.pack()

    champs1 = Label(fields,text="Number of cells at J0 ? (U0)")
    champs1.config(font=("Times New Roman", 15))
    champs1.pack()
    var_texte = StringVar()
    ligne_texte = Entry(fields, textvariable=var_texte)
    ligne_texte.pack()

    champs2 = Label(fields,text="Number of days ? (n)")
    champs2.config(font=("Times New Roman", 15))
    champs2.pack()

    var_texte2 = StringVar()
    ligne_texte2 = Entry(fields, textvariable=var_texte2)
    ligne_texte2.pack()

    champs3 = Label(fields,text="Number of division every 24 hour ? (q)")
    champs3.config(font=("Times New Roman", 15))
    champs3.pack()
    var_texte3 = StringVar()
    ligne_texte3 = Entry(fields, textvariable=var_texte3)
    ligne_texte3.pack()

    champs4 = Label(fields,text="Number of cells at day n ? (Un)")
    champs4.config(font=("Times New Roman", 15))
    champs4.pack()
    var_texte4 = StringVar()
    ligne_texte4 = Entry(fields, textvariable=var_texte4)
    ligne_texte4.pack()

    bouton_calculer = Button(fields, text="Compute", command=lambda: calculer(var_texte, var_texte2,var_texte3,var_texte4,fields))
    bouton_calculer.pack()

    # champs5 = Label(fields,text=f"\nRésultat : ? ")
    # champs5.config(font=("Times New Roman", 15))
    # champs5.pack()

    fields.pack()

    #### Illustration of equations



    fenetre.mainloop()

if __name__ == '__main__':
    PTGC_GUI()
