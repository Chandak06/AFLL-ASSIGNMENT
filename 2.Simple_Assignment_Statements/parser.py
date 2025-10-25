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
    'statement : ID ASSIGN NUMBER SEMICOLON'
    variables[p[1]] = p[3]
    p[0] = p[3]

def p_statement_let_assign(p):
    'statement : LET ID ASSIGN NUMBER SEMICOLON'
    variables[p[2]] = p[4]
    p[0] = p[4]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
