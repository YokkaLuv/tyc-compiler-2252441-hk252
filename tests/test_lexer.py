"""
Lexer test cases for TyC compiler
100 comprehensive test cases for lexical analysis
"""

import pytest
from tests.utils import Tokenizer


def test_001():
    """Test single integer literal"""
    source = "0"
    expected = "INTLIT,0,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_002():
    """Test multiple integer literals"""
    source = "100 255 2500"
    expected = "INTLIT,100,INTLIT,255,INTLIT,2500,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_003():
    """Test float literal with decimal point"""
    source = "0.0"
    expected = "FLOATLIT,0.0,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_004():
    """Test float literals in various formats"""
    source = "3.14 1.23e4 5.67E-2"
    expected = "FLOATLIT,3.14,FLOATLIT,1.23e4,FLOATLIT,5.67E-2,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_005():
    """Test float literal with only decimal point"""
    source = "1."
    expected = "FLOATLIT,1.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_006():
    """Test float literal with only fractional part"""
    source = ".5"
    expected = "FLOATLIT,.5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_007():
    """Test string literal simple"""
    source = '"hello"'
    expected = 'STRINGLIT,hello,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_008():
    """Test empty string literal"""
    source = '""'
    expected = 'STRINGLIT,,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009():
    """Test string with escape sequence"""
    source = r'"hello\n"'
    expected = r'STRINGLIT,hello\n,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_010():
    """Test line comment is skipped"""
    source = "auto x = 5; // comment here"
    expected = "AUTO,auto,ID,x,ASSIGN,=,INTLIT,5,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_011():
    """Test block comment is skipped"""
    source = "auto /* comment */ x = 5;"
    expected = "AUTO,auto,ID,x,ASSIGN,=,INTLIT,5,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_012():
    """Test multiline block comment is skipped"""
    source = "auto /* comment\nline2 */ x"
    expected = "AUTO,auto,ID,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_013():
    """Test keyword auto"""
    source = "auto"
    expected = "AUTO,auto,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_014():
    """Test keyword break"""
    source = "break"
    expected = "BREAK,break,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_015():
    """Test keyword case"""
    source = "case"
    expected = "CASE,case,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_016():
    """Test keyword continue"""
    source = "continue"
    expected = "CONTINUE,continue,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_017():
    """Test keyword default"""
    source = "default"
    expected = "DEFAULT,default,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_018():
    """Test keyword else"""
    source = "else"
    expected = "ELSE,else,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_019():
    """Test keyword float"""
    source = "float"
    expected = "FLOAT,float,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_020():
    """Test keyword for"""
    source = "for"
    expected = "FOR,for,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_021():
    """Test keyword if"""
    source = "if"
    expected = "IF,if,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_022():
    """Test keyword int"""
    source = "int"
    expected = "INT,int,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_023():
    """Test keyword return"""
    source = "return"
    expected = "RETURN,return,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_024():
    """Test keyword string"""
    source = "string"
    expected = "STRING,string,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_025():
    """Test keyword struct"""
    source = "struct"
    expected = "STRUCT,struct,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_026():
    """Test keyword switch"""
    source = "switch"
    expected = "SWITCH,switch,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_027():
    """Test keyword void"""
    source = "void"
    expected = "VOID,void,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_028():
    """Test keyword while"""
    source = "while"
    expected = "WHILE,while,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_029():
    """Test simple identifier"""
    source = "x"
    expected = "ID,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_030():
    """Test identifier with underscore"""
    source = "_private"
    expected = "ID,_private,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_031():
    """Test identifier with digits"""
    source = "var123"
    expected = "ID,var123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_032():
    """Test case-sensitive identifiers"""
    source = "MyVar myvar"
    expected = "ID,MyVar,ID,myvar,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_033():
    """Test operator plus"""
    source = "+"
    expected = "ADD,+,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_034():
    """Test operator minus"""
    source = "-"
    expected = "SUB,-,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_035():
    """Test operator multiply"""
    source = "*"
    expected = "MUL,*,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_036():
    """Test operator divide"""
    source = "/"
    expected = "DIV,/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_037():
    """Test operator modulo"""
    source = "%"
    expected = "MOD,%,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_038():
    """Test operator equal"""
    source = "=="
    expected = "EQ,==,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_039():
    """Test operator not equal"""
    source = "!="
    expected = "NEQ,!=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_040():
    """Test operator less than"""
    source = "<"
    expected = "LT,<,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_041():
    """Test operator greater than"""
    source = ">"
    expected = "GT,>,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_042():
    """Test operator less than or equal"""
    source = "<="
    expected = "LE,<=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_043():
    """Test operator greater than or equal"""
    source = ">="
    expected = "GE,>=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_044():
    """Test operator logical AND"""
    source = "&&"
    expected = "AND,&&,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_045():
    """Test operator logical OR"""
    source = "||"
    expected = "OR,||,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_046():
    """Test operator logical NOT"""
    source = "!"
    expected = "NOT,!,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_047():
    """Test operator increment"""
    source = "++"
    expected = "INC,++,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_048():
    """Test operator decrement"""
    source = "--"
    expected = "DEC,--,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_049():
    """Test operator assignment"""
    source = "="
    expected = "ASSIGN,=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_050():
    """Test operator member access"""
    source = "."
    expected = "DOT,.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_051():
    """Test separator left paren"""
    source = "("
    expected = "LPAREN,(,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_052():
    """Test separator right paren"""
    source = ")"
    expected = "RPAREN,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_053():
    """Test separator left brace"""
    source = "{"
    expected = "LBRACE,{,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_054():
    """Test separator right brace"""
    source = "}"
    expected = "RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_055():
    """Test separator semicolon"""
    source = ";"
    expected = "SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_056():
    """Test separator comma"""
    source = ","
    expected = "COMMA,,,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_057():
    """Test separator colon"""
    source = ":"
    expected = "COLON,:,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_058():
    """Test simple function declaration"""
    source = "void main() { }"
    expected = "VOID,void,ID,main,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_059():
    """Test struct declaration"""
    source = "struct Point { int x; }"
    expected = "STRUCT,struct,ID,Point,LBRACE,{,INT,int,ID,x,SEMI,;,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_060():
    """Test variable declaration"""
    source = "auto x = 10;"
    expected = "AUTO,auto,ID,x,ASSIGN,=,INTLIT,10,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_061():
    """Test if statement"""
    source = "if (x > 5) { }"
    expected = "IF,if,LPAREN,(,ID,x,GT,>,INTLIT,5,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_062():
    """Test while loop"""
    source = "while (i < 10) { }"
    expected = "WHILE,while,LPAREN,(,ID,i,LT,<,INTLIT,10,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_063():
    """Test for loop"""
    source = "for (int i = 0; i < 10; ++i) { }"
    expected = "FOR,for,LPAREN,(,INT,int,ID,i,ASSIGN,=,INTLIT,0,SEMI,;,ID,i,LT,<,INTLIT,10,SEMI,;,INC,++,ID,i,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_064():
    """Test switch statement"""
    source = "switch (x) { case 1: break; }"
    expected = "SWITCH,switch,LPAREN,(,ID,x,RPAREN,),LBRACE,{,CASE,case,INTLIT,1,COLON,:,BREAK,break,SEMI,;,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_065():
    """Test return statement"""
    source = "return x + 5;"
    expected = "RETURN,return,ID,x,ADD,+,INTLIT,5,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_066():
    """Test break statement"""
    source = "break;"
    expected = "BREAK,break,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_067():
    """Test continue statement"""
    source = "continue;"
    expected = "CONTINUE,continue,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_068():
    """Test arithmetic expression"""
    source = "x + y * z"
    expected = "ID,x,ADD,+,ID,y,MUL,*,ID,z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_069():
    """Test comparison expression"""
    source = "a == b && c != d"
    expected = "ID,a,EQ,==,ID,b,AND,&&,ID,c,NEQ,!=,ID,d,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_070():
    """Test member access"""
    source = "obj.field"
    expected = "ID,obj,DOT,.,ID,field,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_071():
    """Test function call"""
    source = "func(a, b, c)"
    expected = "ID,func,LPAREN,(,ID,a,COMMA,,,ID,b,COMMA,,,ID,c,RPAREN,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_072():
    """Test negative integer literal"""
    source = "-42"
    expected = "INTLIT,-42,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_073():
    """Test negative float literal"""
    source = "-3.14"
    expected = "FLOATLIT,-3.14,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_074():
    """Test whitespace is ignored"""
    source = "a   b    c"
    expected = "ID,a,ID,b,ID,c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_075():
    """Test tabs and newlines are ignored"""
    source = "a\tb\nc"
    expected = "ID,a,ID,b,ID,c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_076():
    """Test multiple operators"""
    source = "x++ + y--"
    expected = "ID,x,INC,++,ADD,+,ID,y,DEC,--,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_077():
    """Test string with spaces"""
    source = '"hello world"'
    expected = 'STRINGLIT,hello world,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_078():
    """Test string with tab escape"""
    source = r'"hello\tworld"'
    expected = r'STRINGLIT,hello\tworld,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_079():
    """Test string with quote escape"""
    source = r'"say \"hello\""'
    expected = r'STRINGLIT,say \"hello\",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_080():
    """Test string with backslash escape"""
    source = r'"path\\to\\file"'
    expected = r'STRINGLIT,path\\to\\file,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_081():
    """Test float with e notation lowercase"""
    source = "1e5"
    expected = "FLOATLIT,1e5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_082():
    """Test float with E notation uppercase"""
    source = "1E5"
    expected = "FLOATLIT,1E5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_083():
    """Test float with positive exponent"""
    source = "1e+5"
    expected = "FLOATLIT,1e+5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_084():
    """Test float with negative exponent"""
    source = "1e-5"
    expected = "FLOATLIT,1e-5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_085():
    """Test complex expression"""
    source = "(a + b) * (c - d)"
    expected = "LPAREN,(,ID,a,ADD,+,ID,b,RPAREN,),MUL,*,LPAREN,(,ID,c,SUB,-,ID,d,RPAREN,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_086():
    """Test assignment"""
    source = "x = y = z"
    expected = "ID,x,ASSIGN,=,ID,y,ASSIGN,=,ID,z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_087():
    """Test logical NOT"""
    source = "!flag"
    expected = "NOT,!,ID,flag,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_088():
    """Test unary minus"""
    source = "-x"
    expected = "SUB,-,ID,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_089():
    """Test unary plus"""
    source = "+y"
    expected = "ADD,+,ID,y,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_090():
    """Test struct initialization"""
    source = "Point p = {10, 20};"
    expected = "ID,Point,ID,p,ASSIGN,=,LBRACE,{,INTLIT,10,COMMA,,,INTLIT,20,RBRACE,},SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected
