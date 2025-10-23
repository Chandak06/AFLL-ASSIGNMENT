import ply.lex as lex

tokens = (
    'NUMBER',
    'ID',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN',
    'SEMICOLON',
    'LPAREN', 'RPAREN',
    'LET',
)


t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='

t_SEMICOLON = r';'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'

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
