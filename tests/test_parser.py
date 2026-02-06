"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"


# ========== Additional Test Cases (11-100) ==========
def test_function_inferred_return():
    """11. Function with inferred return type"""
    source = "add(int a, int b) { return a + b; }"
    assert Parser(source).parse() == "success"


def test_empty_struct():
    """12. Empty struct declaration"""
    source = "struct Empty { };"
    assert Parser(source).parse() == "success"


def test_struct_member_struct():
    """13. Struct with struct-typed member"""
    source = "struct A { int x; }; struct B { A a; };"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_no_init():
    """14. Auto variable without init"""
    source = "void main() { auto x; }"
    assert Parser(source).parse() == "success"


def test_var_decl_typed_no_init():
    """15. Typed variables without init"""
    source = "void main() { int x; float y; string s; }"
    assert Parser(source).parse() == "success"


def test_var_decl_struct():
    """16. Struct variable declaration"""
    source = "struct P { int x; }; void main() { P p; }"
    assert Parser(source).parse() == "success"


def test_struct_init_simple():
    """17. Struct initialization"""
    source = "struct P { int x; int y; }; void main() { P p = {1,2}; }"
    assert Parser(source).parse() == "success"


def test_struct_init_empty():
    """18. Empty struct initialization"""
    source = "struct E { }; void main() { E e = { }; }"
    assert Parser(source).parse() == "success"


def test_struct_init_nested():
    """19. Nested struct initialization"""
    source = "struct P { int x; int y; }; struct Q { P p; int z; }; void main() { Q q = {{1,2},3}; }"
    assert Parser(source).parse() == "success"


def test_assignment_member():
    """20. Member assignment"""
    source = "struct P { int x; }; void main() { P p; p.x = 1; }"
    assert Parser(source).parse() == "success"


def test_assignment_chain_expr():
    """21. Assignment chain"""
    source = "void main() { int a; int b; int c; a = b = c; }"
    assert Parser(source).parse() == "success"


def test_expression_statement():
    """22. Expression statement"""
    source = "void main() { 1 + 2; }"
    assert Parser(source).parse() == "success"


def test_function_call_statement():
    """23. Function call statement"""
    source = "void main() { printInt(1); }"
    assert Parser(source).parse() == "success"


def test_if_else_block():
    """24. If-else with blocks"""
    source = "void main() { if (1) { printInt(1); } else { printInt(0); } }"
    assert Parser(source).parse() == "success"


def test_nested_if():
    """25. Nested if without braces"""
    source = "void main() { if (1) if (0) printInt(0); else printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_block():
    """26. While with block"""
    source = "void main() { while (1) { break; } }"
    assert Parser(source).parse() == "success"


def test_for_no_init():
    """27. For without init"""
    source = "void main() { for (; 1; ) break; }"
    assert Parser(source).parse() == "success"


def test_for_no_cond():
    """28. For without condition"""
    source = "void main() { for (auto i = 0; ; i = i + 1) { if (i) break; } }"
    assert Parser(source).parse() == "success"


def test_for_no_update():
    """29. For without update"""
    source = "void main() { for (auto i = 0; i < 10; ) i = i + 1; }"
    assert Parser(source).parse() == "success"


def test_for_all_empty():
    """30. For with all empty"""
    source = "void main() { for (;;) { break; } }"
    assert Parser(source).parse() == "success"


def test_switch_empty():
    """31. Empty switch"""
    source = "void main() { switch (1) { } }"
    assert Parser(source).parse() == "success"


def test_switch_default_only():
    """32. Switch with default only"""
    source = "void main() { switch (1) { default: } }"
    assert Parser(source).parse() == "success"


def test_switch_multiple_cases():
    """33. Switch with multiple cases"""
    source = "void main() { switch (1) { case 1: break; case 2: break; default: break; } }"
    assert Parser(source).parse() == "success"


def test_switch_case_empty_stmtlist():
    """34. Switch case with empty statement list"""
    source = "void main() { switch (1) { case 1: } }"
    assert Parser(source).parse() == "success"


def test_switch_case_expr():
    """35. Switch case with expression"""
    source = "void main() { switch (1) { case 1+2: break; } }"
    assert Parser(source).parse() == "success"


def test_return_no_expr():
    """36. Return without expression"""
    source = "void main() { return; }"
    assert Parser(source).parse() == "success"


def test_return_with_expr():
    """37. Return with expression"""
    source = "int f() { return 1; }"
    assert Parser(source).parse() == "success"


