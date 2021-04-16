import pydot
import os
from tkinter import *
from PIL import ImageTk,Image

class Arbol():
    def comprueba(self,exp):
        if exp in operadores:
            node=pydot.Node("Operador"+str(self.conope)+"\ntipo    valor", shape="rectangle")
            G.add_node(node)
            self.conope+=1
            return node
        try:
            int(exp)
            node = pydot.Node("Numero" + str(self.conNum)+"\ntipo    valor", shape="rectangle")
            G.add_node(node)
            self.conNum += 1
            return node
        except ValueError:
            node = pydot.Node("Variable" + str(self.convar)+"\ntipo    valor", shape="rectangle")
            G.add_node(node)
            self.convar += 1
            return node

    def principal(self,operacion,numim):
        global operadores,G
        os.environ["PATH"] += os.pathsep + 'C:/Program Files(x86)/Graphviz 2.44.1/bin'

        operadores = ["+", "-", "*", "/"]
        #operacion = "var=5*b"
        con = 0
        for i in operacion:
            if i in operadores:
                con += 1
        if con==0:
            return False

        # Variables para contar los terminos que se repiten
        conop = 1
        self.convar = 1
        self.conNum = 1
        self.conope = 1
        congeneral=0

        G = pydot.Dot(graph_type="digraph", rankdir="UD", label=operacion, fontsize="24")
        root = "Programa"
        node = pydot.Node(root + "\ntipo    valor", shape="rectangle")
        G.add_node(node)
        node2 = pydot.Node("Begin\ntipo    valor", shape="rectangle")
        G.add_node(node2)
        edge = pydot.Edge(node, node2)
        G.add_edge(edge)
        node3 = pydot.Node("Sentencias\ntipo    valor", shape="rectangle")
        G.add_node(node3)
        edge = pydot.Edge(node, node3)
        G.add_edge(edge)
        node4 = pydot.Node("End\ntipo    valor", shape="rectangle")
        G.add_node(node4)
        edge = pydot.Edge(node, node4)
        G.add_edge(edge)
        node5 = pydot.Node("Declaracion\ntipo    valor", shape="rectangle")
        G.add_node(node5)
        edge = pydot.Edge(node3, node5)
        G.add_edge(edge)
        op = operacion.split("=")
        node6 = pydot.Node("Variable" + str(self.convar) + "\ntipo    valor", shape="rectangle")
        G.add_node(node6)
        edge = pydot.Edge(node5, node6)
        G.add_edge(edge)
        edge = pydot.Edge(node5, "=")
        G.add_edge(edge)
        edge = pydot.Edge(node6, op[0])
        G.add_edge(edge)
        node7 = pydot.Node("Exp\ntipo    valor", shape="rectangle")
        G.add_node(node7)
        edge = pydot.Edge(node5, node7)
        G.add_edge(edge)
        node8 = pydot.Node("Operacion" + str(conop) + "\ntipo    valor", shape="rectangle")
        G.add_node(node8)
        edge = pydot.Edge(node7, node8)
        G.add_edge(edge)
        self.convar += 1
        if con == 1:
            exp = ""
            for i in op[1]:
                if i in operadores:
                    nodo = self.comprueba(exp)
                    edge = pydot.Edge("Operacion" + str(conop) + "\ntipo    valor", nodo)
                    G.add_edge(edge)
                    nodo2=self.comprueba(i)
                    edge = pydot.Edge("Operacion" + str(conop) + "\ntipo    valor", nodo2)
                    G.add_edge(edge)
                    nodo4=pydot.Node("General"+str(congeneral), label=i)
                    G.add_node(nodo4)
                    edge = pydot.Edge(nodo2, nodo4)
                    G.add_edge(edge)
                    congeneral+=1
                    nodo3=pydot.Node("General"+str(congeneral), label=exp)
                    G.add_node(nodo3)
                    edge = pydot.Edge(nodo, nodo3)
                    G.add_edge(edge)
                    congeneral+=1
                    exp = ""
                else:
                    exp += i
            nodo = self.comprueba(exp)
            edge = pydot.Edge("Operacion" + str(conop) + "\ntipo    valor", nodo)
            G.add_edge(edge)
            nodo3 = pydot.Node("General" + str(congeneral), label=exp)
            G.add_node(nodo3)
            edge = pydot.Edge(nodo, nodo3)
            G.add_edge(edge)
            congeneral+=1
        else:
            while con >= 1:
                exp = ""
                c = 0
                for i in op[1]:
                    c += 1
                    if i in operadores:
                        nodo = self.comprueba(exp)
                        edge = pydot.Edge("Operacion" + str(conop) + "\ntipo    valor", nodo)
                        G.add_edge(edge)
                        nodo2 = self.comprueba(i)
                        edge = pydot.Edge("Operacion" + str(conop) + "\ntipo    valor", nodo2)
                        G.add_edge(edge)
                        nodo4 = pydot.Node("General" + str(congeneral), label=i)
                        G.add_node(nodo4)
                        edge = pydot.Edge(nodo2, nodo4)
                        G.add_edge(edge)
                        congeneral += 1
                        nodo3 = pydot.Node("General" + str(congeneral), label=exp)
                        G.add_node(nodo3)
                        edge = pydot.Edge(nodo, nodo3)
                        G.add_edge(edge)
                        congeneral += 1
                        exp = ""
                        break
                    else:
                        exp += i
                if con>1:
                    node10=pydot.Node("Operacion" + str(conop) + "\ntipo    valor", shape="rectangle")
                    node11 = pydot.Node("Operacion" + str(conop+1) + "\ntipo    valor", shape="rectangle")
                    G.add_node(node10)
                    G.add_node(node11)
                    edge = pydot.Edge(node10,node11)
                    G.add_edge(edge)
                    conop += 1

                op[1] = (op[1])[c:len(op[1])]
                con -= 1

            print(op[1])
            nodo = self.comprueba(op[1])
            edge = pydot.Edge("Operacion" + str(conop) + "\ntipo    valor", nodo)
            G.add_edge(edge)
            nodo3 = pydot.Node("General" + str(congeneral), label=op[1])
            G.add_node(nodo3)
            edge = pydot.Edge(nodo, nodo3)
            G.add_edge(edge)
            congeneral += 1

        G.write("arbol"+str(numim)+".png", format='png')

        return True



