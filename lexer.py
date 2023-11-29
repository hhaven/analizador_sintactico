import ply.lex as lex

# Lista de nombres de tokens
tokens = [
    'INCLUDE', 'STRING', 'ID', 'NUMBER', 'QUOTES',
    'READ', 'WRITE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'ASSIGN',
    'RELATIONAL', 'OP', 'LOGIC',
    'EOF',
    # Palabras reservadas
    'IF', 'ELSE', 'FOR', 'WHILE', 'DO', 'VOID', 'RETURN', 'INT', 'FLOAT', 'CHAR',
]

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR', 
    'while': 'WHILE', 
    'do': 'DO',
    'void': 'VOID', 
    'return': 'RETURN',
    'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR',
    'scanf' : 'READ',
    'printf':'WRITE',
}

# Reglas para expresiones regulares simples
t_LPAREN = r'\('; t_RPAREN = r'\)'; t_LBRACE = r'\{'; t_RBRACE = r'\}'
t_SEMICOLON = r';'; t_COMMA = r','; t_ASSIGN = r'='; t_QUOTES = r'\"' ; t_EOF = r'\$'

def t_INCLUDE(t):
    r'\#include[ ]*<[^>]+>'  # Esta parte reconoce el formato #include <nombre>
    t.lexer.lineno += t.value.count('\n')  # Incrementa el número de línea según los saltos de línea en el comentario
    pass  # include ignorados

# Token para cadenas de caracteres
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*\"'
    #print(f"STRING token: {t.value}, Line: {t.lineno}")
    return t
    
# Reglas más complejas para ID y NUMBER
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Palabras reservadas
    #print(f"ID token: {t.value}, Line: {t.lineno}")
    return t

# Token para comentarios de una línea y multilínea
def t_COMMENT(t):
    r'\/\/.*|\/\*[\s\S]*?\*\/'
    t.lexer.lineno += t.value.count('\n')  # Incrementa el número de línea según los saltos de línea en el comentario
    pass  # Los comentarios son ignorados

# Token para caracteres
def t_CHAR(t):
    r'\"([^\\"]|\\.|\n)*\"'
    return t

# Token para números (enteros y flotantes)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    #print(f"NUMBER token: {t.value}, Line: {t.lineno}")
    return t

# Token para operadores
def t_OP(t):
    r'(\+)|(\-)|(\*)|(\/)|(\%)'
    return t

# Token para operadores logicos
def t_LOGIC(t):
    r'(\>=)|(\<=)|(\==)|(\!=)|(\<)|(\>)'
    return t

# Token para relaciones && ||
def t_RELATIONAL(t):
    r'(\&{2})|(\|{2})'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# Caracteres ignorados
t_ignore = ' \t'

def t_error(t):
    #print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex(debug=1)
