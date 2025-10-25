import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'COMMA',
    'LPAREN',
    'RPAREN',
)

t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()