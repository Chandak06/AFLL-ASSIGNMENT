import ply.lex as lex

tokens = (
    'ID',
    'NUMBER',
    'ASSIGN',
    'SEMICOLON',
    'LET',
)

t_ASSIGN = r'='
t_SEMICOLON = r';'

reserved = {
    'let': 'LET',
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
