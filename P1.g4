grammar P1;

// Parser rules

start: NEWLINE* line (NEWLINE+ line)* NEWLINE* EOF;
line: assign_statement;

// statements
assign_statement: VAR assign_operator value | VAR assign_operator athm_expr ;

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


// Lexer rules

NEWLINE: [\n\r] ;
DIGIT:  [0-9] ;
VAR: 	([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')* ;
SPACE : ' '+ -> skip ;