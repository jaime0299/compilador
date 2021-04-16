class Archivo:

    def Sacar(self,nom):

        L = []

        Lista = open(str(nom),"r")
        for linea in Lista:
            if linea[-1] == '\n':
                linea = linea[:-1]
            n = ""
            for i in range(len(linea)):
                n += linea[i]
            L.append(str(linea))
        Lista.close()

        return L