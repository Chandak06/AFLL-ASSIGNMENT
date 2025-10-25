import ply.lex as lex

tokens = (
    'MATCH',
    'IDENTIFIER',
    'NUMBER',
    'UNDERSCORE',
    'ARROW',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'COMMA'
)

t_ARROW = r'=>'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_UNDERSCORE = r'_'

keywords = {
    'match': 'MATCH',
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t

t_ignore = ' \t'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()