import ply.yacc as yacc
from lexer import tokens
precedence = (
    ('left', 'OR'),                    # Operador OR lógico
    ('left', 'AND'),                   # Operador AND lógico
    ('right', 'NOT'),                  # Operador NOT lógico
    ('nonassoc', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),  # Operadores relacionales
    ('left', 'PLUS', 'MINUS'),         # Operadores de suma y resta
    ('left', 'TIMES', 'DIVIDE'),       # Operadores de multiplicación y división
)

def p_program(p):
    '''program : program statement
               | statement
    '''
    # Programa compuesto de múltiples declaraciones

def p_statement(p):
    '''statement : expression_statement
                 | compound_statement
                 | selection_statement
                 | iteration_statement
                 | jump_statement
                 | function_declaration
    '''
    # Diferentes tipos de declaraciones y sentencias

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON
                            | SEMICOLON
    '''
    # Una expresión seguida de un punto y coma

def p_compound_statement(p):
    '''compound_statement : LBRACE statement_list RBRACE
                          | LBRACE RBRACE
    '''
    # Bloque de código

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement
    '''
    # Lista de declaraciones o sentencias

# Definición de expresiones (operadores aritméticos y lógicos)
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression
                  | LPAREN expression RPAREN
                  | ID
                  | NUMBER
    '''

# Definiciones de selección (if-else)
def p_selection_statement(p):
    '''selection_statement : IF LPAREN expression RPAREN statement
                           | IF LPAREN expression RPAREN statement ELSE statement
    '''
    # Estructuras if y if-else

# Definiciones de iteración (for, while, do-while)
def p_iteration_statement(p):
    '''iteration_statement : WHILE LPAREN expression RPAREN statement
                           | DO statement WHILE LPAREN expression RPAREN SEMICOLON
                           | FOR LPAREN expression_statement expression_statement expression RPAREN statement
    '''
    # Bucles for, while y do-while

# Definiciones de salto (return)
def p_jump_statement(p):
    '''jump_statement : RETURN expression SEMICOLON
                      | RETURN SEMICOLON
    '''
    # Instrucciones de retorno

# Definición de la función
def p_function_declaration(p):
    '''function_declaration : TYPE ID LPAREN params RPAREN compound_statement'''
    # Definición de una función

# Parámetros de la función
def p_params(p):
    '''params : param_list
              | empty
    '''
    # Lista de parámetros

def p_param_list(p):
    '''param_list : param_list COMMA TYPE ID
                  | TYPE ID
    '''
    # Parámetros de función

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
