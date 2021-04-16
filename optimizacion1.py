
class opti1():
    def precalculo(self,codigo):
        cod_res=codigo.copy()
        op1=["*","/"]
        op2=["+","-"]
        vars=[]
        vals=[]
        lineas=[]
        cols=[]
        ban=False
        ban2=True
        exp=[]
        idx=0
        idx_m=[]
        c1=0
        while ban2:
            linea=1
            col=0
            c2=0
            codigo=cod_res.copy()
            for i in range(1,len(codigo)):
                if codigo[i]=="=":
                    print(codigo[i + 2])
                    if codigo[i-1] not in vars:
                        vars.append(codigo[i-1])
                        if codigo[i+2]==";":
                            if self.checknum2(codigo[i+1]):
                                vals.append(codigo[i+1])
                            else:
                                vals.append('')
                        else:
                            vals.append('')
                    else:
                        if codigo[i+2]==";":
                            if self.checknum2(codigo[i+1]):
                                vals[vars.index(codigo[i-1])]=codigo[i+1]
            print(vars)
            print(vals)
            print("\n")
            for i in range(len(codigo)):
                col+=1
                if codigo[i] == "=":
                    ban = True
                elif codigo[i]==";":
                    linea+=1
                    col=0
                    ban=False
                    c1=0
                    exp=[]
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
                                #print(res)
                            else:
                                res = float(exp[0]) / float(exp[2])
                                #print(res)
                            for i in range(3):
                                cod_res.pop(idx)
                            cod_res.insert(idx, res)
                            idx_m = []
                            c2 += 1
                        elif exp[1] in op1 and self.checknum2(exp[0])==False and self.checknum2(exp[2])==False:
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
                        elif exp[1] in op1 and self.checknum2(exp[0])==False:
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
                        elif exp[1] in op1 and self.checknum2(exp[2])==False:
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
                        elif exp[1] in op1:
                            if linea not in lineas:
                                lineas.append(linea)
                                cols.append(col)
                            else:
                                cols[lineas.index(linea)]=col
                            idx_m.pop()
                        elif exp[1] in op2:
                            c2+=1
                            idx_m.pop()
                        else:
                            idx_m.pop()
                        exp = []
                        ban = False
            if c2==0:
                ban2=False
        print(cod_res)
        print(idx_m)
        print("\n")

        exp=[]
        ban2=True
        ban=False
        idx_m=[]
        c1=0
        while ban2:
            linea=1
            col=0
            c2=0
            codigo=cod_res.copy()
            for i in range(1,len(codigo)):
                if codigo[i]=="=":
                    print(codigo[i + 2])
                    if codigo[i-1] not in vars:
                        vars.append(codigo[i-1])
                        if codigo[i+2]==";":
                            if self.checknum2(codigo[i+1]):
                                vals.append(codigo[i+1])
                            else:
                                vals.append('')
                        else:
                            vals.append('')
                    else:
                        if codigo[i+2]==";":
                            if self.checknum2(codigo[i+1]):
                                vals[vars.index(codigo[i-1])]=codigo[i+1]
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
                        elif exp[1] in op2 and self.checknum2(exp[0])==False and self.checknum2(exp[2])==False:
                            if linea in lineas:
                                idx_m.pop()
                            else:
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
                            c2 += 1
                        elif exp[1] in op2 and self.checknum2(exp[0])==False:
                            if linea in lineas:
                                idx_m.pop()
                            else:
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
                            c2 += 1
                        elif exp[1] in op2 and self.checknum2(exp[2])==False:
                            if linea in lineas:
                                idx_m.pop()
                            else:
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
                            c2 += 1
                        else:
                            idx_m.pop()
                        exp = []
                        ban = False
            if c2==0:
                ban2=False
        print(cod_res)

    def nulas(self,codigo):
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

    def checknum2(self, numero):
        try:
            n = float(numero)
            return True
        except:
            return False


#codi=['Begin', 'int', 'a', ',', 'b', ';', 'a', '=', 'b', '*', '1','*','1','/','3','*','2','+','2', ';','b','=','a','/','1',';', 'End']
codi=['Begin',
      'int', 'a', ',', 'b',',', 'c', ';',
      'a', '=', '12',';',
      'b','=','40',';',
      'c','=','a','+','2',';',
      'b','=','c','/','2',';',
      'End']
op1=opti1()
op1.precalculo(codi)
#op1.nulas(codi)