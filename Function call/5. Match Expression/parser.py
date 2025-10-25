import ply.yacc as yacc
from lexer import tokens

start = 'program'

def p_program(p):
    '''program : match_expression'''
    p[0] = p[1]
    print("\n Valid Match Expression (AST Output):")

def p_match_expression(p):
    '''match_expression : MATCH expression LBRACE match_arms RBRACE'''
    p[0] = ('match', p[2], p[4])

def p_match_arms(p):
    '''match_arms : match_arms match_arm
                  | match_arm'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_match_arm(p):
    '''match_arm : pattern ARROW expression
                 | pattern ARROW expression COMMA'''
    p[0] = (p[1], p[3])

def p_pattern(p):
    '''pattern : IDENTIFIER
               | UNDERSCORE
               | NUMBER'''
    p[0] = p[1]

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | function_call
                  | match_expression'''
    p[0] = p[1]

def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN arguments RPAREN
                     | IDENTIFIER LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = ('call', p[1], p[3])
    else:
        p[0] = ('call', p[1], [])

def p_arguments(p):
    '''arguments : arguments COMMA expression
                 | expression'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type}, line: {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()