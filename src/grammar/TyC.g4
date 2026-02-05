grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: declarationList EOF;
declarationList: declarationList declaration | ;
declaration: structDecl | funcDecl;

structDecl: STRUCT ID LBRACE structMemberList RBRACE SEMI;
structMemberList: structMemberList structMember | ;
structMember: primitive ID SEMI;

funcDecl: returnType? ID LPAREN paramList RPAREN blockStmt;

paramList: paramListSub | ;
paramListSub: paramListSub COMMA param | param;
param: primitive ID;

primitive: INT | FLOAT | STRING | ID;
returnType: VOID | primitive;

statement: varDeclStmt | blockStmt | assignStmt | ifStmt | whileStmt | forStmt | switchStmt | breakStmt | continueStmt | returnStmt | exprStmt;

varDeclStmt: (AUTO | primitive) ID varInit SEMI;
varInit: ASSIGN expression | ;

blockStmt: LBRACE stmtList RBRACE;
stmtList: stmtList statement | ;

assignStmt: object ASSIGN expression SEMI;

object: object DOT ID | ID;

ifStmt: IF LPAREN expression RPAREN statement elseStmt?;
elseStmt: ELSE statement;
whileStmt: WHILE LPAREN expression RPAREN statement;
forStmt: FOR LPAREN forInit SEMI optExpr SEMI optExpr RPAREN statement;
forInit: (AUTO | primitive) ID varInit | expression | ;
optExpr: expression | ;
switchStmt: SWITCH LPAREN expression RPAREN LBRACE clauseList RBRACE;

clauseList: clauseList clause | ;
clause: (CASE expression | DEFAULT) COLON stmtList;

breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN optExpr SEMI;

exprStmt: expression SEMI;
expression: assignExpr;
assignExpr: object ASSIGN assignExpr | orExpr;
orExpr: andExpr orExprTail;
orExprTail: orExprTail OR andExpr | ;
andExpr: equalExpr andExprTail;
andExprTail: andExprTail AND equalExpr | ;
equalExpr: compareExpr equalExprTail;
equalExprTail: equalExprTail (EQ | NEQ) compareExpr | ;
compareExpr: addExpr compareExprTail;
compareExprTail: compareExprTail (LT | GT | LE | GE) addExpr | ;
addExpr: mulExpr addExprTail;
addExprTail: addExprTail (ADD | SUB) mulExpr | ;
mulExpr: unaryExpr mulExprTail;
mulExprTail: mulExprTail (MUL | DIV | MOD) unaryExpr | ;
unaryExpr: unaryOp unaryExpr | postfixExpr;
unaryOp: ADD | SUB | NOT | INC | DEC;

postfixExpr: primaryExpr postfixExprTail;
postfixExprTail: postfixExprTail postfixOp | ;
postfixOp: DOT ID | LPAREN argList RPAREN | INC | DEC;
primaryExpr: ID | INTLIT | FLOATLIT | STRINGLIT | LPAREN expression RPAREN | structInit;

structInit: LBRACE structInitList RBRACE;
structInitList: structInitListSub | ;
structInitListSub: structInitListSub COMMA expression | expression;

argList: argListSub | ;
argListSub: argListSub COMMA expression | expression;

//lexer

AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

EQ: '==';
NEQ: '!=';
LE: '<=';
GE: '>=';
AND: '&&';
OR: '||';
INC: '++';
DEC: '--';

LT: '<';
GT: '>';
NOT: '!';
ASSIGN: '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
DOT: '.';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COMMA: ',';
COLON: ':';

FLOATLIT: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?
    | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | [0-9]+ [eE] [+-]? [0-9]+;

INTLIT: [0-9]+;

ILLEGAL_ESCAPE: '"' (STRING_CHAR)* '\\' ~[bfrnt"\\\r\n] {self.text = self.text[1:]};

UNCLOSE_STRING: '"' (STRING_CHAR)* ([\r\n] | EOF) {self.text = self.text[1:]};

STRINGLIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};

fragment STRING_CHAR: ~["\r\n\\] | ESC_SEQ;

fragment ESC_SEQ: '\\' [bfrnt"\\];

ID: [a-zA-Z_][a-zA-Z0-9_]*;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

WS: [ \t\r\n\f]+ -> skip;

ERROR_CHAR: .;
