import ply.yacc as yacc
from lexer import tokens

variables = {}   # {name: {"value": int, "mutable": True/False}}
start = 'statements'

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statement_let(p):
    'statement : LET ID ASSIGN NUMBER SEMICOLON'
    variables[p[2]] = {"value": p[4], "mutable": False}
    p[0] = p[4]

def p_statement_let_mut(p):
    'statement : LET MUT ID ASSIGN NUMBER SEMICOLON'
    variables[p[3]] = {"value": p[5], "mutable": True}
    p[0] = p[5]

def p_statement_assign(p):
    'statement : ID ASSIGN NUMBER SEMICOLON'
    name = p[1]

    if name not in variables:
        print(f"Error: variable '{name}' not defined")

    elif not variables[name]["mutable"]:
        print(f"Error: cannot assign to immutable variable '{name}'")

    else:
        variables[name]["value"] = p[3]

    p[0] = p[3]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
