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

structMember: typeSpec ID SEMI;

funcDecl: (typeSpec | ) ID LPAREN paramList RPAREN blockStmt;

paramList: paramListNonEmpty | ;

paramListNonEmpty: paramListNonEmpty COMMA param | param;

param: typeSpec ID;

typeSpec: INT | FLOAT | STRING | ID;

statement: varDeclStmt | blockStmt | assignStmt | ifStmt | whileStmt | forStmt | switchStmt | breakStmt | continueStmt | returnStmt | exprStmt;

varDeclStmt: (AUTO | typeSpec) ID varInit SEMI;

varInit: ASSIGN expression | ;

blockStmt: LBRACE statementList RBRACE;

statementList: statementList statement | ;

assignStmt: lvalue ASSIGN expression SEMI;

lvalue: lvalue DOT ID | ID;

ifStmt: IF LPAREN expression RPAREN statement elseOpt;

elseOpt: ELSE statement | ;

whileStmt: WHILE LPAREN expression RPAREN statement;

forStmt: FOR LPAREN forInit SEMI forCond SEMI forUpdate RPAREN statement;

forInit: (AUTO | typeSpec) ID varInit | expression | ;

forCond: expression | ;

forUpdate: expression | ;

switchStmt: SWITCH LPAREN expression RPAREN LBRACE caseClauseList RBRACE;

caseClauseList: caseClauseList caseClause | ;

caseClause: (CASE expression | DEFAULT) COLON statementList;

breakStmt: BREAK SEMI;

continueStmt: CONTINUE SEMI;

returnStmt: RETURN returnExpr SEMI;

returnExpr: expression | ;

exprStmt: expression SEMI;

expression: assignExpr;

assignExpr: lvalue ASSIGN assignExpr | logicalOrExpr;

logicalOrExpr: logicalAndExpr logicalOrExprTail;

logicalOrExprTail: logicalOrExprTail OR logicalAndExpr | ;

logicalAndExpr: equalityExpr logicalAndExprTail;

logicalAndExprTail: logicalAndExprTail AND equalityExpr | ;

equalityExpr: relationalExpr equalityExprTail;

equalityExprTail: equalityExprTail (EQ | NEQ) relationalExpr | ;

relationalExpr: additiveExpr relationalExprTail;

relationalExprTail: relationalExprTail (LT | GT | LE | GE) additiveExpr | ;

additiveExpr: multiplicativeExpr additiveExprTail;

additiveExprTail: additiveExprTail (ADD | SUB) multiplicativeExpr | ;

multiplicativeExpr: unaryExpr multiplicativeExprTail;

multiplicativeExprTail: multiplicativeExprTail (MUL | DIV | MOD) unaryExpr | ;

unaryExpr: unaryOp unaryExpr | postfixExpr;

unaryOp: ADD | SUB | NOT | INC | DEC;

postfixExpr: primaryExpr postfixExprTail;

postfixExprTail: postfixExprTail postfixOp | ;

postfixOp: DOT ID | LPAREN argList RPAREN | INC | DEC;

primaryExpr: ID | INTLIT | FLOATLIT | STRINGLIT | LPAREN expression RPAREN | structInit;

structInit: LBRACE structInitList RBRACE;

structInitList: structInitListNonEmpty | ;

structInitListNonEmpty: structInitListNonEmpty COMMA expression | expression;

argList: argListNonEmpty | ;

argListNonEmpty: argListNonEmpty COMMA expression | expression;

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
