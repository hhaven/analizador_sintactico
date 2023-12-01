#importaciones y conf global
from lexer import tokens, lexer
from parse_table import *
from collections import defaultdict
import time
import sys

stack = ["EOF", 0]

def parse():
    # Abre y lee un archivo de código fuente.
    f = open('code2.c', 'r')
    code = f.read()
    lexer.input(code)    
    tok=lexer.token()
    x=stack[-1] #primer elemento de la pila
    # Bucle principal de análisis.
    while True:    
        if x is not None and tok is not None:
        #Manejo de Tokens y Pila
            if x == tok.type:
                symbol_table_insert(tok.value, tok.type, tok.lineno, tok.lexpos)
                stack.pop()
                x=stack[-1]
                tok=lexer.token()
        #Manejo de errores           
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", x)
                print("Se encontro: ", tok.type)
                print("En posición:", tok.lexpos)
                print("En linea:", tok.lineno)
                tok = panic_mode_recovery(x, tok)
                continue
            if x not in tokens:
                if tok is None:
                    print("Analisis sintactico completado con exito")
                    return #aceptar
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                print("En linea:", tok.lineno)
                print("Con valor: ", tok.value)
                celda=search_in_table(x,tok.type)      
                #Manejo de Errores y Recuperación                      
                if  celda is None:
                    expected_tokens = find_expected_tokens(x)
                    print("Error: se esperaba uno de", expected_tokens, "pero se encontró", tok.type)
                    print("En posición:", tok.lexpos)
                    print("En linea:", tok.lineno)
                    print("celda: ", celda)
                    print("Entrando en modo pánico...")
                    tok = panic_mode_recovery(expected_tokens, tok)
                    if tok is None or tok.type == 'EOF':
                        print("No se pudo recuperar del error.")
                        return 0
                    # Reanuda el análisis después de la recuperación
                    x = stack[-1]
                    continue
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("/------------------------------------------------------------------------------/")
                    x=stack[-1]
        else:
            print("Analisis sintactico completado con exito")
            return 0;
        #Manejo de No Terminales
        
            


def barra_de_progreso(duracion, longitud_barra=50):
    for i in range(longitud_barra + 1):
        porcentaje = int((i / longitud_barra) * 100)
        barra = '#' * i + '-' * (longitud_barra - i)
        sys.stdout.write(f"\r[{barra}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / longitud_barra)
    print()

def panic_mode_recovery(recovery_tokens, tok):
    # Bucles que buscan un token de recuperacion y ajustan la pila.
    while tok is not None and tok.type not in recovery_tokens:
        tok = lexer.token()
        print(f"Buscando {recovery_tokens}")
    while stack and (stack[-1] not in recovery_tokens and stack[-1] in tokens):
        stack.pop()

    if stack and tok is not None:
        barra_de_progreso(1)
        print(f"Recuperación exitosa, próximo token: {tok.type}, próximo en la pila: {stack[-1]}")
        return tok
    else:
        barra_de_progreso(1)
        print("La pila está vacía después de la recuperación del modo pánico.")
        return tok
def search_in_table(no_terminal, terminal):
    for i in range(len(table)):
        if( table[i][0] == no_terminal and table[i][1] == terminal):
            return table[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'empty': #la vacía no la inserta
            stack.append(elemento)

def find_expected_tokens(no_terminal):
    expected = []
    for row in table:
        if row[0] == no_terminal and row[2] is not None:
            expected.append(row[1])
    return expected

# Tabla de símbolos
symbol_table = defaultdict(list)

# Insertar en la tabla de símbolos
def symbol_table_insert(name, var_type, line, pos):
    symbol_table[name].append({"type": var_type, "line": line, "pos": pos})

# Mostrar la tabla de símbolos
def symbol_table_print():
    print("Nombre                             Tipo              Linea    Posicion")
    print("----------------------------------------------------------------------")
    for name, entries in symbol_table.items():
        for entry in entries:
            print(f"{name:<35}{entry['type']:10}{entry['line']:10}{entry['pos']:10}")


# Buscar en la tabla de símbolos
def symbol_table_search(name):
    if name in symbol_table:
        for info in symbol_table[name]:
            print(f"{name} - {info}")
    else:
        print(f"No se encontró '{name}' en la tabla de símbolos.")

# Borrar de la tabla de símbolos
def symbol_table_delete(name):
    if name in symbol_table:
        del symbol_table[name]
        print(f"'{name}' eliminado de la tabla de símbolos.")
    else:
        print(f"No se pudo eliminar '{name}' porque no se encuentra en la tabla de símbolos.")

parse()
symbol_table_print()