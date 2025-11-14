import ply.yacc as yacc
from lexer import tokens

variables = {}
start = 'statements'

def p_statements_multiple(p):
    "statements : statements statement"
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    "statements : statement"
    p[0] = [p[1]]

def p_statement_let(p):
    "statement : LET ID ASSIGN expression SEMICOLON"
    variables[p[2]] = {"value": p[4], "mutable": False}
    p[0] = p[4]

def p_statement_let_mut(p):
    "statement : LET MUT ID ASSIGN expression SEMICOLON"
    variables[p[3]] = {"value": p[5], "mutable": True}
    p[0] = p[5]

def p_statement_assign(p):
    "statement : ID ASSIGN expression SEMICOLON"
    name = p[1]
    if name not in variables:
        print(f"Error: variable '{name}' not defined")
    elif not variables[name]["mutable"]:
        print(f"Error: variable '{name}' is immutable")
    else:
        variables[name]["value"] = p[3]
    p[0] = p[3]

def p_statement_if_else(p):
    "statement : IF condition block ELSE block"
    p[0] = p[3] if p[2] else p[5]

def p_statement_if(p):
    "statement : IF condition block"
    p[0] = p[3] if p[2] else None

def p_block(p):
    "block : LBRACE statements RBRACE"
    p[0] = p[2]

def p_condition(p):
    "condition : expression compare_op expression"
    op = p[2]
    if op == ">": p[0] = p[1] > p[3]
    elif op == "<": p[0] = p[1] < p[3]
    elif op == ">=": p[0] = p[1] >= p[3]
    elif op == "<=": p[0] = p[1] <= p[3]
    elif op == "==": p[0] = p[1] == p[3]
    elif op == "!=": p[0] = p[1] != p[3]

def p_compare_op(p):
    """
    compare_op : GT
               | LT
               | GE
               | LE
               | EQ
               | NE
    """
    p[0] = p[1]

def p_expression_binop(p):
    """
    expression : expression PLUS term
               | expression MINUS term
    """
    p[0] = p[1] + p[3] if p[2] == "+" else p[1] - p[3]

def p_expression_term(p):
    "expression : term"
    p[0] = p[1]

def p_term_binop(p):
    """
    term : term TIMES factor
         | term DIVIDE factor
    """
    if p[2] == "*":
        p[0] = p[1] * p[3]
    else:
        if p[3] == 0:
            print("Error: division by zero")
            p[0] = 0
        else:
            p[0] = p[1] // p[3]

def p_term_factor(p):
    "term : factor"
    p[0] = p[1]

def p_factor_number(p):
    "factor : NUMBER"
    p[0] = p[1]

def p_factor_variable(p):
    "factor : ID"
    name = p[1]
    if name not in variables:
        print(f"Error: variable '{name}' not defined")
        p[0] = 0
    else:
        p[0] = variables[name]["value"]

def p_factor_group(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
