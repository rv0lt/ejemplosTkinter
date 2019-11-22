from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Progressbar
def clicked():
    #lee la variable txt y modifica el contenido de lbl
    res= "Welcome to " + txt.get()
    lbl.configure(text=res)
def clicked_2():
    #Obtiene el valor de la variable selected y lo imprime
    print(selected.get())
def clicked_3():
    messagebox.showerror(":(", "Muy Mal")
if __name__ == '__main__':
    window=Tk()
    window.title("Esto es una prueba")
    window.geometry('800x600')
    
    #Texto Escrito que se guarda en la variable lbl
    lbl = Label(window, text="hello")
    #grid configura la posicion del elemento
    lbl.grid(column=0, row=0)

    #Entrada de datos que se guardan en la variable txt
    txt = Entry(window, width=10)
    #txt = Entry(window, width=10, state="disabled")
    #Al añadir el state="disabled" impedimos que sobre está entrada se puedan escribir datos
    txt.grid(column=1, row=0)

    #Crea un boton que al seleccionarse ejecuta la funcion clicked
    btn= Button(window, text="Click me", command=clicked)
    btn.grid(column=2, row=0)

    #Crea un elemento que despliega una lista de la cual se puede seleccionar
    cmb_values=(1,2,3, "Holi", "Loretito")#Tupla con los eltos que tendra la lista
    combo= Combobox(window)
    combo['values'] = cmb_values
    combo.current(0)#El elto preseleccionado es el que tenga la posicion 0 de la tupla
    combo.grid(column=0, row=1)
    #combo.get() Obtiene el valor seleccionado de la lista
    
    #Crea una casilla de verificación
    chk_state=BooleanVar().set(True) #set check state
    chk=Checkbutton(window, text="Marcame",  var=chk_state)
    chk.grid(column=1, row=1)
    
    #Crea 3 elementos, tales que al marcar uno el que lo estuviera previamente se deseleccionaria
    selected=IntVar()
    rad1=Radiobutton(window, text='First', value=1, variable=selected)    
    rad2=Radiobutton(window, text='Second', value=2, variable=selected)    
    rad3=Radiobutton(window, text='Third', value=3,variable=selected)    
    rad1.grid(column=0, row=2)
    rad2.grid(column=1, row=2)
    rad3.grid(column=2, row=2)
    #Crea un boton que al darle click llama a clicked_2, el cual escribira por terminal el valor del elto seleccionado
    btn_2=Button(window, text="Click", command=clicked_2)
    btn_2.grid(column=3, row=2)
    #txt.focus()
    #txt_2 es un texto largo(scroll)
    txt_2= scrolledtext.ScrolledText(window, width=40,height=10)#Si no se le especifica tamaño llenará toda la pantalla
    txt_2.grid(column=0, row=3)
    txt_2.insert(INSERT, "Hola!!!!")
    #boton que llama a una funcion la cual muesttra un messagebox de error
    btn_3= Button(window, text= "NO ME PULSES", command= clicked_3)
    btn_3.grid(column=1, row=3)
    
    #Muesta un cuadro que pregunta al usuario, si se hace click en yes se devolvera True, si se hace en no devolvera False
    res=messagebox.askyesno('Pregunta muy importante', "¿Te gustan las patatas?")
    #res=messagebox.askquestion
    #res=messagebox.askyesnocancel
    #res=messagebox.askokcancel
    #messagebox.askretrycancel
    
    #Crea un widget el cual permite elegir un numero de entre un rango dado
    spin=Spinbox(window, from_=0, to=100)
    spin.grid(column=0, row=4)
    
    #Crear una barra de progreso
    bar=Progressbar(window,length=200)
    bar['value'] = 70
    bar.grid(column=1, row=4)

    #Añadir barras de menu
    #menu=Menu(window)
    #menu.add_command(label='Miau')
    #Agregar nuevos elementos al menu
    #menu.add_cascade(label='Guau', menu=menu)
    #Asociar el menu a la ventana
    #window.config(menu=menu)
    window.mainloop()

