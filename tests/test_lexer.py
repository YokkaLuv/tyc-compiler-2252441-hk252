"""
Lexer test cases for TyC compiler
100 comprehensive test cases for lexical analysis
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

def test_keyword_struct():
    """11. Struct keyword and braces"""
    tokenizer = Tokenizer("struct Point { }")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,},<EOF>"


def test_keyword_while_loop():
    """12. While keyword with condition"""
    tokenizer = Tokenizer("while (i < 10)")
    assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),<EOF>"


def test_logical_and_operator():
    """13. Logical AND operator"""
    tokenizer = Tokenizer("a && b")
    assert tokenizer.get_tokens_as_string() == "a,&&,b,<EOF>"


def test_logical_or_operator():
    """14. Logical OR operator"""
    tokenizer = Tokenizer("x || y")
    assert tokenizer.get_tokens_as_string() == "x,||,y,<EOF>"


def test_increment_operator():
    """15. Increment operator"""
    tokenizer = Tokenizer("++i")
    assert tokenizer.get_tokens_as_string() == "++,i,<EOF>"


def test_decrement_operator():
    """16. Decrement operator"""
    tokenizer = Tokenizer("j--")
    assert tokenizer.get_tokens_as_string() == "j,--,<EOF>"


def test_float_exponent():
    """17. Float with exponent notation"""
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"


def test_string_with_escape_sequence():
    """18. String with escape sequence"""
    tokenizer = Tokenizer(r'"hello\nworld"')
    assert tokenizer.get_tokens_as_string() == r"hello\nworld,<EOF>"


def test_block_comment():
    """19. Block comment"""
    tokenizer = Tokenizer("/* This is a comment */ x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_member_access():
    """20. Member access operator"""
    tokenizer = Tokenizer("p.x = 5")
    assert tokenizer.get_tokens_as_string() == "p,.,x,=,5,<EOF>"


# ========== Additional Test Cases (21-100) ==========
def test_keyword_break():
    """21. Keyword break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"


def test_keyword_continue():
    """22. Keyword continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"


def test_keyword_return():
    """23. Keyword return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"


def test_keyword_if_else():
    """24. Keywords if and else"""
    tokenizer = Tokenizer("if else")
    assert tokenizer.get_tokens_as_string() == "if,else,<EOF>"


def test_keyword_for():
    """25. Keyword for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"


def test_keyword_switch_default():
    """26. Keywords switch and default"""
    tokenizer = Tokenizer("switch default")
    assert tokenizer.get_tokens_as_string() == "switch,default,<EOF>"


def test_operator_eq_neq():
    """27. Equality operators"""
    tokenizer = Tokenizer("a==b!=c")
    assert tokenizer.get_tokens_as_string() == "a,==,b,!=,c,<EOF>"


def test_operator_relational():
    """28. Relational operators"""
    tokenizer = Tokenizer("a<=b>=c")
    assert tokenizer.get_tokens_as_string() == "a,<=,b,>=,c,<EOF>"


def test_operator_not():
    """29. Logical NOT operator"""
    tokenizer = Tokenizer("!a")
    assert tokenizer.get_tokens_as_string() == "!,a,<EOF>"


def test_operator_mod():
    """30. Modulus operator"""
    tokenizer = Tokenizer("a%3")
    assert tokenizer.get_tokens_as_string() == "a,%,3,<EOF>"


def test_operator_add_sub():
    """31. Add and subtract operators"""
    tokenizer = Tokenizer("a+-b")
    assert tokenizer.get_tokens_as_string() == "a,+,-,b,<EOF>"


def test_operator_mul_div():
    """32. Multiply and divide operators"""
    tokenizer = Tokenizer("a*b/c")
    assert tokenizer.get_tokens_as_string() == "a,*,b,/,c,<EOF>"


def test_separator_parens():
    """33. Parenthesis separators"""
    tokenizer = Tokenizer("( )")
    assert tokenizer.get_tokens_as_string() == "(,),<EOF>"


def test_separator_braces():
    """34. Brace separators"""
    tokenizer = Tokenizer("{ }")
    assert tokenizer.get_tokens_as_string() == "{,},<EOF>"


def test_separator_comma_colon():
    """35. Comma and colon separators"""
    tokenizer = Tokenizer(", :")
    assert tokenizer.get_tokens_as_string() == ",,:,<EOF>"


def test_identifier_underscore():
    """36. Identifier with underscore"""
    tokenizer = Tokenizer("_var1")
    assert tokenizer.get_tokens_as_string() == "_var1,<EOF>"


def test_identifier_mixed():
    """37. Identifier mixed case"""
    tokenizer = Tokenizer("Abc_123")
    assert tokenizer.get_tokens_as_string() == "Abc_123,<EOF>"


def test_int_literal_zero():
    """38. Integer literal zero"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"


