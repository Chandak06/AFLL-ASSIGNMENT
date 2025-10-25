import ply.yacc as yacc
from lexer import tokens

variables = {}
start = 'statement'

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = None

def p_statements_single(p):
    'statements : statement'
    p[0] = None

def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    variables[p[1]] = p[3]
    p[0] = p[3]

def p_statement_let_assign(p):
    'statement : LET ID ASSIGN expression SEMICOLON'
    variables[p[2]] = p[4]
    p[0] = p[4]


def p_expression_binop(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        if p[3] == 0:
            print("Error: Division by zero!")
            p[0] = 0
        else:
            p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    try:
        p[0] = variables[p[1]]
    except KeyError:
        print(f"Error: Variable '{p[1]}' not defined")
        p[0] = 0

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
