import ply.yacc as yacc
from lexer import tokens

# Symbol table now stores:
# { var_name: { "value": <int>, "mutable": True/False } }
variables = {}

start = 'statements'

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]


# -----------------------------
#   LET (immutable)
# -----------------------------
def p_statement_let(p):
    'statement : LET ID ASSIGN expression SEMICOLON'
    if p[2] in variables:
        print(f"Error: variable '{p[2]}' already defined")
    else:
        variables[p[2]] = {"value": p[4], "mutable": False}
    p[0] = p[4]


# -----------------------------
#   LET MUT (mutable)
# -----------------------------
def p_statement_let_mut(p):
    'statement : LET MUT ID ASSIGN expression SEMICOLON'
    if p[3] in variables:
        print(f"Error: variable '{p[3]}' already defined")
    else:
        variables[p[3]] = {"value": p[5], "mutable": True}
    p[0] = p[5]


# -----------------------------
#   Assignment (must be mutable)
# -----------------------------
def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    name = p[1]

    if name not in variables:
        print(f"Error: variable '{name}' not defined")
    else:
        if not variables[name]["mutable"]:
            print(f"Error: cannot assign to immutable variable '{name}'")
        else:
            variables[name]["value"] = p[3]

    p[0] = p[3]


# -----------------------------
#   Expressions
# -----------------------------
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


# -----------------------------
#   Term ( * / )
# -----------------------------
def p_term_binop(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        if p[3] == 0:
            print("Error: division by zero")
            p[0] = 0
        else:
            # Rust-style integer division
            p[0] = p[1] // p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


# -----------------------------
#   Factor
# -----------------------------
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_id(p):
    'factor : ID'
    if p[1] not in variables:
        print(f"Error: variable '{p[1]}' not defined")
        p[0] = 0
    else:
        p[0] = variables[p[1]]["value"]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()
