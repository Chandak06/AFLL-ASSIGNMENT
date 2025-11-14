import ply.lex as lex

tokens = [
    'MATCH',
    'ID', 'NUMBER',
    'ARROW',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'COMMA',
    'UNDERSCORE'
]

t_ARROW     = r'=>'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','

def t_MATCH(t):
    r'match'
    return t

def t_UNDERSCORE(t):
    r'_'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
