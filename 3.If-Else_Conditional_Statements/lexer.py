import ply.lex as lex

tokens = (
    'IF', 'ELSE',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'ID', 'NUMBER',
    'ASSIGN', 'SEMICOLON',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'
)

# Keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE',
}

# Operators
t_ASSIGN = r'='
t_GT     = r'>'
t_LT     = r'<'
t_GE     = r'>='
t_LE     = r'<='
t_EQ     = r'=='
t_NE     = r'!='

# Delimiters
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_SEMICOLON = r';'

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
