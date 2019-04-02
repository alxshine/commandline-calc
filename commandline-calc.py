import ply.lex as lex
import ply.yacc as yacc
import custom_formats

#lexing rules
reserved = {
    "hex": 'FORMAT_HEX',
    "bin": 'FORMAT_BIN',
        }

format_functions = {
    "hex": custom_formats.format_hex,
    "bin": custom_formats.format_bin
        }

tokens = [ 
        'DEC', 'HEX', 'BIN',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
        'LPAREN', 'RPAREN',
        'ID',
        ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID') #checking for reserved keywords
    return t

def try_get_value(token, base):
    try:
        return int(token, base)
    except ValueError:
        print("Integer value too large %s" % token)

def t_DEC(t):
    r'[1-9]\d*'
    t.value = try_get_value(t.value, 10)
    return t

def t_HEX(t):
    r'0x[\da-fA-F]+'
    t.value = try_get_value(t.value, 16)
    return t

def t_OCT(t):
    r'0o[0-7]+'
    t.value = try_get_value(t.value, 8)
    return t

def t_BIN(t):
    r'0b[01]+'
    t.value = try_get_value(t.value, 2)
    return t

#ignore whitespace
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal input '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#parsing rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    )

#dictionary of defined names
names = {}

def p_statement_format(t):
    '''statement : FORMAT_HEX expression
    | FORMAT_BIN expression'''
    f = format_functions[ t[1] ]
    print( f( t[2] ) )

def p_statement_assign(t):
    'statement : ID EQUALS expression'
    names[t[1]] = t[3]
    print(t[3])

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression'''
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_number(t):
    '''number : DEC 
    | HEX 
    | BIN'''
    t[0] = t[1]
    
def p_expression_number(t):
    'expression : number'
    t[0] = t[1]

def p_expression_name(t):
    'expression : ID'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error: '%s'" % t)

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
