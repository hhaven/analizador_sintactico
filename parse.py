import ply.yacc as yacc
from lexer import tokens
from symboltable import SymbolTable

# Crear una instancia de la tabla de símbolos
symbol_table = SymbolTable()

# Regla para el programa completo
def p_program(p):
    '''program : program statement
               | statement
    '''
    # Programa compuesto de múltiples declaraciones o sentencias

# Regla para las diferentes sentencias
def p_statement(p):
    '''statement : variable_declaration
                 | conditional_statement
                 | function_call SEMICOLON
                 | return_statement
                 | function_declaration
    '''
    # Incluye declaraciones de variables, condicionales y llamadas a funciones

def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON
                       | RETURN SEMICOLON
    '''

# Regla para la declaración de variables
def p_variable_declaration(p):
    '''variable_declaration : TYPE ID SEMICOLON'''
    # Agregar variable a la tabla de símbolos
    symbol_table.add(p[2], p[1], None, p.lineno(2))

# Regla para las estructuras condicionales if-else
def p_conditional_statement(p):
    '''conditional_statement : IF LPAREN expression RPAREN compound_statement
                             | IF LPAREN expression RPAREN compound_statement ELSE compound_statement'''
    #

def p_compound_statement(p):
    '''compound_statement : LBRACE statement_list RBRACE
                          | LBRACE RBRACE'''
    if len(p) == 3:
        # Esto maneja un bloque vacío: {}
        p[0] = None
    else:
        # Esto maneja un bloque con sentencias
        p[0] = p[2]

# Regla para las expresiones
def p_expression(p):
    '''expression : STRING
                  | ID
                  | NUMBER
                  | LPAREN expression RPAREN
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
    '''
    # Expresiones, incluyendo operaciones aritméticas y comparaciones

# Regla para llamadas a funciones
def p_function_call(p):
    '''function_call : ID LPAREN argument_list RPAREN
                     | ID LPAREN RPAREN
    '''
# Regla para la declaración de funciones
def p_function_declaration(p):
    '''function_declaration : TYPE ID LPAREN argument_list RPAREN LBRACE statement_list RBRACE
                            | TYPE ID LPAREN RPAREN LBRACE statement_list RBRACE
    '''

# Regla para la lista de argumentos en llamadas a funciones
def p_argument_list(p):
    '''argument_list : argument_list COMMA expression
                     | expression
    '''
    # Lista de argumentos en una llamada a función

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement
    '''
    if len(p) == 3:
        # maneja multiples sentencias
        p[0] = p[1] + [p[2]]
    else:
        # maneja una unica sentencia
        p[0] = [p[1]]


# Regla para manejar errores de sintaxis
def p_error(p):
    if p:
        print(f"Syntax error at {p.value} on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Construir el parser
parser = yacc.yacc(debug=True)