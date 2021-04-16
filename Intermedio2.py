from tkinter import *
import tkinter.ttk as ttk

class Tablas():

    def Inicia(self, Lista_Pricipal, metodo):
        self.Lista1 = self.Separaracion(Lista_Pricipal) 
        self.Lista2 = self.Separaracion(Lista_Pricipal) 
        
        #Triplos
        self.A = []
        self.B = []
        self.C = []
        self.D = []
        #Cuadrúplos
        self.E = []
        self.F = []
        self.G = []
        self.H = []

        if metodo=="Triplos":
            for i in range(len(self.Lista1)):
                self.Triplos(i)

            self.Creacion_Tablas_Triplos()
        else:
            for i in range(len(self.Lista2)):
                self.Cuadruplos(i)

            self.Creacion_Tablas_Cuadruplos()
        
        # #Lista Opera:  ['suma=58+20-84*2+246/2', 'suma=45+2-58/2']      


    def Separaracion(self,Lista):

        Operadores = ["+","-","*","/","="]

        L = []
        I = 0

        #print ("Lista: ",Lista)
        for i in range(len(Lista)):
            Aux = []
            I = 0
            for j in range(len(Lista[i])):
                if (str(Lista[i][j]) in Operadores):
                    A1 = Lista[i][I:j]
                    I = j+1
                    Aux.append(A1)
                    Aux.append(Lista[i][j])
                elif (j == len(Lista[i])-1):                    
                    A2 = Lista[i][I:len(Lista[i])]
                    Aux.append(A2)
            L.append(Aux)
        #print ("L: ",L) 
        return L           

    def Triplos(self,contador):

        Lista = self.Lista1
        
        Menores = ["+","-"]
        Mayores = ["*","/"]

        D = []
        O = []
        Op1 = []
        Op2 = []
        N = 0

        Ban = True  
        Con = contador      
        while (Ban):#(Con < 1):
            #print ("1. ",Lista[Con])
            A = []
            for i in range(len(Lista[Con])):
                #print (i)
                if(Lista[Con][i] in Mayores):
                    for j in range(0,i-1):
                        A.append(Lista[Con][j])
                    #print ("A: ",A)
                    A.append("["+str(N)+"]")
                    for j in range(i+2,len(Lista[Con])):
                        A.append(Lista[Con][j])
                    #print ("B: ",A)
                    D.append("["+str(N)+"]")
                    O.append(Lista[Con][i])
                    Op1.append(str(Lista[Con][i-1]))
                    Op2.append(str(Lista[Con][i+1]))
                    Lista[Con].pop(i-1)
                    Lista[Con].pop(i)
                    Lista[Con].pop(i-1) 
                    N += 1             
                    break
            #print ("2. ",A)
            #print (len(Lista[Con]))            
            if (len(A) == 0):
                Ban = False                
            else:
                Lista[Con] = []
                Lista[Con] = A  

        #print ("--------------------------")
        Ban = True  
        Con = contador      
        while (Ban):#(Con < 1):
            #print ("3. ",Lista[Con])
            A = []
            for i in range(len(Lista[Con])):
                #print (i)
                if(Lista[Con][i] in Menores):                    
                    for j in range(0,i-1):
                        A.append(Lista[Con][j])
                    #print ("A: ",A)
                    A.append("["+str(N)+"]")
                    for j in range(i+2,len(Lista[Con])):
                        A.append(Lista[Con][j])
                    #print ("B: ",A)
                    D.append("["+str(N)+"]")
                    O.append(Lista[Con][i])
                    Op1.append(str(Lista[Con][i-1]))
                    Op2.append(str(Lista[Con][i+1]))
                    Lista[Con].pop(i-1)
                    Lista[Con].pop(i)
                    Lista[Con].pop(i-1)
                    N += 1              
                    break
            #print ("4. ",A)
            #print (len(Lista[Con]))
            if (len(A) == 0):
                Ban = False
            else:
                Lista[Con] = []
                Lista[Con] = A
        
        D.append("["+str(N)+"]")
        O.append(Lista[Con][1])
        Op1.append(Lista[Con][0])
        Op2.append("["+str(N-1)+"]")
        #print ("Direccion: ",D)
        #print ("Operador: ",O)
        #print ("Operando1: ",Op1)
        #print ("Operando2: ",Op2)

        self.A.append(D)
        self.B.append(O)
        self.C.append(Op1)
        self.D.append(Op2)

    def Creacion_Tablas_Triplos(self):

        ventana = Toplevel()
        ventana.geometry("1180x705+85+0")
        ventana.title("Triplos")
        ventana.config(bg="black")

        x1 = 10
        y = 10
        Largo = 65
        for i in range(len(self.Lista1)):        
            SBFRAME1 = Frame(ventana)
            SB1 = Scrollbar(SBFRAME1, relief=RAISED)
            SB1.pack(side=RIGHT, fill=Y)
            Table1 = ttk.Treeview(SBFRAME1, columns=("O", "R1","R2"), height=5, selectmode=BROWSE, yscrollcommand=SB1.set)
            Table1.pack(side=LEFT, fill=BOTH)
            Table1.heading("#0", text="DIR")
            Table1.column("#0", minwidth=Largo, width=Largo, anchor=W)
            Table1.heading("O", text="ODOR")
            Table1.column("O", minwidth=Largo, width=Largo, anchor=W)
            Table1.heading("R1", text="ORANDO1")
            Table1.column("R1", minwidth=Largo, width=Largo, anchor=W)
            Table1.heading("R2", text="ORANDO2")
            Table1.column("R2", minwidth=Largo, width=Largo, anchor=W)
            SB1.config(command=Table1.yview)
            SBFRAME1.place(x=x1, y=y)

            for j in range(len(self.A[i])):
                Table1.insert("",END,text=str(self.A[i][j]),values=(str(self.B[i][j]),str(self.C[i][j]),str(self.D[i][j])))

            y += 140
            if (i == 4 or i == 9 or i == 14 or i == 19):
                y = 10
                x1 += 290

    def Cuadruplos(self,contador):
        Lista = self.Lista2
        
        Menores = ["+","-"]
        Mayores = ["*","/"]

        D = []
        O = []
        Op1 = []
        Op2 = []
        N = 0

        Ban = True  
        Con = contador      
        while (Ban):#(Con < 1):
            #print ("1. ",Lista[Con])
            A = []
            for i in range(len(Lista[Con])):
                #print (i)
                if(Lista[Con][i] in Mayores):
                    N += 1
                    for j in range(0,i-1):
                        A.append(Lista[Con][j])
                    #print ("A: ",A)
                    A.append("V"+str(N))
                    for j in range(i+2,len(Lista[Con])):
                        A.append(Lista[Con][j])
                    #print ("B: ",A)
                    D.append("V"+str(N))
                    O.append(Lista[Con][i])
                    Op1.append(str(Lista[Con][i-1]))
                    Op2.append(str(Lista[Con][i+1]))
                    Lista[Con].pop(i-1)
                    Lista[Con].pop(i)
                    Lista[Con].pop(i-1)                                 
                    break
            #print ("2. ",A)
            #print (len(Lista[Con]))            
            if (len(A) == 0):
                Ban = False                
            else:
                Lista[Con] = []
                Lista[Con] = A  

        #print ("--------------------------")
        
        Ban = True  
        Con = contador      
        while (Ban):#(Con < 1):
            #print ("3. ",Lista[Con])
            A = []
            for i in range(len(Lista[Con])):
                #print (i)
                if(Lista[Con][i] in Menores): 
                    N += 1                   
                    for j in range(0,i-1):
                        A.append(Lista[Con][j])
                    #print ("A: ",A)
                    A.append("V"+str(N))
                    for j in range(i+2,len(Lista[Con])):
                        A.append(Lista[Con][j])
                    #print ("B: ",A)
                    D.append("V"+str(N))
                    O.append(Lista[Con][i])
                    Op1.append(str(Lista[Con][i-1]))
                    Op2.append(str(Lista[Con][i+1]))
                    Lista[Con].pop(i-1)
                    Lista[Con].pop(i)
                    Lista[Con].pop(i-1)                                  
                    break
            #print ("4. ",A)
            #print (len(Lista[Con]))
            if (len(A) == 0):
                Ban = False
            else:
                Lista[Con] = []
                Lista[Con] = A
        
        D.append(Lista[Con][0])
        O.append(Lista[Con][1])
        Op1.append("V"+str(N))
        Op2.append("----------")        
        #print ("Operador: ",O)
        #print ("Operando1: ",Op1)
        #print ("Operando2: ",Op2)
        #print ("Auxiliar: ",D)
        
        self.E.append(O)
        self.F.append(Op1)
        self.G.append(Op2)
        self.H.append(D)

    def Creacion_Tablas_Cuadruplos(self):

        ventana = Toplevel()
        ventana.geometry("1180x705+85+0")
        ventana.title("Cuadruplos")
        ventana.config(bg="black")

        x1 = 10
        y = 10
        Largo = 65
        for i in range(len(self.Lista2)):        
            SBFRAME1 = Frame(ventana)
            SB1 = Scrollbar(SBFRAME1, relief=RAISED)
            SB1.pack(side=RIGHT, fill=Y)
            Table1 = ttk.Treeview(SBFRAME1, columns=("R1","R2","A"), height=5, selectmode=BROWSE, yscrollcommand=SB1.set)
            Table1.pack(side=LEFT, fill=BOTH)
            Table1.heading("#0", text="OPOR")
            Table1.column("#0", minwidth=Largo, width=Largo, anchor=W)
            Table1.heading("R1", text="ORANDO1")
            Table1.column("R1", minwidth=Largo, width=Largo, anchor=W)
            Table1.heading("R2", text="ORANDO2")
            Table1.column("R2", minwidth=Largo, width=Largo, anchor=W)
            Table1.heading("A", text="AUX")
            Table1.column("A", minwidth=Largo, width=Largo, anchor=W)
            SB1.config(command=Table1.yview)
            SBFRAME1.place(x=x1, y=y)

            for j in range(len(self.E[i])):
                Table1.insert("",END,text=str(self.E[i][j]),values=(str(self.F[i][j]),str(self.G[i][j]),str(self.H[i][j])))

            y += 140
            if (i == 4 or i == 9 or i == 14 or i == 19):
                y = 10
                x1 += 290


#Lista = ['OP1=58+20-84*2+246/2', 'OP2=45+2-58/2','Y=78+35-8*2+4/2','X=78+35-8/2','Z=27*2/4+5']
#T=Tablas()
#T.Inicia(Lista)