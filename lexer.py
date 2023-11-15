import ply.lex as lex

# Lista de nombres de tokens
tokens = [
    'INCLUDE', 'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'ASSIGN', 'STRING',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'AND', 'OR', 'NOT',
    # Palabras reservadas
    'IF', 'ELSE', 'FOR', 'WHILE', 'DO', 'VOID', 'RETURN', 'TYPE'
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
    'int': 'TYPE', 'float': 'TYPE', 'char': 'TYPE'
}

# Reglas para expresiones regulares simples
t_PLUS = r'\+'; t_MINUS = r'-'; t_TIMES = r'\*'; t_DIVIDE = r'/'
t_LPAREN = r'\('; t_RPAREN = r'\)'; t_LBRACE = r'\{'; t_RBRACE = r'\}'
t_SEMICOLON = r';'; t_COMMA = r','; t_ASSIGN = r'='
t_LT = r'<'; t_LE = r'<='; t_GT = r'>'; t_GE = r'>='; t_EQ = r'=='; t_NE = r'!='
t_AND = r'&&'; t_OR = r'\|\|'; t_NOT = r'!'

def t_INCLUDE(t):
    r'\#include[ ]*<[^>]+>|\"[^"]+\"'
    return t

# Reglas más complejas para ID y NUMBER
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Token para comentarios de una línea y multilínea
def t_COMMENT(t):
    r'\/\/.*|\/\*[\s\S]*?\*\/'
    pass  # Los comentarios son ignorados

# Token para cadenas de caracteres
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Token para caracteres (puede que necesites esto dependiendo de tu código)
def t_CHAR(t):
    r"\'([^\\\n]|(\\.))*?\'"
    return t

# Token para números (enteros y flotantes)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Caracteres ignorados
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
