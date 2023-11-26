instrucciones = 0

table = [
  # 1
  [instrucciones, 'SEMICOLON', None],
  [instrucciones, 'COMA', None],
  [instrucciones, 'WHILE', [while_op, instrucciones]],
  [instrucciones, 'LPAREN', None],
  [instrucciones, 'RPAREN', None],
  [instrucciones, 'BBLOCK', None],
  [instrucciones, 'EBLOCK', ['empty']],
  [instrucciones, 'LECTURA', [scanf, 'SEMICOLON', instrucciones]],
  [instrucciones, 'COMILLAS_DOBLES', None],
  [instrucciones, 'ESCRITURA', [printf, 'SEMICOLON', instrucciones]],
  [instrucciones, 'BOOL', None],
  [instrucciones, 'LOGIC', None],
  [instrucciones, 'IGUAL', None],
  [instrucciones, 'INT', [var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'FLOAT', [var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'CHAR', [var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'RELATIONAL', None],
  [instrucciones, 'OPERADORES', None],
  [instrucciones, 'MODIFICADOR', None],
  [instrucciones, 'IDENTIFICADOR', [aux_var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'STRING', None],
  [instrucciones, 'NUMERO', None],
  [instrucciones, 'EOF', ['empty']],
]
