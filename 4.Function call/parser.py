import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : function_call'''
    print("Valid function call:", p[1])

def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN RPAREN
                     | IDENTIFIER LPAREN arguments RPAREN'''
    if len(p) == 4:
        p[0] = ('call', p[1], [])
    else:
        p[0] = ('call', p[1], p[3])

def p_arguments(p):
    '''arguments : arguments COMMA expression
                 | expression'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | function_call'''
    p[0] = p[1]

def p_error(p):
    print(" Syntax error!")

parser = yacc.yacc()