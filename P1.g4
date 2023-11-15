grammar P1;

// Parser rules

start: NEWLINE* line (NEWLINE+ line)* NEWLINE* EOF;
line: assign_statement | if_statement;

// statements
assign_statement: VAR assign_operator value | VAR assign_operator athm_expr ;
if_statement: 'if ' bool_statement ':' NEWLINE* ('\t'line NEWLINE*)+ ('elif ' bool_statement ':' NEWLINE* ('\t'line NEWLINE*)+)* ('else:' NEWLINE* ('\t'line NEWLINE*)+)?;
bool_statement: bool_value | comparison | bool_statement (logic_operator bool_statement)+ | '(' bool_statement ')';
comparison: bool_value relat_operator bool_value;
bool_value: value | 'not ' value;

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
relat_operator: ( '<' | '>' | '>=' | '<=' | '==' | '!=') ;
logic_operator: ( 'and' | 'not' | 'or' ) ;

athm_expr: value (arith_operator value)+ ;


// Lexer rules


NEWLINE: ('\t')* ([\n\r]) ;
DIGIT:  [0-9] ;
VAR: 	([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')* ;
SPACE : ' '+ -> skip ;
