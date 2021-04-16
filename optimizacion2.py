class Optimizacion:

    def Inicio(self):
        
        codi=[
            'Begin', 
            'int','a',',','b',',','c',';', 
            'a','=','b','*','3',';',
            'c','=','b',';',
            'a','=','c','+','4','/','3',';',
            'End'
            ]

        self.Reduccion_de_Potencias(codi)

    def Reduccion_de_Potencias(self, Codigo):
        
        ALL_CODE = []
        Inicio = 1
        Fin = 0
        Con = 0
        Op = ""
        for i in Codigo:
            A = []
            if (i == 'Begin' or i == 'End'):
                A.append(i)
                ALL_CODE.append(A)    
            if (i == ';'):        
                Fin = Con + 1;        
            if (Inicio != 0 and Fin != 0):
                Op = Codigo[Inicio:Fin]
                ALL_CODE.append(Op)
                Inicio = Fin
                Fin = 0        
            Con += 1

        print ("-----------------------------------------------")
        print ("Codigo Entrada")
        print ("-----------------------------------------------")

        for i in range(len(ALL_CODE)):
            for j in range(len(ALL_CODE[i])):
                print (ALL_CODE[i][j], end=" ")
            print ("\n")
    
        Lista_Operacion = []
        Lista_Posiciones = []

        con = 0
        for i in ALL_CODE:
            if ("=" in i and len(i) > 4):
                Lista_Operacion.append(i)
                Lista_Posiciones.append(con)
            con += 1

        L_O = []
        Opreaciones = ['+','-','*','/']

        for i in range(len(Lista_Operacion)):
            Contador = 0
            for j in range(len(Lista_Operacion[i])):
                if (Lista_Operacion[i][j] in Opreaciones):
                    Contador += 1
                if (j == len(Lista_Operacion[i]) - 1 and Contador < 2):
                    L_O.append(Lista_Operacion[i])
            if (Contador >= 2):
                Lista_Posiciones.pop(int(i))

        M = []
        P = '*'
        for i in range(len(L_O)):
            for j in range(len(L_O[i])):
                A1 = []
                if (L_O[i][j] in Opreaciones):
                    Contador += 1
                if (L_O[i][j] == P and L_O[i][j-2] != P):
                    A1.append(L_O[i][j-1])
                    A1.append(L_O[i][j])
                    A1.append(L_O[i][j+1])
                    M.append(A1)

        List = []
        for i in range(len(M)):
            Contador = 0
            for j in range(len(M[i])):
                try:
                    if (j != 1):
                        float(M[i][j])
                        Contador += 1
                except:
                    List.append(M[i])
            if (Contador >= 2):
                Lista_Posiciones.pop(int(i))

        L = []
        for i in List:
            A = []
            try:
                X = int(i[0])
                for j in range(X):
                    if (j < X - 1):
                        A.append(i[2])
                        A.append('+')
                    else:
                        A.append(i[2])
            except:
                X = int(i[2])
                for j in range(X):
                    if (j < X - 1):
                        A.append(i[0])
                        A.append('+')
                    else:
                        A.append(i[0])
            L.append(A)

        c = 0
        Reduccion = []
        Final = Lista_Posiciones[len(Lista_Posiciones)-1] + 1
        while (c < len(Lista_Posiciones)):
            for i in range(len(ALL_CODE)):
                if (c == 0 and i != Lista_Posiciones[c]):
                    Reduccion.append(ALL_CODE[i])
                else:
                    A = []
                    A.append(ALL_CODE[int(Lista_Posiciones[c])][0])
                    A.append(ALL_CODE[int(Lista_Posiciones[c])][1])
                    for j in range(len(L[c])):

                        A.append(L[c][j])
                    A.append(ALL_CODE[int(Lista_Posiciones[c])][len(ALL_CODE[int(Lista_Posiciones[c])]) - 1])
                    Reduccion.append(A)
                    break            
            c += 1

        for i in range(Final,len(ALL_CODE)):
            Reduccion.append(ALL_CODE[i])

        """
        print ("-----------------------------------------------")
        print ("Codigo Salida Optimizado")
        print ("-----------------------------------------------")
        for i in range(len(Reduccion)):
            for j in range(len(Reduccion[i])):
                print (Reduccion[i][j], end=" ")
            print ("\n")
        """

        Final_Lista = []
        for i in range(len(Reduccion)):
            for j in range(len(Reduccion[i])):
                Final_Lista.append(Reduccion[i][j])
        
        return Final_Lista

    def Eliminacion_de_Copeas(self, Codigo):
        
        ALL_CODE = []
        Inicio = 1
        Fin = 0
        Con = 0
        Op = ""
        for i in Codigo:
            A = []
            if (i == 'Begin' or i == 'End'):
                A.append(i)
                ALL_CODE.append(A)    
            if (i == ';'):        
                Fin = Con + 1;        
            if (Inicio != 0 and Fin != 0):
                Op = Codigo[Inicio:Fin]
                ALL_CODE.append(Op)
                Inicio = Fin
                Fin = 0        
            Con += 1

        """
        print ("-----------------------------------------------")
        print ("Codigo Entrada")
        print ("-----------------------------------------------")
        
        for i in range(len(ALL_CODE)):
            for j in range(len(ALL_CODE[i])):
                print (ALL_CODE[i][j], end=" ")
            print ("\n")
        """

        Lista_Operacion = []
        Lista_Posiciones = []

        con = 0
        for i in ALL_CODE:
            if ("=" in i and len(i) < 5):
                Lista_Operacion.append(i[0:len(i)-1])
                Lista_Posiciones.append(con)
            con += 1

        L_V = []
        V_C = []
        L_P = []
        Var = []
        c = 0
        for i in range(len(Lista_Operacion)):
            try:
                x = float(Lista_Operacion[c][2])
                if(Lista_Operacion[c][0] not in L_V):
                    L_V.append(Lista_Operacion[c][0])
            except:
                Var.append(Lista_Operacion[c][0])
                V_C.append(Lista_Operacion[c][2])
                L_P.append(Lista_Posiciones[c])
            c += 1

        Opreaciones = ['+','-','*','/']
        c = 0
        while (c < len(L_P)):
            for i in range(len(ALL_CODE)):
                if (i == L_P[c]):
                    for x in range(i+1,len(ALL_CODE)):
                        for y in range(len(ALL_CODE[x])):
                            if (y > 1 and ALL_CODE[x][y] != ';' and ALL_CODE[x][y] not in Opreaciones and ALL_CODE[x][y] not in L_V):
                                if (Var[c] == ALL_CODE[x][y]):
                                    ALL_CODE[x][y] = V_C[c]
                    break
                    
            c += 1

        Elimincacion = []
        for i in range(len(ALL_CODE)):
            if (i not in L_P):
                Elimincacion.append(ALL_CODE[i])

        return Elimincacion
        """print ("-----------------------------------------------")
        print ("Codigo Salida Optimizado")
        print ("-----------------------------------------------")
        for i in range(len(Elimincacion)):
            for j in range(len(Elimincacion[i])):
                print (Elimincacion[i][j], end=" ")
            print ("\n")"""
