//Grammar for State language. A state machine that compiles to Solidity

grammar State;

/* PARSER */

contract: machine (address)* (st)* start;

machine: MACHINE ID;

address: ADDRESS ID ASSIGN HEXADDR;

st : ST ID OPENBRACE (transition)* CLOSEBRACE;

transition : TRANSITION ID REQUIRES disjunction;

disjunction : (conjunction)(OR conjunction)* ;

conjunction : (ID)(COMMA ID)* ;

start : START ASSIGN ID ;

/* LEXER */

MACHINE : 'Machine';

ADDRESS : 'address';

ASSIGN : '=';

HEXADDR : '0x' [0-9a-fA-F]+ ;

ST : 'state';

OPENBRACE : '{';

CLOSEBRACE : '}';

COMMA : ',';

OR : 'or';

TRANSITION : 'transition';

REQUIRES : 'requires';

START : 'start';

ID : [a-zA-Z_]+ ;

WHITESPACE : [ \t\r\n]+ -> skip ;