def test_int_literal_large():
    """39. Integer literal large"""
    tokenizer = Tokenizer("123456")
    assert tokenizer.get_tokens_as_string() == "123456,<EOF>"


def test_float_trailing_dot():
    """40. Float with trailing dot"""
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"


def test_float_leading_dot():
    """41. Float with leading dot"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"


def test_float_exponent():
    """42. Float with exponent"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"


def test_float_exponent_signed():
    """43. Float with signed exponent"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"


def test_string_empty():
    """44. Empty string literal"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"


def test_string_tab_escape():
    """45. String with tab escape"""
    tokenizer = Tokenizer(r'"a\t b"')
    assert tokenizer.get_tokens_as_string() == r"a\t b,<EOF>"


def test_string_quote_escape():
    """46. String with escaped quote"""
    tokenizer = Tokenizer(r'"\""')
    assert tokenizer.get_tokens_as_string() == r"\",<EOF>"


def test_string_backslash_escape():
    """47. String with escaped backslash"""
    tokenizer = Tokenizer(r'"\\"')
    assert tokenizer.get_tokens_as_string() == r"\\,<EOF>"


def test_illegal_escape():
    """48. Illegal escape in string"""
    tokenizer = Tokenizer(r'"\x"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\x"


def test_unclosed_string():
    """49. Unclosed string"""
    tokenizer = Tokenizer('"abc')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc"


def test_error_char():
    """50. Error character"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"


def test_line_comment_with_code():
    """51. Line comment with code"""
    tokenizer = Tokenizer("x//cmt\ny")
    assert tokenizer.get_tokens_as_string() == "x,y,<EOF>"


def test_block_comment_with_symbols():
    """52. Block comment with symbols"""
    tokenizer = Tokenizer("/* a + b */x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_mixed_comments():
    """53. Mixed comments"""
    tokenizer = Tokenizer("x/*c*/y//z")
    assert tokenizer.get_tokens_as_string() == "x,y,<EOF>"


def test_struct_decl_tokens():
    """54. Struct declaration tokens"""
    tokenizer = Tokenizer("struct S { int x; };")
    assert tokenizer.get_tokens_as_string() == "struct,S,{,int,x,;,},;,<EOF>"


def test_func_decl_tokens():
    """55. Function declaration tokens"""
    tokenizer = Tokenizer("void main(){}")
    assert tokenizer.get_tokens_as_string() == "void,main,(,),{,},<EOF>"


def test_var_decl_auto_no_init():
    """56. Auto variable without initialization"""
    tokenizer = Tokenizer("auto x;")
    assert tokenizer.get_tokens_as_string() == "auto,x,;,<EOF>"


def test_var_decl_typed_init():
    """57. Typed variable with initialization"""
    tokenizer = Tokenizer("int x=1;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,1,;,<EOF>"


def test_assignment_chain():
    """58. Assignment chain"""
    tokenizer = Tokenizer("a=b=c")
    assert tokenizer.get_tokens_as_string() == "a,=,b,=,c,<EOF>"


def test_member_access_chain():
    """59. Member access chain"""
    tokenizer = Tokenizer("a.b.c")
    assert tokenizer.get_tokens_as_string() == "a,.,b,.,c,<EOF>"


def test_function_call_no_args():
    """60. Function call with no args"""
    tokenizer = Tokenizer("foo()")
    assert tokenizer.get_tokens_as_string() == "foo,(,),<EOF>"


def test_function_call_args():
    """61. Function call with args"""
    tokenizer = Tokenizer("foo(1,2)")
    assert tokenizer.get_tokens_as_string() == "foo,(,1,,,2,),<EOF>"


def test_postfix_inc():
    """62. Postfix increment"""
    tokenizer = Tokenizer("x++")
    assert tokenizer.get_tokens_as_string() == "x,++,<EOF>"


def test_prefix_dec():
    """63. Prefix decrement"""
    tokenizer = Tokenizer("--x")
    assert tokenizer.get_tokens_as_string() == "--,x,<EOF>"


def test_unary_not():
    """64. Unary logical not"""
    tokenizer = Tokenizer("!flag")
    assert tokenizer.get_tokens_as_string() == "!,flag,<EOF>"


def test_logical_and_or():
    """65. Logical AND/OR"""
    tokenizer = Tokenizer("a&&b||c")
    assert tokenizer.get_tokens_as_string() == "a,&&,b,||,c,<EOF>"


def test_relational_expr():
    """66. Relational expression"""
    tokenizer = Tokenizer("a<b")
    assert tokenizer.get_tokens_as_string() == "a,<,b,<EOF>"


def test_equality_expr():
    """67. Equality expression"""
    tokenizer = Tokenizer("a==b")
    assert tokenizer.get_tokens_as_string() == "a,==,b,<EOF>"


def test_string_with_space():
    """68. String with space"""
    tokenizer = Tokenizer('"a b"')
    assert tokenizer.get_tokens_as_string() == "a b,<EOF>"


def test_struct_init_empty():
    """69. Empty struct initialization"""
    tokenizer = Tokenizer("{}")
    assert tokenizer.get_tokens_as_string() == "{,},<EOF>"


def test_struct_init_list():
    """70. Struct initialization list"""
    tokenizer = Tokenizer("{1,2}")
    assert tokenizer.get_tokens_as_string() == "{,1,,,2,},<EOF>"


def test_nested_struct_init():
    """71. Nested struct initialization"""
    tokenizer = Tokenizer("{{1,2},3}")
    assert tokenizer.get_tokens_as_string() == "{,{,1,,,2,},,,3,},<EOF>"


def test_for_loop_tokens():
    """72. For loop tokens"""
    tokenizer = Tokenizer("for(i=0;i<10;i++)")
    assert tokenizer.get_tokens_as_string() == "for,(,i,=,0,;,i,<,10,;,i,++,),<EOF>"


def test_if_else_tokens():
    """73. If-else tokens"""
    tokenizer = Tokenizer("if(x) y; else z;")
    assert tokenizer.get_tokens_as_string() == "if,(,x,),y,;,else,z,;,<EOF>"


def test_while_tokens():
    """74. While tokens"""
    tokenizer = Tokenizer("while(x){x++;}")
    assert tokenizer.get_tokens_as_string() == "while,(,x,),{,x,++,;,},<EOF>"


def test_switch_tokens():
    """75. Switch tokens"""
    tokenizer = Tokenizer("switch(x){case 1:break;default:}")
    assert tokenizer.get_tokens_as_string() == "switch,(,x,),{,case,1,:,break,;,default,:,},<EOF>"


def test_return_tokens():
    """76. Return statement tokens"""
    tokenizer = Tokenizer("return;")
    assert tokenizer.get_tokens_as_string() == "return,;,<EOF>"


def test_return_expr_tokens():
    """77. Return expression tokens"""
    tokenizer = Tokenizer("return x+1;")
    assert tokenizer.get_tokens_as_string() == "return,x,+,1,;,<EOF>"


def test_complex_expr_tokens():
    """78. Complex expression tokens"""
    tokenizer = Tokenizer("a*(b+c)-d/2")
    assert tokenizer.get_tokens_as_string() == "a,*,(,b,+,c,),-,d,/,2,<EOF>"


def test_string_formfeed_escape():
    """79. String with formfeed escape"""
    tokenizer = Tokenizer(r'"a\f"')
    assert tokenizer.get_tokens_as_string() == r"a\f,<EOF>"


def test_string_backspace_escape():
    """80. String with backspace escape"""
    tokenizer = Tokenizer(r'"a\b"')
    assert tokenizer.get_tokens_as_string() == r"a\b,<EOF>"


def test_string_carriage_escape():
    """81. String with carriage return escape"""
    tokenizer = Tokenizer(r'"a\r"')
    assert tokenizer.get_tokens_as_string() == r"a\r,<EOF>"


def test_float_exp_only():
    """82. Float exponent only"""
    tokenizer = Tokenizer("3e+8")
    assert tokenizer.get_tokens_as_string() == "3e+8,<EOF>"


def test_auto_struct_var():
    """83. Struct type name as identifier"""
    tokenizer = Tokenizer("Point p;")
    assert tokenizer.get_tokens_as_string() == "Point,p,;,<EOF>"


def test_member_vs_float():
    """84. Member access vs float"""
    tokenizer = Tokenizer("a.5")
    assert tokenizer.get_tokens_as_string() == "a,.5,<EOF>"


def test_negative_int():
    """85. Negative integer literal (unary minus)"""
    tokenizer = Tokenizer("-45")
    assert tokenizer.get_tokens_as_string() == "-,45,<EOF>"


def test_negative_float():
    """86. Negative float literal (unary minus)"""
    tokenizer = Tokenizer("-3.14")
    assert tokenizer.get_tokens_as_string() == "-,3.14,<EOF>"


def test_string_newline_escape():
    """87. String with newline escape"""
    tokenizer = Tokenizer(r'"a\n"')
    assert tokenizer.get_tokens_as_string() == r"a\n,<EOF>"


def test_float_with_exp_and_dot():
    """88. Float with dot and exponent"""
    tokenizer = Tokenizer("1.e2")
    assert tokenizer.get_tokens_as_string() == "1.e2,<EOF>"


def test_chained_calls_member():
    """89. Function call then member access"""
    tokenizer = Tokenizer("a().b")
    assert tokenizer.get_tokens_as_string() == "a,(,),.,b,<EOF>"


def test_struct_init_in_call():
    """90. Struct init as function argument"""
    tokenizer = Tokenizer("f({1,2})")
    assert tokenizer.get_tokens_as_string() == "f,(,{,1,,,2,},),<EOF>"


def test_increment_decrement_combo():
    """91. Increment and decrement combo"""
    tokenizer = Tokenizer("x++--")
    assert tokenizer.get_tokens_as_string() == "x,++,--,<EOF>"


def test_assignment_in_expr():
    """92. Assignment inside expression"""
    tokenizer = Tokenizer("a=b+1")
    assert tokenizer.get_tokens_as_string() == "a,=,b,+,1,<EOF>"


def test_comma_in_args():
    """93. Multiple arguments"""
    tokenizer = Tokenizer("foo(a,b,c)")
    assert tokenizer.get_tokens_as_string() == "foo,(,a,,,b,,,c,),<EOF>"


def test_colon_in_switch_case():
    """94. Colon in switch case"""
    tokenizer = Tokenizer("case 1:")
    assert tokenizer.get_tokens_as_string() == "case,1,:,<EOF>"


def test_nested_parens():
    """95. Nested parentheses"""
    tokenizer = Tokenizer("((x))")
    assert tokenizer.get_tokens_as_string() == "(,(,x,),),<EOF>"


def test_logical_not_paren():
    """96. Logical not with parentheses"""
    tokenizer = Tokenizer("!(a||b)")
    assert tokenizer.get_tokens_as_string() == "!,(,a,||,b,),<EOF>"


def test_multiple_dots():
    """97. Multiple dots"""
    tokenizer = Tokenizer("a.b.c.d")
    assert tokenizer.get_tokens_as_string() == "a,.,b,.,c,.,d,<EOF>"


def test_comment_after_code():
    """98. Comment after code"""
    tokenizer = Tokenizer("x; // comment")
    assert tokenizer.get_tokens_as_string() == "x,;,<EOF>"


def test_whitespace_mix():
    """99. Mixed whitespace"""
    tokenizer = Tokenizer("\t  \n  x  ")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_string_multiple_escapes():
    """100. String with multiple escapes"""
    tokenizer = Tokenizer(r'"a\t\n\r"')
    assert tokenizer.get_tokens_as_string() == r"a\t\n\r,<EOF>"


def test_long_program_tokens():
    """101. Long program with multiple structs and declarations"""
    source = """struct Point { int x; int y; };
struct Person { string name; int age; float height; };
void main() {
    Point p = {1,2};
    Person q = {"Bob", 30, 1.75};
    p.x = p.x + 1;
    if (p.x > 0) { printString(q.name); }
}"""
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == (
        "struct,Point,{,int,x,;,int,y,;,},;,"
        "struct,Person,{,string,name,;,int,age,;,float,height,;,},;,"
        "void,main,(,),{,"
        "Point,p,=,{,1,,,2,},;,"
        "Person,q,=,{,Bob,,,30,,,1.75,},;,"
        "p,.,x,=,p,.,x,+,1,;,"
        "if,(,p,.,x,>,0,),{,printString,(,q,.,name,),;,},"
        "},<EOF>"
    )
