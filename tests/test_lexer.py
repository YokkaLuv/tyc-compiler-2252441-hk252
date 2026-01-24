"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# Test Case 1: Integer Literals
def test_integer_literals():
    """Test integer literal recognition (decimal base 10)"""
    source = "0 100 255 2500"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Should recognize integer literals
    assert "INTLIT,0" in tokens
    assert "INTLIT,100" in tokens
    assert "INTLIT,255" in tokens
    assert "INTLIT,2500" in tokens
    assert "EOF" in tokens


# Test Case 2: Float Literals
def test_float_literals():
    """Test float literal recognition (decimal notation and scientific notation)"""
    source = "0.0 3.14 1.23e4 5.67E-2 1. .5"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Should recognize float literals in various formats
    assert "FLOATLIT,0.0" in tokens
    assert "FLOATLIT,3.14" in tokens
    assert "FLOATLIT,1.23e4" in tokens
    assert "FLOATLIT,5.67E-2" in tokens
    assert "FLOATLIT,1." in tokens
    assert "FLOATLIT,.5" in tokens
    assert "EOF" in tokens


# Test Case 3: String Literals with Escape Sequences
def test_string_literals():
    """Test string literal recognition with escape sequences"""
    source = '"This is a string" "He asked me: \\"Where is John?\\"" ""'
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Should recognize string literals (note: lexer strips the quotes)
    assert 'STRINGLIT,This is a string' in tokens
    assert 'STRINGLIT,He asked me: \\"Where is John?\\"' in tokens
    assert 'STRINGLIT,' in tokens  # empty string
    assert "EOF" in tokens


# Test Case 4: Comments (Line and Block Comments)
def test_comments():
    """Test that comments are properly ignored and not tokenized"""
    source = """
    // This is a line comment
    auto x = 5; /* This is a block comment
                   that spans multiple lines */
    /* Another block comment */ int y = 10;
    """
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Comments should NOT appear in tokens, only meaningful tokens should
    assert "AUTO,auto" in tokens
    assert "ID,x" in tokens
    assert "INTLIT,5" in tokens
    assert "INT,int" in tokens
    assert "ID,y" in tokens
    assert "INTLIT,10" in tokens
    # Comments should not be in token stream
    assert "This is a line comment" not in tokens
    assert "This is a block comment" not in tokens
    assert "EOF" in tokens


# Test Case 5: Keywords and Identifiers
def test_keywords_and_identifiers():
    """Test recognition of keywords and valid identifiers"""
    source = "auto int float string void struct MyVar myvar _private counter123"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Should recognize keywords
    assert "AUTO,auto" in tokens
    assert "INT,int" in tokens
    assert "FLOAT,float" in tokens
    assert "STRING,string" in tokens
    assert "VOID,void" in tokens
    assert "STRUCT,struct" in tokens
    
    # Should recognize identifiers (case-sensitive)
    assert "ID,MyVar" in tokens
    assert "ID,myvar" in tokens
    assert "ID,_private" in tokens
    assert "ID,counter123" in tokens
    assert "EOF" in tokens


# Test Case 6: Negative Integer Literals (Basic)
def test_negative_integer_literals():
    """Test that negative integers are recognized as single INTLIT tokens"""
    source = "-45 -100 -0 -999"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Negative integers should be single tokens, not SUB + INTLIT
    assert "INTLIT,-45" in tokens
    assert "INTLIT,-100" in tokens
    assert "INTLIT,-0" in tokens
    assert "INTLIT,-999" in tokens
    # SUB should NOT appear
    assert "SUB" not in tokens
    assert "EOF" in tokens


# Test Case 7: Negative Float Literals (Basic)
def test_negative_float_literals():
    """Test that negative floats are recognized as single FLOATLIT tokens"""
    source = "-3.14 -0.5 -1.23e4 -5.67E-2 -1. -.5"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Negative floats should be single tokens
    assert "FLOATLIT,-3.14" in tokens
    assert "FLOATLIT,-0.5" in tokens
    assert "FLOATLIT,-1.23e4" in tokens
    assert "FLOATLIT,-5.67E-2" in tokens
    assert "FLOATLIT,-1." in tokens
    assert "FLOATLIT,-.5" in tokens
    # SUB should NOT appear
    assert "SUB" not in tokens
    assert "EOF" in tokens


# Test Case 8: Subtraction with Spaces (should use SUB operator)
def test_subtraction_with_spaces():
    """Test that subtraction with spaces uses SUB operator correctly"""
    source = "5 - 3"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # With spaces, should be: INTLIT(5) SUB INTLIT(3)
    assert "INTLIT,5" in tokens
    assert "SUB,-" in tokens
    assert "INTLIT,3" in tokens
    assert "EOF" in tokens


# Test Case 9: Subtraction without Spaces (ambiguous - lexer uses longest match)
def test_subtraction_without_spaces():
    """Test subtraction without spaces - lexer will treat -3 as negative literal"""
    source = "5-3"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # Without spaces: lexer uses longest match, so -3 becomes INTLIT(-3)
    # Result: INTLIT(5) INTLIT(-3) - parser would handle this
    assert "INTLIT,5" in tokens
    assert "INTLIT,-3" in tokens
    # Note: This is lexically valid, parser will report error for consecutive literals
    assert "EOF" in tokens


# Test Case 10: Mixed Negative Literals and Subtraction
def test_mixed_negative_and_subtraction():
    """Test mixed cases of negative literals and subtraction"""
    source = "-10 + 5 - 3 * -2"
    tokenizer = Tokenizer(source)
    tokens = tokenizer.get_tokens_as_string()
    
    # -10 is negative literal, - 3 is subtraction (with space), -2 is negative literal
    assert "INTLIT,-10" in tokens
    assert "ADD,+" in tokens
    assert "INTLIT,5" in tokens
    assert "SUB,-" in tokens
    assert "INTLIT,3" in tokens
    assert "MUL,*" in tokens
    assert "INTLIT,-2" in tokens
    assert "EOF" in tokens
