import ply.yacc as yacc
from lexer import tokens

start = 'program'

def p_program(p):
    "program : match_expression"
    print("Valid Match Expression:", p[1])
    p[0] = p[1]

def p_match_expression(p):
    "match_expression : MATCH expression LBRACE match_arms RBRACE"
    p[0] = ('match', p[2], p[4])

def p_match_arms(p):
    """
    match_arms : match_arms match_arm
               | match_arm
    """
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_match_arm(p):
    """
    match_arm : pattern ARROW expression COMMA
              | pattern ARROW expression
    """
    p[0] = (p[1], p[3])

def p_pattern(p):
    """
    pattern : ID
            | NUMBER
            | UNDERSCORE
    """
    p[0] = p[1]

def p_expression_base(p):
    """
    expression : NUMBER
               | ID
    """
    p[0] = p[1]

def p_expression_call(p):
    "expression : function_call"
    p[0] = p[1]

def p_expression_match(p):
    "expression : match_expression"
    p[0] = p[1]

def p_function_call(p):
    """
    function_call : ID LPAREN RPAREN
                  | ID LPAREN arguments RPAREN
    """
    if len(p) == 4:
        p[0] = ('call', p[1], [])
    else:
        p[0] = ('call', p[1], p[3])

def p_arguments(p):
    """
    arguments : arguments COMMA expression
              | expression
    """
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