def test_return_inferred():
    """38. Return with inferred type"""
    source = "f() { return 1; }"
    assert Parser(source).parse() == "success"


def test_return_multiple():
    """39. Multiple return statements"""
    source = "int f() { return 1; return 2; }"
    assert Parser(source).parse() == "success"


def test_postfix_inc():
    """40. Postfix increment"""
    source = "void main() { int x; x++; }"
    assert Parser(source).parse() == "success"


def test_prefix_dec():
    """41. Prefix decrement"""
    source = "void main() { int x; --x; }"
    assert Parser(source).parse() == "success"


def test_unary_not():
    """42. Unary not expression"""
    source = "void main() { int x; !x; }"
    assert Parser(source).parse() == "success"


def test_logical_and_or():
    """43. Logical and/or expression"""
    source = "void main() { int x; x = 1 && 0 || 1; }"
    assert Parser(source).parse() == "success"


def test_relational_eq():
    """44. Relational and equality expressions"""
    source = "void main() { int x; x = 1 < 2; x = 3 == 4; }"
    assert Parser(source).parse() == "success"


def test_arith_precedence():
    """45. Arithmetic precedence"""
    source = "void main() { int x; x = 1 + 2 * 3; }"
    assert Parser(source).parse() == "success"


def test_paren_expr():
    """46. Parenthesized expression"""
    source = "void main() { int x; x = (1 + 2) * 3; }"
    assert Parser(source).parse() == "success"


def test_nested_member_access():
    """47. Nested member access"""
    source = "struct P { int x; }; struct Q { P p; }; void main() { Q q; q.p.x = 1; }"
    assert Parser(source).parse() == "success"


def test_function_call_args():
    """48. Function call with args"""
    source = "int add(int a, int b) { return a + b; } void main() { auto x = add(1,2); }"
    assert Parser(source).parse() == "success"


def test_function_call_struct_arg():
    """49. Function call with struct literal"""
    source = "struct P { int x; }; void f(P p) { } void main() { f({1}); }"
    assert Parser(source).parse() == "success"


def test_block_empty():
    """50. Empty block statement"""
    source = "void main() { { } }"
    assert Parser(source).parse() == "success"


def test_block_with_decls():
    """51. Block with declarations"""
    source = "void main() { { int x; x = 1; } }"
    assert Parser(source).parse() == "success"


def test_multiple_functions():
    """52. Multiple functions"""
    source = "int f() { return 1; } void g() { return; }"
    assert Parser(source).parse() == "success"


def test_struct_and_func_mix():
    """53. Struct and function mix"""
    source = "struct P { int x; }; int f() { return 1; }"
    assert Parser(source).parse() == "success"


def test_assignment_in_expr():
    """54. Assignment inside expression"""
    source = "void main() { int x; int y; y = (x = 1) + 2; }"
    assert Parser(source).parse() == "success"


def test_chained_calls():
    """55. Chained calls"""
    source = "int f() { return 1; } int g(int a) { return a; } void main() { g(f()); }"
    assert Parser(source).parse() == "success"


def test_expression_in_for_init():
    """56. For init as expression"""
    source = "void main() { int i; for (i = 0; i < 3; i = i + 1) { } }"
    assert Parser(source).parse() == "success"


def test_expression_in_for_update():
    """57. For update expression"""
    source = "void main() { int i; for (; i < 3; i = i + 1) { } }"
    assert Parser(source).parse() == "success"


def test_switch_case_parenthesized():
    """58. Parenthesized case expression"""
    source = "void main() { switch (1) { case (1): break; } }"
    assert Parser(source).parse() == "success"


def test_switch_case_unary():
    """59. Unary case expressions"""
    source = "void main() { switch (1) { case -1: break; case +2: break; } }"
    assert Parser(source).parse() == "success"


def test_case_fallthrough():
    """60. Switch fallthrough"""
    source = "void main() { switch (1) { case 1: case 2: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_case_with_block():
    """61. Case with block statement"""
    source = "void main() { switch (1) { case 1: { } } }"
    assert Parser(source).parse() == "success"


def test_empty_statement_list_in_block():
    """62. Multiple empty blocks"""
    source = "void main() { { } { } }"
    assert Parser(source).parse() == "success"


