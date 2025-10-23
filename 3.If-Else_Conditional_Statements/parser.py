import ply.yacc as yacc
from lexer import tokens

# Symbol table (optional)
variables = {}

# -------------------------------
# Statements
# -------------------------------
def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = None

def p_statements_single(p):
    'statements : statement'
    p[0] = None

# Assignment inside if/else blocks
def p_statement_assign(p):
    'statement : ID ASSIGN NUMBER SEMICOLON'
    variables[p[1]] = p[3]
    p[0] = p[3]

# If-Else
def p_statement_if_else(p):
    'statement : IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'
    if p[3]:
        p[0] = p[6]
    else:
        p[0] = p[10]

def p_statement_if(p):
    'statement : IF LPAREN condition RPAREN LBRACE statements RBRACE'
    if p[3]:
        p[0] = p[6]

# -------------------------------
# Conditions (simple numeric comparisons)
# -------------------------------
def p_condition(p):
    '''
    condition : NUMBER GT NUMBER
              | NUMBER LT NUMBER
              | NUMBER GE NUMBER
              | NUMBER LE NUMBER
              | NUMBER EQ NUMBER
              | NUMBER NE NUMBER
    '''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")
    exit(1)

parser = yacc.yacc()
