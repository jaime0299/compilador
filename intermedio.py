from tkinter import *

class Intermedio():
    def notacion_P(self, operacion, ventana):
        global top
        self.x=20
        self.y=100
        self.y_base=200
        oper1 = ["*", "/"]
        oper2 = ["+", "-"]
        operadores = ["+", "-", "*", "/"]

        opes = operacion.split("=")
        opera = opes[1]
        con_magico=0
        pilaOperadores = []
        pilaOperandos = []
        pilaOperadores.append("=")
        pilaOperandos.append(opes[0])
        exp = ""
        salida = ""
        opera_list=[]
        ope_max=0
        for i in opera:
            if i in operadores:
                if i in oper1:
                    ope_max+=1
                opera_list.append(exp)
                opera_list.append(i)
                exp=""
            else:
                exp+=i
        if exp!="":
            opera_list.append(exp)
            exp=""
        print(opera_list)
        top = Toplevel(ventana)
        top.geometry("1678x768+0+0")
        top.title("Notación Polaca")

        Label(top, text="Operación: "+operacion, font=("Arial","18")).place(x=10,y=700)
        for i in opera_list:
            if i not in operadores:
                pilaOperandos.append(i)
                con_magico+=1
            else:
                if i in oper1:
                    ope_max-=1
                if len(pilaOperadores)>0:
                    if (pilaOperadores[len(pilaOperadores) - 1] in oper1 and i in oper2) or (pilaOperadores[len(pilaOperadores) - 1] in oper1 and i in oper1) or (pilaOperadores[len(pilaOperadores) - 1] in oper2 and i in oper2):
                        for x in range(len(pilaOperadores)-1):
                            if pilaOperadores[len(pilaOperadores)-1] in oper1 or ope_max>=2:
                                if con_magico > 1:
                                    print(pilaOperandos)
                                    print(pilaOperadores)
                                    self.agrega_pilas(pilaOperadores, pilaOperandos)
                                    salida += pilaOperandos[len(pilaOperandos) - 1]
                                    pilaOperandos.pop()
                                    salida += pilaOperandos[len(pilaOperandos) - 1]
                                    pilaOperandos.pop()
                                    salida += pilaOperadores[len(pilaOperadores) - 1]
                                    pilaOperadores.pop()
                                    print(salida)
                                    self.agregasalida(salida)
                                    print("\n")
                                else:
                                    print(pilaOperandos)
                                    print(pilaOperadores)
                                    self.agrega_pilas(pilaOperadores, pilaOperandos)
                                    if len(pilaOperandos) > 1:
                                        salida += pilaOperandos[len(pilaOperandos) - 1]
                                        pilaOperandos.pop()
                                    salida += pilaOperadores[len(pilaOperadores) - 1]
                                    pilaOperadores.pop()
                                    print(salida)
                                    self.agregasalida(salida)
                                    print("\n")
                                con_magico = 0
                        pilaOperadores.append(i)
                    else:
                        pilaOperadores.append(i)
                else:
                    pilaOperadores.append(i)


        if len(pilaOperadores)>1:
            for i in range(len(pilaOperadores)):
                if con_magico>1:
                    print(pilaOperandos)
                    print(pilaOperadores)
                    self.agrega_pilas(pilaOperadores,pilaOperandos)
                    salida += pilaOperandos[len(pilaOperandos) - 1]
                    pilaOperandos.pop()
                    salida += pilaOperandos[len(pilaOperandos) - 1]
                    pilaOperandos.pop()
                    salida += pilaOperadores[len(pilaOperadores) - 1]
                    pilaOperadores.pop()
                    print(salida)
                    self.agregasalida(salida)
                    print("\n")
                else:
                    print(pilaOperandos)
                    print(pilaOperadores)
                    if pilaOperandos[len(pilaOperandos) - 1]!=opes[0] or pilaOperadores[len(pilaOperadores) - 1]=="=":
                        print(pilaOperandos)
                        print(pilaOperadores)
                        self.agrega_pilas(pilaOperadores,pilaOperandos)
                        if len(pilaOperandos)>0:
                            salida += pilaOperandos[len(pilaOperandos) - 1]
                            pilaOperandos.pop()
                        salida += pilaOperadores[len(pilaOperadores) - 1]
                        pilaOperadores.pop()
                        print(salida)
                        self.agregasalida(salida)
                        print("\n")
                    else:
                        print(pilaOperandos)
                        print(pilaOperadores)
                        self.agrega_pilas(pilaOperadores,pilaOperandos)
                        salida += pilaOperadores[len(pilaOperadores) - 1]
                        pilaOperadores.pop()
                        print(salida)
                        self.agregasalida(salida)
                        print("\n")
                con_magico = 0

    def agrega_pilas(self,pila1,pila2):
        self.y = self.y_base
        for i in range(len(pila2)):
            E=Entry(top,font=("Times New Roman",'14','bold'),
                                width=3,justify='center')
            E.place(x=self.x,y=self.y)
            E.insert(END,str(pila2[i]))
            self.y-=40
        self.x+=50
        self.y = self.y_base
        for i in range(len(pila1)):
            E = Entry(top, font=("Times New Roman", '14', 'bold'),
                      width=3, justify='center')
            E.place(x=self.x, y=self.y)
            E.insert(END, str(pila1[i]))
            self.y -= 40
        self.x+=30
        self.y = self.y_base


    def agregasalida(self,salida):
        self.y=self.y_base/2
        Label(top,text=salida, font=(("Times New Roman", '14', 'bold'))).place(x=self.x,y=self.y)
        self.x+=(len(salida)*12)
        if self.x>=1600:
            self.y_base+=200
            self.x=20

    def check(self,num):
        try:
            int(num)
            return True
        except:
            return False

    def codigoP(self,operacion,ventana):
        top=Toplevel(ventana)
        top.title("Código-P")

        txt=Text(top,height=30, width=40,font=('Times New Roman','16'))
        txt.pack()

        operadores = ["+", "-", "*", "/"]
        ope_p=["adi","sbi","mpi","div"]
        opes = operacion.split("=")
        opera = opes[1]
        exp = ""
        opera_list = []
        for i in opera:
            if i in operadores:
                opera_list.append(exp)
                opera_list.append(i)
                exp = ""
            else:
                exp += i
        if exp != "":
            opera_list.append(exp)
            exp = ""
        print(opera_list)
        print("------------Codigo P---------------")
        print("lda "+opes[0])
        txt.insert(END, "Operación: "+operacion+"\n")
        txt.insert(END,"-----------------Código P--------------------\n")
        txt.insert(END,"lda "+opes[0]+"\n")
        idx=""
        for i in opera_list:
            if i in operadores:
                idx=ope_p[operadores.index(i)]
            else:
                print("lcd "+i)
                if self.check(i):
                    txt.insert(END, "ldc " + i + "\n")
                else:
                    txt.insert(END, "lod " + i + "\n")
                if idx!="":
                    print(idx)
                    txt.insert(END,idx+"\n")
                    idx=""
        print("sto")
        txt.insert(END, "sto" + "\n")

"""
root=Tk()
I = Intermedio()
I.notacion_P("y=a+b*5-30*4/5",root)
#I.codigoP("x=12*33+b*5-40",root)
I.codigoP("y=a+b*5-30*4/5",root)
I.codigoP("z=a*b*c/d",root)
root.mainloop()"""
