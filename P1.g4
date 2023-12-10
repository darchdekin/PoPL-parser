grammar P1;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from P1Parser import P1Parser
}
@lexer::members {
class P1Denter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: P1Lexer = lexer

    def pull_token(self):
        return super(P1Lexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.P1Denter(self, self.NL, P1Parser.INDENT, P1Parser.DEDENT, False)
    return self.denter.next_token()
}


// Parser rules

start: line+ EOF;
block: INDENT line+ DEDENT ;

line: (assign_statement NL | conditional_statement);

// statements
assign_statement: VAR assign_operator value | VAR assign_operator athm_expr ;
conditional_statement: 'if ' conditional_value ':' block ('elif ' conditional_value ':' block)* ('else:' block)?;

// datatypes
int: '-'? DIGIT+;
bool: 'True' | 'False' ;
float: '-'? ( DIGIT+ '.' DIGIT* | '.' DIGIT+ ) ;
string:
	  ( '"' ( '\\"' | ~(NL | '"') )* '"' )		// Double-quote string
	| ( '\'' ( '\\\'' | ~(NL | '\'') )* '\'')		// Single-quote string
	;


literal: bool | int | float | string;
value: VAR | literal | '(' value ')' | list ;
list: '[' (value (',' value)*)? ']' ;

//operators
arith_operator: ( '+' | '-' | '*' | '/' | '%' ) ;
assign_operator: ( '=' | '+=' | '-=' | '*=' | '/=' ) ;

athm_expr: value (arith_operator value)+ ;
conditional_value: 'True' | 'False';

// Lexer rules

NL: ('\r'? '\n' ' '*) | ('\r'? '\n' '\t'*); //For tabs just switch out ' '* with '\t'*;
DIGIT:  [0-9] ;
VAR: 	([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')* ;
SPACE : ' '+ -> skip ;
BOOLEAN: 'True' | 'False';
