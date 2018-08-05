from tkinter import*
from tkinter import ttk

def mainWindow():
    dias = []
    años = []
    for dia in range(1,32):
        dias+=[dia]
    for año in range(1949,2019):
        años+=[año]

    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
           "Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
    
    root=Tk()
    root.resizable(False,False)
    root.title("Sign up page")
    root.geometry("650x550+400+100")
    root.config(bg="White")
    font1=("Segoe UI Light",24,"bold")
    font2=("Segoe UI Light",14)
    Label(root,bg="#38403D",width=1000,height=8).place(x=1,y=1)
    Label(root,bg="#38403D",text="Crea una cuenta",fg="white",font=font1).place(x=50,y=10)
    Label(root,bg="#38403D",text="Es gratis y lo será siempre",fg="white",font=font2).place(x=50,y=55)
    Label(root,bg="#CAE5DC",height=100,width=1000).place(x=1,y=100)
    #Nombre
    Label(root,bg="#CAE5DC",fg="#38403D",text="Nombre",font=font2).place(x=50,y=120)
    Entry(root,bg="white",fg="#38403D",width=25,font=font2).place(x=50,y=150)
    #Apellidos
    Label(root,bg="#CAE5DC",fg="#38403D",text="Apellidos",font=font2).place(x=340,y=120)
    Entry(root,bg="white",fg="#38403D",width=25,font=font2).place(x=340,y=150)
    #Correo
    Label(root,bg="#CAE5DC",fg="#38403D",text="Correo",font=font2).place(x=50,y=200)
    Entry(root,bg="white",fg="#38403D",width=54,font=font2).place(x=50,y=230)
    #Password
    Label(root,bg="#CAE5DC",fg="#38403D",text="Contraseña",font=font2).place(x=50,y=280)
    Entry(root,bg="white",fg="#38403D",width=25,font=font2,show="*").place(x=50,y=310)
    Label(root,bg="#CAE5DC",fg="#38403D",text="Vuelva a introducir contraseña",font=font2).place(x=50,y=350)
    Entry(root,bg="white",fg="#38403D",width=25,font=font2,show="*").place(x=50,y=380)
    #Fecha de nacimiento
    Label(root,bg="#CAE5DC",fg="#38403D",text="Fecha de nacimiento(Mes/Día/Año)",font=font2).place(x=339,y=280)
    ttk.Combobox(root,values=meses,font=font2,width=9).place(x=340,y=310)
    ttk.Combobox(root,values=dias,font=font2,width=2).place(x=460,y=310)
    ttk.Combobox(root,values=años,font=font2,width=4).place(x=510,y=310)
    #Genero
    Label(root,bg="#CAE5DC",fg="#38403D",text="Género",font=font2).place(x=339,y=350)
    #Label(root,bg="#CAE5DC",fg="#38403D",text="Femenino",font=("Segoe UI Light",12)).place(x=339,y=380)
    Radiobutton(root,text="Femenino",bg="#CAE5DC",fg="#38403D",font=font2,value=1).place(x=350,y=380)
    Radiobutton(root,text="Masculino",bg="#CAE5DC",fg="#38403D",font=font2,value=2).place(x=500,y=380)
    #Button
    Button(root,width=55,font=font2,height=2,bg="#38403D",fg="#CAE5DC",text="crear cuenta").place(x=50,y=450)
mainWindow()
