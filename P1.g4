grammar P1;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from MyCoolParser import MyCoolParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: MyCoolLexer = lexer

    def pull_token(self):
        return super(MyCoolLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NL, MyCoolParser.INDENT, MyCoolParser.DEDENT, ***Should Ignore EOF***)
    return self.denter.next_token()

}


// Parser rules

start: NEWLINE* line (NL* line)* NEWLINE* EOF;
line: assign_statement NEWLINE | conditional_statement NEWLINE;
block: INDENT (line NL)+ DEDENT;

// statements
assign_statement: VAR assign_operator value | VAR assign_operator athm_expr ;
conditional_statement: 'if ' conditional_value ':' block ('elif ' conditional_value ':' block)* ('else:' block)?;

// datatypes
int: '-'? DIGIT+;
bool: 'True' | 'False' ;
float: '-'? ( DIGIT+ '.' DIGIT* | '.' DIGIT+ ) ;
string:
	  ( '"' ( '\\"' | ~(NEWLINE | '"') )* '"' )		// Double-quote string
	| ( '\'' ( '\\\'' | ~(NEWLINE | '\'') )* '\'')		// Single-quote string
	;


literal: bool | int | float | string;
value: VAR | literal | '(' value ')' | list ;
list: '[' (value (',' value)*)? ']' ;

//operators
arith_operator: ( '+' | '-' | '*' | '/' | '%' ) ;
assign_operator: ( '=' | '+=' | '-=' | '*=' | '/=' ) ;

athm_expr: value (arith_operator value)+ ;
conditional_value: 'true' | 'false';

// Lexer rules

NEWLINE: [\n\r] ;
DIGIT:  [0-9] ;
VAR: 	([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')* ;
SPACE : ' '+ -> skip ;
BOOLEAN: 'true' | 'false';
NL: ('\r'? '\n' ' '*) | ('\r'? '\n' '\t'*); //For tabs just switch out ' '* with '\t'*;
