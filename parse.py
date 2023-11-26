from lexer import tokens, lexer
from parse_table import *
from collections import defaultdict

stack = ["EOF", 0]

def parse(code):
    f = open('c.c', 'r')
    code = f.read()
    lexer.input(code)    
    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:    
        if x == tok.type and x == 'EOF':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'EOF':
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                print("En posición:", tok.lexpos)
                print("En linea:", tok.lineno)
                return 0;
            if x not in tokens: #es no terminal
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                print("En linea:", tok.lineno)
                celda=search_in_table(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    print("En linea:", tok.lineno)
                    print("celda: ", celda)
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("/--------------------------------/")
                    x=stack[-1]            
def search_in_table(no_terminal, terminal):
    for i in range(len(table)):
        if( table[i][0] == no_terminal and table[i][1] == terminal):
            return table[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'empty': #la vacía no la inserta
            stack.append(elemento)
