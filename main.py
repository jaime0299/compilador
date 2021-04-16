#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from Archivo import *
from tkinter import filedialog as fd
import tkinter.ttk as ttk
from tkinter import messagebox
from Arbol import *
from intermedio import *
from Intermedio2 import *
from optimizacion2 import *
from PIL import ImageTk,Image

A = Archivo()
Ar= Arbol()
Inter = Intermedio()
Inter2=Tablas()
op2=Optimizacion()
class  Principal:

    def __init__(self):

        global p_res, tipo_d, operadores, clases, nums
        p_res=['int', 'cad', 'decimal', 'char', 'ask', 'show', 'Begin', 'End']
        clases=['PR','PR','PR','PR','PR','PR']
        tipo_d = ['int', 'cad', 'decimal', 'char']
        operadores = ['+', '-', '*', '/', '=']
        nums = ['0','1','2','3','4','5','6','7','8','9']
        self.error=False

    def Ventana(self):

        global texto,texto1,ventana
        
        ventana = Tk()
        ventana.geometry("740x685+300+20")
        ventana.title("Compilador del Pinguino")
        ventana.config(bg="black")

        #LabelFrame #1 ---> Cargan los archivos txt desde los archivos
        LF1 = LabelFrame(ventana, text = " Cargar Archivo ",height = 53,width = 383,bg="black",fg="white")
        LF1.place(x=10,y=10)

        var = StringVar()
        E1 = Entry(ventana,textvariable=var,width = 50,state="disable")
        E1.place(x=20,y=30)

        self.Btn_Cargar = Button(ventana,text="BUSCAR",bg="gray",fg="black",command=lambda: self.Cargar_Datos_Archivo(E1,texto))
        self.Btn_Cargar.place(x=330,y=28)

        #LabelFrame #2 ---> Funciones extras como Examinar archivo y Limpiar
        LF2 = LabelFrame(ventana, text = " Funciones ",height = 53,width = 328,bg="black",fg="white")
        LF2.place(x=400,y=10)

        self.Btn_Examinar = Button(ventana,text="EXAMINAR",bg="GREEN",fg="black",width=20,command=lambda: self.Examinar())
        self.Btn_Examinar.place(x=410,y=28)

        self.Btn_Limpiar = Button(ventana,text="LIMPIAR",bg="RED",fg="black",width=20,command=lambda: self.Limpiar(texto,texto1,E1),state="normal")
        self.Btn_Limpiar.place(x=570,y=28)

        #LabelFrame #3 ---> Archivo de txt que contiene el codigo
        LF3 = LabelFrame(ventana, text = " Archivo.txt ",height = 600,width = 383,bg="black",fg="white")
        LF3.place(x=10,y=73)
        
        SBFRAME = Frame(ventana)
        texto = Text(SBFRAME, height=27, width=38,font=('Times New Roman','14'),wrap=WORD)
        scroll = Scrollbar(SBFRAME, command=texto.yview)
        texto.configure(yscrollcommand=scroll.set)
        texto.tag_bind('bite', '<1>', lambda e, t=texto: t.insert(END, "Texto"))
        texto.pack(side=LEFT,fill=BOTH)
        scroll.pack(side=RIGHT, fill=Y)
        SBFRAME.place(x=20, y=93)
        
        #LabelFrame #4 ---> Tabla
        LF4 = LabelFrame(ventana, text = " Tabla ",height = 218,width = 328,bg="black",fg="white")
        LF4.place(x=400,y=73)

        SBFRAME2 = Frame(ventana)
        SB = Scrollbar(SBFRAME2, relief=RAISED)
        SB.pack(side=RIGHT, fill=Y)
        self.Table = ttk.Treeview(SBFRAME2, columns=("T","C", "A","D","R"), height=8,selectmode=BROWSE, yscrollcommand=SB.set)
        self.Table.pack(side=LEFT, fill=BOTH)
        self.Table.heading("#0", text="No.")
        self.Table.column("#0", minwidth=40, width=40, anchor=CENTER)
        self.Table.heading("T", text="T")
        self.Table.column("T", minwidth=50, width=50, anchor=CENTER)
        self.Table.heading("C", text="C")
        self.Table.column("C", minwidth=55, width=55, anchor=CENTER)
        self.Table.heading("A", text="A")
        self.Table.column("A", minwidth=40, width=40, anchor=CENTER)
        self.Table.heading("D", text="D")
        self.Table.column("D", minwidth=40, width=40, anchor=CENTER)
        self.Table.heading("R", text="R")
        self.Table.column("R", minwidth=59, width=59, anchor=CENTER)
        SB.config(command=self.Table.yview)
        SBFRAME2.place(x=410, y=93)

        #LabelFrame #5 ---> Botones extras (Léxico,Sintáctico,...,etc)
        LF4 = LabelFrame(ventana, text = " Botones ",height = 205,width = 328,bg="black",fg="white")
        LF4.place(x=400,y=293)

        y = 313
        colorfg = "white"
        colorbg = "black"

        self.Btn_Lexico = Button(ventana,text="LÉXICO",bg=colorbg,fg=colorfg,width=43,command=lambda: self.mandaL(),state="disabled")
        self.Btn_Lexico.place(x=410,y=y)
        y += 30 

        self.Btn_Sintatico = Button(ventana,text="SINTÁCTICO",width=43,bg=colorbg,fg=colorfg,command=lambda: self.Sintactico(),state="disabled")
        self.Btn_Sintatico.place(x=410,y=y)
        y += 30
        
        self.Btn_Semantico = Button(ventana,text="SEMÁNTICO",width=43,bg=colorbg,fg=colorfg,command=lambda: self.Semantico(),state="disabled")
        self.Btn_Semantico.place(x=410,y=y)
        y += 30

        self.Btn_CI = Button(ventana,text="CÓDIGO INTERMEDIO",width=43,bg=colorbg,fg=colorfg,command=lambda: self.Codigo_Intermedio(),state="disabled")
        self.Btn_CI.place(x=410,y=y)
        y += 30

        self.Btn_Optimizacion = Button(ventana,text="OPTIMIZACIÓN",width=43,bg=colorbg,fg=colorfg,command=lambda: self.Optimizacion(),state="disabled")
        self.Btn_Optimizacion.place(x=410,y=y)
        y += 30

        self.Btn_CO = Button(ventana,text="CÓDIGO OBJETO",width=43,bg=colorbg,fg=colorfg,command=lambda: self.Codigo_Objeto(),state="disabled")
        self.Btn_CO.place(x=410,y=y)
        y += 30

        #LabelFrame #6 ---> Terminal
        LF6 = LabelFrame(ventana, text = " Terminal ",height = 173,width = 328,bg="black",fg="white")
        LF6.place(x=400,y=500)

        SBFRAME1 = Frame(ventana)
        texto1 = Text(SBFRAME1, height=7, width=36,font=('Times New Roman','12'),wrap=WORD,state='disabled')
        scroll1 = Scrollbar(SBFRAME1, command=texto1.yview)
        texto1.configure(yscrollcommand=scroll1.set)
        texto1.tag_bind('bite', '<1>', lambda e, t=texto1: t.insert(END, "Texto"))
        texto1.pack(side=LEFT,fill=BOTH)
        scroll1.pack(side=RIGHT, fill=Y)
        SBFRAME1.place(x=410, y=520)

        ventana.mainloop()

    def Cargar_Datos_Archivo(self,E1,texto):

        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        
        if (nombrearch != ""):
            Lista = []
            Lista = A.Sacar(nombrearch) 
            E1.config(state='normal')
            E1.delete(0,END)
            E1.insert(END,str(nombrearch))
            E1.config(state='disabled')

            texto.config(state='normal')
            texto.delete("1.0","end-1c")
            for i in range(len(Lista)):
                texto.insert(END,str(Lista[i] + "\n"))
            #texto.config(state='disabled')

            self.Btn_Examinar.config(state='normal')
            #self.Btn_Cargar.config(state='disabled')
        else:
            print ("No selecciono un archivo.")

    def Examinar(self):

        self.Btn_Lexico.config(bg="darkblue",fg="black",state='normal')
        self.Btn_Examinar.config(state='normal')

    def mandaL(self):
        self.Btn_Lexico.config(state="disabled")
        self.Lexico()
        self.addtable()

    def Errores(self,Error,Linea):
        self.error=True
        texto1.config(state='normal')
        texto1.delete("1.0", "end-1c")
        texto1.insert(END, Error+" (Linea " + str(Linea) + ")")
        texto1.config(fg="RED")
        texto1.config(state='disabled')

    def Lexico(self):
        global tokens,ini,fin,revi
        texto1.delete("1.0", "end-1c")
        self.Table.delete(*self.Table.get_children())
        texto1.delete("1.0","end")
        self.error=False
        txt=texto.get('1.0','end-1c')
        codi = txt.split("\n")
        tokens=[]
        revi=[]
        ini=-1
        fin=-1
        codigo=[]
        for i in range(len(codi)):
            if codi[i]=="Begin":
                ini=i
            elif codi[i]=="End" and ini!=(-1):
                fin=i
                break

        tokens.append(["Begin","PR","0",ini,"-"])
        c=ini+1
        string=False
        while c<fin:
            end_l=False
            linea=codi[c].split(" ")
            string=False
            print (linea)
            for i in linea:
                if (len(i)>1):
                    if i[0] == "/" and i[1] == "/":
                        break
                if i.endswith(";"):
                    i=i[0:len(i)-1]
                    end_l=True
                if i.startswith("\"") or i.endswith("\""):
                    if string or i.endswith("\""):
                        string = False
                    else:
                        string=True
                elif i in p_res and string==False:
                    if i not in revi:
                        cl = clases[p_res.index(i)]
                        tokens.append([i, cl, '0', c, '-'])
                        revi.append(i)
                    else:
                        self.agrega_rep(i,c)
                elif i not in p_res and string==False:
                   exp=""
                   for j in i:
                       if j in operadores or j==",":
                            if j not in revi:
                                cl='Caracter'
                                if j in operadores:
                                    cl='Operador'
                                tokens.append([j, cl, '0', c, '-'])
                                revi.append(j)
                            else:
                                self.agrega_rep(j,c)
                            if exp!="":
                                if self.checknum(exp,c)==False:
                                    return
                            exp=""
                       elif j!=" ":
                           exp+=j

                   if exp!="":
                       if self.checknum(exp,c)==False:
                           return
            """if string:
                self.Errores("Error léxico: Declaración ilegal de cadena.\n",c)
                return"""
            if end_l==False:
                pass
            else:
                if ";" not in revi:
                    tokens.append([";", "Caracter", "0", c, "-"])
                    revi.append(";")
                else:
                    self.agrega_rep(";",c)
            c+=1
        return

    def Sintactico(self):
        self.Btn_Sintatico.config(state="disabled")
        txt = texto.get('1.0', 'end-1c')
        codi = txt.split("\n")
        string = False
        c=0
        fin=len(codi)
        codigo=[]
        while c<fin:
            string=False
            con_com=0
            linea=codi[c]
            exp=""
            cade=""
            for i in range(len(linea)):
                if linea[i]=="/" and linea[i+1]=="/":
                    if exp!="":
                        codigo.append(exp)
                    break
                elif linea[i]=="\"":
                    exp+=linea[i]
                    string = not string
                    if string==False:
                        codigo.append(exp)
                        exp=""
                elif linea[i] in operadores or linea[i]=="," or linea[i]==";" and string==False:
                    if exp!="":
                        codigo.append(exp)
                    codigo.append(linea[i])
                    exp=""
                elif linea[i]==" ":
                    if string:
                        exp += linea[i]
                else:
                    exp+=linea[i]

                if exp in p_res and string==False:
                    codigo.append(exp)
                    exp=""
            if string:
                if exp!="":
                    codigo.append(exp)
            c+=1
        print("CODIGO:")
        print (codigo)
        self.codigo_s=codigo
        self.analiza_retro(codigo)

    def analiza_retro(self,cad):
        global gram
        ven=Toplevel()
        ven.title("Análisis")
        ven.geometry("1320x750+5+5")
        SBFRAME = Frame(ven)
        texto3 = Text(SBFRAME, height=27, width=140, font=('Times New Roman', '14'), wrap=WORD)
        scroll = Scrollbar(SBFRAME, command=texto3.yview)
        texto3.configure(yscrollcommand=scroll.set)
        texto3.tag_bind('bite', '<1>', lambda e, t=texto3: t.insert(END, "Texto"))
        texto3.pack(side=LEFT, fill=BOTH)
        scroll.pack(side=RIGHT, fill=Y)
        SBFRAME.place(x=0, y=0)

        cad.append("#")
        abc = ["a", "b", "c", "d", "e", "f"]
        lets = [[""], ["|let"], ["|num"]]
        self.cl = 0
        # gram = [["S",1,"x"],["S",2,"(|S|R"],["R",1,",|S|R"],["R",2,")"]]    #Gramatica 1
        # gram = [["S",1,"c|A"],["A",1,"a|B"],["B",1,"b"],["B",2,"e"]]       #Gramatica 2
        gram = [["Programa", 1, "Begin|Sentencias|End"],
                ["Programa", 2, "Begin|End"],
                ["Sentencias", 1, "Declaracion"],
                ["Sentencias", 2, "Imprimir"],
                ["Sentencias", 3, "Declaracion|Sentencias"],
                ["Sentencias", 4, "Imprimir|Sentencias"],
                ["Declaracion", 1, "tipo_dato|Variable|;"],
                ["Declaracion", 2, "Variable|=|ask|cadena|;"],
                ["Declaracion", 3, "Variable|=|Exp|;"],
                ["tipo_dato", 1, "int"],
                ["tipo_dato", 2, "cad"],
                ["tipo_dato", 3, "char"],
                ["tipo_dato", 4, "decimal"],
                ["Variable", 1, "var"],
                ["Variable", 2, "var|,|Variable"],
                ["Exp", 1, "Variable"],
                ["Exp", 2, "Numero"],
                ["Exp", 3, "cadena"],
                ["Exp", 4, "Operacion"],
                ["Exp", 5, "Variable|,|Exp"],
                ["Exp", 6, "Numero|,|Exp"],
                ["Exp", 7, "cadena|,|Exp"],
                ["Exp", 8, "Operacion|,|Exp"],
                ["Numero", 1, "num"],
                ["cadena", 1, "cade"],
                ["Operacion", 1, "Numero|operador|Numero"],
                ["Operacion", 2, "Variable|operador|Variable"],
                ["Operacion", 3, "Numero|operador|Variable"],
                ["Operacion", 4, "Variable|operador|Numero"],
                ["Operacion", 5, "Variable|operador|Operacion"],
                ["Operacion", 6, "Numero|operador|Operacion"],
                ["Operacion", 7, "cadena|operador|cadena"],
                ["Operacion", 8, "cadena|operador|Variable"],
                ["Operacion", 9, "Variable|operador|cadena"],
                ["operador", 1, "+"],
                ["operador", 2, "-"],
                ["operador", 3, "/"],
                ["operador", 4, "*"],
                ["Imprimir", 1, "show|Exp|;"]
                ]
        NT = ["Programa", "Sentencias", "Declaracion", "tipo_dato", "Variable", "Exp", "Numero", "cadena",
              "Operacion", "operador", "Imprimir"]
        # NT = ["S","R"]          #No terminales 1
        # NT =["S","A","B"]      #No terminales 2

        SI = "Programa"  # Estado inicial
        # cad = ["(","x",",","(","x",",","x",")",")","#"]     #Cadena 1
        # cad = ["c","a","d","#"]                #Cadena 2
        """cad = ["Begin",
               "int", "a", ",", "suma", ",", "b", ";",
               "cad", "msj", ";",
               "msj", "=", "\"Hola\"", ";",
               "show", "msj", ";",
               "suma", "=", "a", ";", "show", "\"Suma es igual a: \"", ",", "suma", ";",
               "End", "#"]"""
        es = "n"
        c = 0
        pila = ["@"]
        fin = [SI, "#"]

        l = []
        l.append(es)
        l.append(c + 1)
        l.append(pila)
        l.append(fin)
        texto3.insert(END, l)
        texto3.insert(END, "\n")
        regla = "1"
        while es != "t" and es != "e":
            if es == "n":
                if fin[0] in NT:
                    regla = "Regla 1"
                    if pila[0] == "@":
                        pila[0] = fin[0]
                    else:
                        pila.append(fin[0])
                    num, prod = self.busca(fin[0])
                    fin.pop(0)
                    pila[len(pila) - 1] += "|" + str(num)
                    fin = prod + fin
                elif fin[0] == "var":
                    if self.checkvar(cad[c]):
                        regla = "Regla 2"
                        pila.append(fin[0])
                        fin.pop(0)
                        c += 1
                    else:
                        regla = "Regla 4"
                        es = "r"
                elif fin[0] == "cade":
                    if cad[c].startswith("\"") and cad[c].endswith("\""):
                        regla = "Regla 2"
                        pila.append(fin[0])
                        fin.pop(0)
                        c += 1
                    else:
                        regla = "Regla 4"
                        es = "r"
                elif fin[0]=="num":
                    if self.checknum2(cad[c]):
                        regla = "Regla 2"
                        pila.append(fin[0])
                        fin.pop(0)
                        c += 1
                    else:
                        regla = "Regla 4"
                        es = "r"
                elif fin[0] == cad[c] and cad[c] != "#":
                    regla = "Regla 2"
                    pila.append(fin[0])
                    fin.pop(0)
                    c += 1
                elif fin[0] == "#":
                    regla = "Regla 3"
                    es = "t"
                elif fin[0] != cad[c]:
                    regla = "Regla4"
                    es = "r"
            elif es == "r":
                sim = pila[len(pila) - 1]
                sim = sim.split("|")
                if sim[0] not in NT:
                    regla = "Regla 5"
                    fin.insert(0, pila[len(pila) - 1])
                    pila.pop(len(pila) - 1)
                    c -= 1
                else:
                    ban, pr_ant, pr_nu = self.busca_2(sim)
                    if ban:
                        regla = "Regla 6a"
                        es = "n"
                        for i in range(len(pr_ant)):
                            fin.pop(0)
                        fin = pr_nu + fin
                        num = int(sim[1]) + 1
                        pila[len(pila) - 1] = sim[0] + "|" + str(num)
                    elif ban == False and sim[0] == SI:
                        regla = "Regla 6b"
                        es = "e"
                    else:
                        regla = "Regla 6c"
                        for i in range(len(pr_ant)):
                            fin.pop(0)
                        fin.insert(0, sim[0])
                        pila.pop(len(pila) - 1)
            l = []
            l.append(es)
            l.append(c + 1)
            l.append(pila)
            l.append(fin)
            texto3.insert(END,regla)
            texto3.insert(END, "\n")
            texto3.insert(END,l)
            texto3.insert(END, "\n")

        if es == "t":
            print("TERMINADO Y ACEPTADA")
            texto3.insert(END,"TERMINADO Y ACEPTADA")
            messagebox.showinfo("Éxito", "La cadena de entrada ha sido aceptada.")
            self.Btn_Semantico.config(state="normal")
        else:
            print("ERROR, CADENA RECHAZADA")
            texto3.insert(END,"ERROR, CADENA RECHAZADA")
            messagebox.showerror("Error", "La cadena de entrada ha sido rechazada.")

    def busca(self,sim):
        for i in range(len(gram)):
            if gram[i][0] == sim:
                l = gram[i][2].split("|")
                return gram[i][1], l

    def busca_2(self,sim):
        ban = False
        pr_ant = []
        pr_nu = []
        for i in range(len(gram)):
            if gram[i][0] == sim[0] and gram[i][1] == int(sim[1]):
                pr_ant = gram[i][2].split("|")
            elif gram[i][0] == sim[0] and gram[i][1] > int(sim[1]):
                ban = True
                pr_nu = gram[i][2].split("|")
                break
        return ban, pr_ant, pr_nu

    def agrega_rep(self,tok,line):
        for z in range(len(tokens)):
            if tokens[z][0]==tok:
                if tokens[z][4]=="-":
                    tokens[z][4]=str(line)
                else:
                    tokens[z][4]+=", "+str(line)
                break

    def checknum(self,exp,c):
        cl = ""
        if exp[0] in nums:
            cl = "Caracter"
            am="0"
            for x in exp:
                if x not in nums and x!=".":
                    self.Errores("Error léxico. Número inválido. \n", c)
                    return False
        else:
            cl = "ID"
            am="1"
            if self.checkvar(exp) == False:
                self.Errores("Error léxico. Variable inválida o "
                             "palabra reservada erronea.\n", c)
                return False
        if exp not in revi:
            tokens.append([exp, cl, am, c, '-'])
            revi.append(exp)
        else:
            self.agrega_rep(exp,c)
        return

    def checknum2(self, numero):
        try:
            n = float(numero)
            return True
        except:
            return False

    def checkvar(self, variable):

        var = str(variable)
        # var = str(input("Introduce una cadena: "))
        #
        print("Variable: ", var)

        Lista = []
        Minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        Mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        Numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

        Mex = True
        for i in range(len(str(var))):
            Lista.append(str(var[i]))
            # print ("A: ",str(var[i]),", POS: ",i)
            if (i == 0 and str(var[i]) in Minusculas or str(var[i]) in Mayusculas and str(var[i]) not in Numeros):
                # print ("Pasa Restriccion 1")
                Mex = True
            elif (i == 0 and (str(var[i]) not in Minusculas or str(var[i]) not in Mayusculas)):
                print("Error 1")
                Mex = False
                break
            elif (i >= 1 and str(var[i]) != " " and (
                    str(var[i]) in Minusculas or str(var[i]) in Mayusculas or str(var[i]) in Numeros)):
                # print ("Pasa Restriccion 2")
                Mex = True
            if (i >= 1 and str(var[i]) == " " or (
                    str(var[i]) not in Minusculas and str(var[i]) not in Mayusculas and str(var[i]) not in Numeros)):
                print("Error 2")
                Mex = False
                break

        if (Mex):
            print(var, " Se Acepta como variable.")
            return True
        else:
            print(var, " No se Acepta como variable")
            return False

    def addtable(self):
        print(tokens)
        if self.error==False:
            tokens.append(["End", "PR", "0", fin, "-"])
        for i in range(len(tokens)):
            self.Table.insert("",END,text=str(i+1),values=(tokens[i][0],tokens[i][1],tokens[i][2],tokens[i][3],tokens[i][4]))
        self.Btn_Sintatico.config(state="normal")

    def Semantico(self):
        codigo = self.codigo_s
        # self.Btn_CI.config(state='normal')
        self.Btn_Semantico.config(state="disabled")

        Lista_Opera = []

        TIPO = ["int", "cad", "decimal", "char"]
        OPERA = ["+", "-", "*", "/"]
        VAR = []
        TIPOS = []
        t = ""
        posi = 0
        posf = 0
        bshow=False
        for i in range(len(codigo)):
            if codigo[i] in TIPO:
                t = codigo[i]
            elif codigo[i] != "," and codigo[i] != ";" and t != "":
                if codigo[i] in VAR:
                    self.Error_Sema("Variable Repetida.")
                    return
                VAR.append(codigo[i])
                TIPOS.append(t)
            elif codigo[i] == ";":
                t = ""
            if codigo[i]=="show":
                bshow=True
            elif bshow and codigo[i] not in OPERA and codigo[i]!=",":
                print("PASA1")
                if codigo[i]==";":
                    bshow=False
                elif self.checknum2(codigo[i]) or (codigo[i].startswith("\"") and codigo[i].endswith("\"")):
                    pass
                elif codigo[i] not in VAR:
                    print("PASA2")
                    self.Error_Sema("Identifiadores no Declarados.")
                    return
            if codigo[i] == "=":
                V = []
                T = []
                posi = i - 1
                c = 0  # Decimal = decimal + int
                ban = True
                while (ban):
                    if (codigo[c] == ";" and c > posi):
                        posf = c
                        ban = False
                    c += 1
                Aux = codigo[posi:posf]
                V.append(Aux[0])
                if (Aux[0] not in VAR):
                    self.Error_Sema("Identificadores no Declarados.")
                    return
                val = VAR.index(Aux[0])
                T.append(TIPOS[val])
                M = False
                W = False
                for j in range(2, len(Aux)):
                    print("Aux: ", Aux[j])
                    if (Aux[j] in VAR):
                        val = VAR.index(Aux[j])
                        V.append(Aux[j])
                        T.append(TIPOS[val])
                    elif (Aux[j] not in OPERA):
                        ti, Es = self.Num_Check(Aux[j])
                        to, As = self.Cad_Check(T[0], Aux[j])
                        if (Es):
                            V.append(Aux[j])
                            T.append(ti)
                        elif (As):
                            V.append(Aux[j])
                            T.append(to)
                        elif (Es == False and As == False):
                            self.Error_Sema("Identifiadores no Declarados.")
                            return
                    elif (Aux[j] in OPERA):
                        M = True
                        if (Aux[j] != "+"):
                            W = True

                print("V: ", V)
                print("T: ", T)

                KK = False
                K = T[0]
                if (K == "int"):
                    KK = True
                    for j in range(len(T)):
                        if (T[j] != K):
                            self.Error_Sema("Operandos Incompatibles.1")
                            return
                elif (K == "decimal"):
                    KK = True
                    for j in range(len(T)):
                        if (T[j] == "cad" or T[j] == "char"):
                            self.Error_Sema("Operandos Incompatibles.2")
                            return
                elif (K == "cad"):
                    if (W):
                        self.Error_Sema("Operadores Incompatibles.")
                        return
                    else:
                        for j in range(len(T)):
                            if (T[j] != K and T[j]!="char"):
                                self.Error_Sema("Operandos Incompatibles.")
                                return
                elif (K == "char"):
                    if (M):
                        self.Error_Sema("Operandos Incompatibles.4")
                        return
                    else:
                        for j in range(len(T)):
                            if (T[j] != K):
                                self.Error_Sema("Operandos Incompatibles.")
                                return
                if (KK):
                    A = "".join(Aux)
                    Lista_Opera.append(A)



        print(VAR)
        print(TIPOS)
        print(Lista_Opera)

        self.Tabla_Semantica()

        self.images=[]
        for i in range(len(Lista_Opera)):
            b=Ar.principal(Lista_Opera[i],i)
            if b:
                self.img = Image.open("arbol" + str(i) + ".png")
                self.img = self.img.resize((1000, 700), Image.ANTIALIAS)
                self.im = ImageTk.PhotoImage(self.img)
                self.images.append(self.im)
        for i in range(len(self.images)):
            self.top = Toplevel()
            self.canvas = Canvas(self.top, width=1700, height=760)
            self.canvas.pack()
            self.canvasImage = self.canvas.create_image(0, 0, image=self.images[i], anchor="nw")
        self.Btn_CI.config(state="normal")
        self.lista_opera=Lista_Opera

    def Num_Check(self, var):

        try:
            A = float(var)
            valor = str(var).find(".")
            print(valor, var)
            if (valor >= 1):
                return "decimal", True
            else:
                return "int", True
        except:
            return "NO", False

    def Cad_Check(self, T, var):

        if (str(var)[0] == '"' and str(var)[len(var) - 1] == '"' and len(var) == 3):
            return "char", True
        elif (str(var)[0] == '"' and str(var)[len(var) - 1] == '"' and len(var) > 3):
            return "cad", True
        else:
            return "NO", False

    def Error_Sema(self, error):

        texto1.config(state='normal')
        texto1.delete("1.0", "end-1c")
        texto1.insert(END, "Error Semántico: \n")
        texto1.insert(END, "         - " + error)
        # texto1.insert(END, Error+" (Linea " + str(Linea) + ")")
        texto1.config(fg="RED")
        texto1.config(state='disabled')

    def Tabla_Semantica(self):

        ven = Toplevel()
        ven.title("Tabla Semantica")
        ven.geometry("1240x668+50+5")

        Gramatica = [["Programa", "-->", "Begin|Sentencias|End"],
                     ["Sentencias", "-->", "Declaracion"],
                     ["Sentencias", "-->", "Imprimir"],
                     ["Sentencias", "-->", "Declaracion|Sentencias"],
                     ["Sentencias", "-->", "Imprimir|Sentencias"],
                     ["Declaracion", "-->", "tipo_dato|Variable|;"],
                     ["Declaracion", "-->", "Variable|=|ask|cadena|;"],
                     ["Declaracion", "-->", "Variable|=|Exp|;"],
                     ["tipo_dato", "-->", "int"],
                     ["tipo_dato", "-->", "cad"],
                     ["tipo_dato", "-->", "char"],
                     ["tipo_dato", "-->", "decimal"],
                     ["Variable", "-->", "var"],
                     ["Variable", "-->", "var|,|Variable"],
                     ["Exp", "-->", "Variable"],
                     ["Exp", "-->", "Numero"],
                     ["Exp", "-->", "cadena"],
                     ["Exp", "-->", "Operacion"],
                     ["Exp", "-->", "Variable|,|Exp"],
                     ["Exp", "-->", "Numero|,|Exp"],
                     ["Exp", "-->", "cadena|,|Exp"],
                     ["Exp", "-->", "Operacion|,|Exp"],
                     ["Numero", "-->", "num"],
                     ["cadena", "-->", "cade"],
                     ["Operacion", "-->", "Numero|operador|Numero"],
                     ["Operacion", "-->", "Variable|operador|Variable"],
                     ["Operacion", "-->", "Numero|operador|Variable"],
                     ["Operacion", "-->", "Variable|operador|Numero"],
                     ["Operacion", "-->", "Variable|operador|Operacion"],
                     ["Operacion", "-->", "Numero|operador|Operacion"],
                     ["Operacion", "-->", "cadena|operador|cadena"],
                     ["Operacion", "-->", "cadena|operador|Variable"],
                     ["Operacion", "-->", "Variable|operador|cadena"],
                     ["operador", "-->", "+"],
                     ["operador", "-->", "-"],
                     ["operador", "-->", "/"],
                     ["operador", "-->", "*"],
                     ["Imprimir", "-->", "show|Exp|;"]]

        TIPO = [["Programa.tipo", "-->", "Begin.tipo|Sentencias.tipo|End.tipo"],
                ["Sentencias.tipo", "-->", "Declaracion.tipo"],
                ["Sentencias.tipo", "-->", "Imprimir.tipo"],
                ["Sentencias.tipo", "-->", "Declaracion.tipo|Sentencias.tipo"],
                ["Sentencias.tipo", "-->", "Imprimir.tipo|Sentencias.tipo"],
                ["Declaracion.tipo", "-->", "tipo_dato.tipo|Variable.tipo|;.tipo"],
                ["Declaracion.tipo", "-->", "Variable.tipo|=.tipo|ask.tipo|cadena.tipo|;.tipo"],
                ["Declaracion.tipo", "-->", "Variable.tipo|=.tipo|Exp.tipo|;.tipo"],
                ["tipo_dato.tipo", "-->", "int.tipo"],
                ["tipo_dato.tipo", "-->", "cad.tipo"],
                ["tipo_dato.tipo", "-->", "char.tipo"],
                ["tipo_dato.tipo", "-->", "decimal.tipo"],
                ["Variable.tipo", "-->", "var.tipo"],
                ["Variable.tipo", "-->", "var.tipo|,.tipo|Variable.tipo"],
                ["Exp.tipo", "-->", "Variable.tipo"],
                ["Exp.tipo", "-->", "Numero.tipo"],
                ["Exp.tipo", "-->", "cadena.tipo"],
                ["Exp.tipo", "-->", "Operacion.tipo"],
                ["Exp.tipo", "-->", "Variable.tipo|,.tipo|Exp.tipo"],
                ["Exp.tipo", "-->", "Numero.tipo|,.tipo|Exp.tipo"],
                ["Exp.tipo", "-->", "cadena.tipo|,.tipo|Exp.tipo"],
                ["Exp.tipo", "-->", "Operacion.tipo|,.tipo|Exp.tipo"],
                ["Numero.tipo", "-->", "num.tipo"],
                ["cadena.tipo", "-->", "cade.tipo"],
                ["Operacion.tipo", "-->", "Numero.tipo|operador.tipo|Numero.tipo"],
                ["Operacion.tipo", "-->", "Variable.tipo|operador.tipo|Variable.tipo"],
                ["Operacion.tipo", "-->", "Numero.tipo|operador.tipo|Variable.tipo"],
                ["Operacion.tipo", "-->", "Variable.tipo|operador.tipo|Numero.tipo"],
                ["Operacion.tipo", "-->", "Variable.tipo|operador.tipo|Operacion.tipo"],
                ["Operacion.tipo", "-->", "Numero.tipo|operador.tipo|Operacion.tipo"],
                ["Operacion.tipo", "-->", "cadena.tipo|operador.tipo|cadena.tipo"],
                ["Operacion.tipo", "-->", "cadena.tipo|operador.tipo|Variable.tipo"],
                ["Operacion.tipo", "-->", "Variable.tipo|operador.tipo|cadena.tipo"],
                ["operador.tipo", "-->", "+.tipo"],
                ["operador.tipo", "-->", "-.tipo"],
                ["operador.tipo", "-->", "/.tipo"],
                ["operador.tipo", "-->", "*.tipo"],
                ["Imprimir.tipo", "-->", "show.tipo|Exp.tipo|;.tipo"]]

        VALOR = [["Programa.valor", "-->", "Begin.valor|Sentencias.valor|End.valor"],
                 ["Sentencias.valor", "-->", "Declaracion.valor"],
                 ["Sentencias.valor", "-->", "Imprimir.valor"],
                 ["Sentencias.valor", "-->", "Declaracion.valor|Sentencias.valor"],
                 ["Sentencias.valor", "-->", "Imprimir.valor|Sentencias.valor"],
                 ["Declaracion.valor", "-->", "tipo_dato.valor|Variable.valor|;.valor"],
                 ["Declaracion.valor", "-->", "Variable.valor|=.valor|ask.valor|cadena.valor|;.valor"],
                 ["Declaracion.valor", "-->", "Variable.valor|=.valor|Exp.valor|;.valor"],
                 ["tipo_dato.valor", "-->", "int.valor"],
                 ["tipo_dato.valor", "-->", "cad.valor"],
                 ["tipo_dato.valor", "-->", "char.valor"],
                 ["tipo_dato.valor", "-->", "decimal.valor"],
                 ["Variable.valor", "-->", "var.valor"],
                 ["Variable.valor", "-->", "var.valor|,.valor|Variable.valor"],
                 ["Exp.valor", "-->", "Variable.valor"],
                 ["Exp.valor", "-->", "Numero.valor"],
                 ["Exp.valor", "-->", "cadena.valor"],
                 ["Exp.valor", "-->", "Operacion.valor"],
                 ["Exp.valor", "-->", "Variable.valor|,.valor|Exp.valor"],
                 ["Exp.valor", "-->", "Numero.valor|,.valor|Exp.valor"],
                 ["Exp.valor", "-->", "cadena.valor|,.valor|Exp.valor"],
                 ["Exp.valor", "-->", "Operacion.valor|,.valor|Exp.valor"],
                 ["Numero.valor", "-->", "num.valor"],
                 ["cadena.valor", "-->", "cade.valor"],
                 ["Operacion.valor", "-->", "Numero.valor|operador.valor|Numero.valor"],
                 ["Operacion.valor", "-->", "Variable.valor|operador.valor|Variable.valor"],
                 ["Operacion.valor", "-->", "Numero.valor|operador.valor|Variable.valor"],
                 ["Operacion.valor", "-->", "Variable.valor|operador.valor|Numero.valor"],
                 ["Operacion.valor", "-->", "Variable.valor|operador.valor|Operacion.valor"],
                 ["Operacion.valor", "-->", "Numero.valor|operador.valor|Operacion.valor"],
                 ["Operacion.valor", "-->", "cadena.valor|operador.valor|cadena.valor"],
                 ["Operacion.valor", "-->", "cadena.valor|operador.valor|Variable.valor"],
                 ["Operacion.valor", "-->", "Variable.valor|operador.valor|cadena.valor"],
                 ["operador.valor", "-->", "+.valor"],
                 ["operador.valor", "-->", "-.valor"],
                 ["operador.valor", "-->", "/.valor"],
                 ["operador.valor", "-->", "*.valor"],
                 ["Imprimir.valor", "-->", "show.valor|Exp.valor|;.valor"]]

        SBFRAME2 = Frame(ven)
        SB = Scrollbar(SBFRAME2, relief=RAISED)
        SB.pack(side=RIGHT, fill=Y)
        Table = ttk.Treeview(SBFRAME2, columns=("T", "V"), height=31, selectmode=BROWSE, yscrollcommand=SB.set)
        Table.pack(side=LEFT, fill=BOTH)
        Table.heading("#0", text="Gramática")
        Table.column("#0", minwidth=400, width=400, anchor=W)
        Table.heading("T", text="TIPO")
        Table.column("T", minwidth=400, width=400, anchor=W)
        Table.heading("V", text="VALOR")
        Table.column("V", minwidth=400, width=400, anchor=W)
        SB.config(command=Table.yview)
        SBFRAME2.place(x=10, y=10)

        for i in range(len(Gramatica)):
            Table.insert("", END, text=Gramatica[i][0:3], values=(TIPO[i][0:3], VALOR[i][0:3]))

        return

    def Codigo_Intermedio(self):
        self.Btn_CI.config(state="disabled")
        veninter=Toplevel()
        veninter.title("Código intermedio")
        NotP=Button(veninter,text="Notación polaca",font=("Arial","20"), command=lambda:self.polaca())
        NotP.pack()
        CodP=Button(veninter, text="Código-P",font=("Arial","20"), command=lambda:self.codigoP())
        CodP.pack()
        Tri=Button(veninter, text="Triplos",font=("Arial","20"), command=lambda:self.triplos())
        Tri.pack()
        Cuat=Button(veninter, text="Cuadruplos",font=("Arial","20"), command=lambda:self.cuadruplos())
        Cuat.pack()
        self.Btn_Optimizacion.config(state='normal')

    def polaca(self):
        for i in self.lista_opera:
            Inter.notacion_P(i, ventana)

    def codigoP(self):
        for i in self.lista_opera:
            Inter.codigoP(i, ventana)

    def triplos(self):
        Inter2.Inicia(self.lista_opera,"Triplos")

    def cuadruplos(self):
        Inter2.Inicia(self.lista_opera,"Cuadruplos")

    def Optimizacion(self):
        self.Btn_Optimizacion.config(state="disabled")
        ven_op=Toplevel()
        ven_op.title("Optimizaciones")
        self.btn_precalculo=Button(ven_op,text="Precalculo de expresiones constantes",
                                   command=lambda:self.precalculo(self.codigo_s))
        self.btn_precalculo.pack()
        self.btn_nulas = Button(ven_op, text="Eliminación de secuencias nulas",
                                     command=lambda: self.nulas(self.codigo_s))
        self.btn_nulas.pack()
        self.btn_red = Button(ven_op, text="Reducción de potencias",
                                command=lambda: self.reduccion())
        self.btn_red.pack()
        self.btn_cop = Button(ven_op, text="Propagación de copias",
                              command=lambda: self.copias())
        self.btn_cop.pack()

    def precalculo(self,codigo):
        self.btn_nulas.config(state="normal")
        self.btn_precalculo.config(state="disabled")
        cod_res = codigo.copy()
        op1 = ["*", "/"]
        op2 = ["+", "-"]
        vars = []
        vals = []
        lineas = []
        cols = []
        ban = False
        ban2 = True
        exp = []
        idx = 0
        idx_m = []
        c1 = 0
        while ban2:
            linea = 1
            col = 0
            c2 = 0
            codigo = cod_res.copy()
            for i in range(1, len(codigo)):
                if codigo[i] == "=":
                    print(codigo[i + 2])
                    if codigo[i - 1] not in vars:
                        vars.append(codigo[i - 1])
                        if codigo[i + 2] == ";":
                            if self.checknum2(codigo[i + 1]):
                                vals.append(codigo[i + 1])
                            else:
                                vals.append('')
                        else:
                            vals.append('')
                    else:
                        if codigo[i + 2] == ";":
                            if self.checknum2(codigo[i + 1]):
                                vals[vars.index(codigo[i - 1])] = codigo[i + 1]
            print(vars)
            print(vals)
            print("\n")
            for i in range(len(codigo)):
                col += 1
                if codigo[i] == "=":
                    ban = True
                elif codigo[i] == ";":
                    linea += 1
                    col = 0
                    ban = False
                    c1 = 0
                    exp = []
                elif ban:
                    if i not in idx_m:
                        exp.append(codigo[i])
                        idx_m.append(i)
                        c1 += 1
                    if c1 == 1:
                        if c2 > 0:
                            idx = i - 2 * c2
                        else:
                            idx = i
                    if c1 == 3:
                        c1 = 0
                        if exp[1] in op1 and self.checknum2(exp[0]) and self.checknum2(exp[2]):
                            if exp[1] == "*":
                                res = float(exp[0]) * float(exp[2])
                                # print(res)
                            else:
                                res = float(exp[0]) / float(exp[2])
                                # print(res)
                            for i in range(3):
                                cod_res.pop(idx)
                            cod_res.insert(idx, res)
                            idx_m = []
                            c2 += 1
                        elif exp[1] in op1 and self.checknum2(exp[0]) == False and self.checknum2(exp[2]) == False:
                            if self.checknum2(vals[vars.index(exp[0])]) and self.checknum2(vals[vars.index(exp[2])]):
                                if exp[1] == "*":
                                    res = float(vals[vars.index(exp[0])]) * float(vals[vars.index(exp[2])])
                                    # print(res)
                                else:
                                    res = float(vals[vars.index(exp[0])]) / float(vals[vars.index(exp[2])])
                                    # print(res)
                                for i in range(3):
                                    cod_res.pop(idx)
                                cod_res.insert(idx, res)
                                idx_m = []
                                c2 += 1
                        elif exp[1] in op1 and self.checknum2(exp[0]) == False:
                            if exp[0] in vars:
                                if self.checknum2(vals[vars.index(exp[0])]):
                                    if exp[1] == "*":
                                        res = float(vals[vars.index(exp[0])]) * float(exp[2])
                                        # print(res)
                                    else:
                                        res = float(vals[vars.index(exp[0])]) / float(exp[2])
                                        # print(res)
                                    for i in range(3):
                                        cod_res.pop(idx)
                                    cod_res.insert(idx, res)
                                    idx_m = []
                                    c2 += 1
                            else:
                                if linea not in lineas:
                                    lineas.append(linea)
                                    cols.append(col)
                                else:
                                    cols[lineas.index(linea)] = col
                                idx_m.pop()
                        elif exp[1] in op1 and self.checknum2(exp[2]) == False:
                            if exp[2] in vars:
                                if self.checknum2(vals[vars.index(exp[2])]):
                                    if exp[1] == "*":
                                        res = float(exp[0]) * float(vals[vars.index(exp[2])])
                                        # print(res)
                                    else:
                                        res = float(exp[0]) / float(vals[vars.index(exp[2])])
                                        # print(res)
                                    for i in range(3):
                                        cod_res.pop(idx)
                                    cod_res.insert(idx, res)
                                    idx_m = []
                                    c2 += 1
                            else:
                                if linea not in lineas:
                                    lineas.append(linea)
                                    cols.append(col)
                                else:
                                    cols[lineas.index(linea)] = col
                                idx_m.pop()
                        elif exp[1] in op1:
                            if linea not in lineas:
                                lineas.append(linea)
                                cols.append(col)
                            else:
                                cols[lineas.index(linea)] = col
                            idx_m.pop()
                        elif exp[1] in op2:
                            c2 += 1
                            idx_m.pop()
                        else:
                            idx_m.pop()
                        exp = []
                        ban = False
            if c2 == 0:
                ban2 = False
        print(cod_res)
        print(idx_m)
        print("\n")

        exp = []
        ban2 = True
        ban = False
        idx_m = []
        c1 = 0
        while ban2:
            linea = 1
            col = 0
            c2 = 0
            codigo = cod_res.copy()
            for i in range(1, len(codigo)):
                if codigo[i] == "=":
                    print(codigo[i + 2])
                    if codigo[i - 1] not in vars:
                        vars.append(codigo[i - 1])
                        if codigo[i + 2] == ";":
                            if self.checknum2(codigo[i + 1]):
                                vals.append(codigo[i + 1])
                            else:
                                vals.append('')
                        else:
                            vals.append('')
                    else:
                        if codigo[i + 2] == ";":
                            if self.checknum2(codigo[i + 1]):
                                vals[vars.index(codigo[i - 1])] = codigo[i + 1]
            print(vars)
            print(vals)
            print("\n")
            for i in range(len(codigo)):
                col += 1
                if codigo[i] == "=":
                    ban = True
                elif codigo[i] == ";":
                    linea += 1
                    col = 0
                    ban = False
                    c1 = 0
                    exp = []
                elif ban:
                    if i not in idx_m:
                        exp.append(codigo[i])
                        idx_m.append(i)
                        c1 += 1
                    if c1 == 1:
                        if c2 > 0:
                            idx = i - 2 * c2
                        else:
                            idx = i
                    if c1 == 3:
                        print(exp)
                        c1 = 0
                        if exp[1] in op2 and self.checknum2(exp[0]) and self.checknum2(exp[2]):
                            if linea in lineas:
                                idx_m.pop()
                            else:
                                if exp[1] == "+":
                                    res = float(exp[0]) + float(exp[2])
                                    # print(res)
                                else:
                                    res = float(exp[0]) - float(exp[2])
                                    # print(res)
                                for i in range(3):
                                    cod_res.pop(idx)
                                cod_res.insert(idx, res)
                                idx_m = []
                            c2 += 1
                        elif exp[1] in op2 and self.checknum2(exp[0]) == False and self.checknum2(exp[2]) == False:
                            if linea in lineas:
                                idx_m.pop()
                            else:
                                if exp[0] in vars and exp[2] in vars:
                                    if self.checknum2(vals[vars.index(exp[0])]) and self.checknum2(
                                            vals[vars.index(exp[2])]):
                                        if exp[1] == "+":
                                            res = float(vals[vars.index(exp[0])]) + float(vals[vars.index(exp[2])])
                                            # print(res)
                                        else:
                                            res = float(vals[vars.index(exp[0])]) - float(vals[vars.index(exp[2])])
                                            # print(res)
                                        for i in range(3):
                                            cod_res.pop(idx)
                                        cod_res.insert(idx, res)
                                        idx_m = []
                                else:
                                    idx_m.pop()
                            c2 += 1
                        elif exp[1] in op2 and self.checknum2(exp[0]) == False:
                            if linea in lineas:
                                idx_m.pop()
                            else:
                                if exp[0] in vars:
                                    if self.checknum2(vals[vars.index(exp[0])]):
                                        if exp[1] == "+":
                                            res = float(vals[vars.index(exp[0])]) + float(exp[2])
                                            # print(res)
                                        else:
                                            res = float(vals[vars.index(exp[0])]) - float(exp[2])
                                            # print(res)
                                        for i in range(3):
                                            cod_res.pop(idx)
                                        cod_res.insert(idx, res)
                                        idx_m = []
                                else:
                                    idx_m.pop()
                            c2 += 1
                        elif exp[1] in op2 and self.checknum2(exp[2]) == False:
                            if linea in lineas:
                                idx_m.pop()
                            else:
                                if exp[2] in vars:
                                    if self.checknum2(vals[vars.index(exp[2])]):
                                        if exp[1] == "+":
                                            res = float(exp[0]) + float(vals[vars.index(exp[2])])
                                            # print(res)
                                        else:
                                            res = float(exp[0]) - float(vals[vars.index(exp[2])])
                                            # print(res)
                                        for i in range(3):
                                            cod_res.pop(idx)
                                        cod_res.insert(idx, res)
                                        idx_m = []
                                else:
                                    idx_m.pop()
                            c2 += 1
                        else:
                            idx_m.pop()
                        exp = []
                        ban = False
            if c2 == 0:
                ban2 = False
        print(cod_res)


        self.cod_pre=cod_res.copy()
        ven_pre = Toplevel()
        ven_pre.title("Precalculo de expresiones constantes")
        txt_pre=Text(ven_pre,height=27, width=38,font=('Times New Roman','14'),wrap=WORD)
        txt_pre.pack()
        for i in cod_res:
            txt_pre.insert(END,str(i)+" ")
            if i=="Begin" or i==";":
                txt_pre.insert(END,"\n")

    def nulas(self,codigo):
        self.btn_nulas.config(state="disabled")
        self.btn_red.config(state="normal")
        op1=["*","/"]
        cod_res = codigo.copy()
        c1=0
        idx=0
        for i in range(len(codigo)):
            if codigo[i] in op1:
                if c1 > 0:
                    idx = i - (2 * c1)
                else:
                    idx = i
                if codigo[i]=="*":
                    if codigo[i+1]=="1":
                        cod_res.pop(idx+1)
                        cod_res.pop(idx)
                        c1+=1
                    elif codigo[i-1]=="1":
                        cod_res.pop(idx-1)
                        cod_res.pop(idx-1)
                        c1+=1
                elif codigo[i]=="/":
                    if codigo[i+1]=="1":
                        cod_res.pop(idx+1)
                        cod_res.pop(idx)
                        c1+=1
        print(cod_res)


        self.cod_nul=cod_res.copy()
        ven_nul = Toplevel()
        ven_nul.title("Eliminación de secuencias nulas")
        txt_nul = Text(ven_nul, height=27, width=38, font=('Times New Roman', '14'), wrap=WORD)
        txt_nul.pack()
        for i in cod_res:
            txt_nul.insert(END, str(i) + " ")
            if i == "Begin" or i == ";":
                txt_nul.insert(END, "\n")

    def reduccion(self):
        self.btn_red.config(state="disabled")
        self.btn_cop.config(state="normal")
        self.cod_red=op2.Reduccion_de_Potencias(self.codigo_s)
        ven_red = Toplevel()
        ven_red.title("Reducción de potencias")
        txt_red = Text(ven_red, height=27, width=38, font=('Times New Roman', '14'), wrap=WORD)
        txt_red.pack()
        for i in self.cod_red:
            txt_red.insert(END, str(i) + " ")
            if i == "Begin" or str(i) == ";":
                txt_red.insert(END, "\n")

    def copias(self):
        self.btn_cop.config(state="disabled")
        self.btn_precalculo.config(state="normal")
        self.cod_cop = op2.Eliminacion_de_Copeas(self.codigo_s)
        self.codigo_s=[]
        ven_cop = Toplevel()
        ven_cop.title("Propagación de copias")
        txt_cop = Text(ven_cop, height=27, width=38, font=('Times New Roman', '14'), wrap=WORD)
        txt_cop.pack()
        for i in range(len(self.cod_cop)):
            for j in range(len(self.cod_cop[i])):
                txt_cop.insert(END, str(self.cod_cop[i][j]))
                self.codigo_s.append(str(self.cod_cop[i][j]))
            txt_cop.insert(END, "\n")

    def Codigo_Objeto(self):

        self.Btn_Limpiar.config(state='normal')
        self.Btn_CO.config(state="disabled")

    def Limpiar(self,T1,T2,E1):

        self.Table.delete(*self.Table.get_children())

        self.Btn_Cargar.config(state='normal')
        #self.Btn_Examinar.config(state="disabled")
        self.Btn_Examinar.config(state="normal")
        self.Btn_Lexico.config(bg="black",fg="white",state='disabled')
        self.Btn_Sintatico.config(state="disabled")
        self.Btn_Semantico.config(state="disabled")
        self.Btn_CI.config(state="disabled")
        self.Btn_Optimizacion.config(state="disabled")
        self.Btn_CO.config(state="disabled")

        E1.config(state='normal')
        E1.delete(0,END)
        E1.config(state='disabled')

        #T1.config(state='normal')
        T2.config(state='normal')
        T1.delete("1.0", "end-1c")
        T2.delete("1.0", "end-1c")
        #T1.config(state='disabled')
        T2.config(state='disabled')

P = Principal()
P.Ventana()