def test_if_without_else():
    """63. If without else"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_single_stmt():
    """64. While with single statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_single_stmt():
    """65. For with single statement"""
    source = "void main() { for (auto i = 0; i < 1; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_return_in_void_function():
    """66. Return in void function"""
    source = "void main() { return; return; }"
    assert Parser(source).parse() == "success"


def test_return_in_inferred_void_function():
    """67. Return in inferred void function"""
    source = "main() { return; }"
    assert Parser(source).parse() == "success"


def test_auto_without_init_then_assign():
    """68. Auto without init then assign"""
    source = "void main() { auto x; x = 1; }"
    assert Parser(source).parse() == "success"


def test_struct_assignment():
    """69. Struct assignment"""
    source = "struct P { int x; int y; }; void main() { P a; P b; a = b; }"
    assert Parser(source).parse() == "success"


def test_struct_member_read():
    """70. Struct member read"""
    source = "struct P { int x; }; void main() { P p; int x; x = p.x; }"
    assert Parser(source).parse() == "success"


def test_call_chain():
    """71. Call chain"""
    source = "void main() { foo(1)(2); }"
    assert Parser(source).parse() == "success"


def test_multiple_var_decls():
    """72. Multiple variable declarations"""
    source = "void main() { int a; float b; string c; }"
    assert Parser(source).parse() == "success"


def test_nested_blocks():
    """73. Nested blocks"""
    source = "void main() { { { int x; } } }"
    assert Parser(source).parse() == "success"


def test_continue_in_loop():
    """74. Continue in loop"""
    source = "void main() { while (1) { continue; } }"
    assert Parser(source).parse() == "success"


def test_break_in_loop():
    """75. Break in loop"""
    source = "void main() { while (1) { if (1) break; } }"
    assert Parser(source).parse() == "success"


def test_break_in_switch():
    """76. Break in switch"""
    source = "void main() { switch (1) { case 1: break; default: break; } }"
    assert Parser(source).parse() == "success"


def test_complex_expression():
    """77. Complex arithmetic expression"""
    source = "void main() { int x; x = (1 + 2) * (3 - 4) / 5; }"
    assert Parser(source).parse() == "success"


def test_logical_not_with_paren():
    """78. Logical not with parentheses"""
    source = "void main() { int x; x = !(1 < 2); }"
    assert Parser(source).parse() == "success"


def test_inc_dec_in_expr():
    """79. Increment/decrement in expression"""
    source = "void main() { int x; x = ++x + x--; }"
    assert Parser(source).parse() == "success"


def test_mod_operator():
    """80. Mod operator"""
    source = "void main() { int x; x = 10 % 3; }"
    assert Parser(source).parse() == "success"


def test_relational_chain():
    """81. Relational chain"""
    source = "void main() { int x; x = 1 < 2 < 3; }"
    assert Parser(source).parse() == "success"


def test_equality_chain():
    """82. Equality chain"""
    source = "void main() { int x; x = 1 == 2 == 3; }"
    assert Parser(source).parse() == "success"


def test_assignment_with_member():
    """83. Assignment with member access"""
    source = "struct P { int x; }; void main() { P p; p.x = 1; p.x = p.x + 1; }"
    assert Parser(source).parse() == "success"


def test_struct_init_in_assignment():
    """84. Struct init in assignment"""
    source = "struct P { int x; int y; }; void main() { P p; p = {1,2}; }"
    assert Parser(source).parse() == "success"


def test_function_with_params():
    """85. Function with multiple params"""
    source = "int sum(int a, int b, int c) { return a + b + c; }"
    assert Parser(source).parse() == "success"


def test_function_with_struct_param():
    """86. Function with struct param"""
    source = "struct P { int x; }; void f(P p) { return; }"
    assert Parser(source).parse() == "success"


def test_call_with_struct_init():
    """87. Call with struct init"""
    source = "struct P { int x; }; void main() { P p; p = {1}; printInt(p.x); }"
    assert Parser(source).parse() == "success"


def test_for_with_assignment_init():
    """88. For with assignment init"""
    source = "void main() { int i; for (i = 0; i < 10; i = i + 1) { } }"
    assert Parser(source).parse() == "success"


def test_for_with_assignment_update():
    """89. For with assignment update"""
    source = "void main() { int i; for (i = 0; i < 10; ++i) { } }"
    assert Parser(source).parse() == "success"


def test_switch_with_default_middle():
    """90. Switch with default in middle"""
    source = "void main() { switch (1) { case 0: break; default: break; case 2: break; } }"
    assert Parser(source).parse() == "success"


def test_complex_program():
    """91. Complex program"""
    source = """struct Point { int x; int y; };
struct Person { string name; int age; float height; };
int add(int a, int b) { return a + b; }
void main() {
    Point p = {1,2};
    Person q = {"Bob", 30, 1.75};
    p.x = add(p.x, 1);
    if (p.x > 0) { printString(q.name); }
}"""
    assert Parser(source).parse() == "success"


def test_empty_block_in_function():
    """92. Empty block in function"""
    source = "void main() { { } }"
    assert Parser(source).parse() == "success"


def test_nested_struct_access():
    """93. Nested struct access"""
    source = "struct P { int x; }; struct Q { P p; }; void main() { Q q; int a; a = q.p.x; }"
    assert Parser(source).parse() == "success"


def test_function_call_nested_args():
    """94. Function call with nested args"""
    source = "int f(int a) { return a; } void main() { int x; x = f(f(1)); }"
    assert Parser(source).parse() == "success"


def test_expression_statement_member_inc():
    """95. Member postfix increment"""
    source = "struct P { int x; }; void main() { P p; p.x++; }"
    assert Parser(source).parse() == "success"


def test_struct_literal_in_expression():
    """96. Struct literal in expression"""
    source = "struct P { int x; int y; }; void main() { P p; p = {1,2}; }"
    assert Parser(source).parse() == "success"


def test_for_with_expression_init_only():
    """97. For with expression init only"""
    source = "void main() { int i; for (i = 0; ; ) { break; } }"
    assert Parser(source).parse() == "success"


def test_switch_case_unary_plus_minus():
    """98. Switch case unary plus/minus"""
    source = "void main() { switch (1) { case +1: break; case -2: break; } }"
    assert Parser(source).parse() == "success"


def test_nested_blocks_with_statements():
    """99. Nested blocks with statements"""
    source = "void main() { { int x; x = 1; { x = x + 1; } } }"
    assert Parser(source).parse() == "success"


def test_multiple_declarations_program():
    """100. Multiple declarations program"""
    source = "struct A { int x; }; struct B { float y; }; void main() { A a; B b; }"
    assert Parser(source).parse() == "success"


def test_adjacent_int_literals_expr():
    """111. Adjacent integer literals expression"""
    source = "void main() { 10 -3; }"
    assert Parser(source).parse() == "success"


def test_adjacent_float_literals_expr():
    """112. Adjacent float literals expression"""
    source = "void main() { 1.5 -2.25; }"
    assert Parser(source).parse() == "success"


def test_adjacent_mixed_literals_expr():
    """113. Adjacent mixed numeric literals expression"""
    source = "void main() { 2 -3.0; }"
    assert Parser(source).parse() == "success"


def test_adjacent_literals_in_assignment():
    """114. Adjacent literals in assignment"""
    source = "void main() { int x; x = 10 -3; }"
    assert Parser(source).parse() == "success"


def test_adjacent_literals_in_return():
    """115. Adjacent literals in return"""
    source = "int f() { return 10 -3; }"
    assert Parser(source).parse() == "success"


# ========== Negative Test Cases (Syntax Errors) ==========
def test_missing_semi_in_var_decl():
    """101. Missing semicolon in variable declaration"""
    source = "void main() { int x }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_missing_semi_in_return():
    """102. Missing semicolon in return"""
    source = "void main() { return }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_missing_semi_in_expr_stmt():
    """103. Missing semicolon in expression statement"""
    source = "void main() { x = 1 }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_invalid_for_syntax():
    """104. Invalid for syntax (missing semicolon)"""
    source = "void main() { for (i = 0 i < 10; i++) { } }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_struct_member_missing_semi():
    """105. Struct member missing semicolon"""
    source = "struct A { int x };"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_param_missing_type():
    """106. Function parameter missing type"""
    source = "int f(x) { return 1; }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_switch_case_missing_colon():
    """107. Switch case missing colon"""
    source = "void main() { switch (1) { case 1 printInt(1); } }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_unclosed_block():
    """108. Unclosed block"""
    source = "void main() { int x;"
    result = Parser(source).parse()
    assert "<EOF>" in result


def test_invalid_func_decl():
    """109. Invalid function declaration"""
    source = "void main( { }"
    result = Parser(source).parse()
    assert "Error on line" in result


def test_misplaced_else():
    """110. Misplaced else"""
    source = "void main() { else printInt(1); }"
    result = Parser(source).parse()
    assert "Error on line" in result
