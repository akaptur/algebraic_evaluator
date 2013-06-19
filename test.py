import algebra_parser as a
import pdb

def test_parser():
    e = a.Evaluator()
    # pdb.set_trace()
    assert e.evaluate('2*3+1') == 7

def test_multiply_at_end():
    e = a.Evaluator()
    assert e.evaluate('2+3*1') == 5

def test_multiply_chained():
    e = a.Evaluator()
    assert e.evaluate('2+3*1*3') == 11

def test_chained_precedence():
    e = a.Evaluator()
    assert e.evaluate('2+3*1*3+1') == 12

def test_whitespace():
    e = a.Evaluator()
    assert e.evaluate('2 * 3 + 1') == 7

def test_multi_digit_num():
    e = a.Evaluator()
    assert e.evaluate('142*2') == 284

def test_tokenizer():
    e = a.Evaluator()
    assert e.tokenize('2*3+4') == [2, '*', 3, '+', 4]
    assert e.tokenize('55*3+4') == [55, '*', 3, '+', 4]
    assert e.tokenize('') == []
    try:
        e.tokenize('$')
        assert False # make sure this block fails one way or another!
    except Exception as e:
        assert e.message == "Invalid character in expression, cannot tokenize"


if __name__ == '__main__':
    test_parser()
    test_multiply_at_end()
    test_multiply_chained()
    test_chained_precedence()
    test_whitespace()
    test_multi_digit_num()
    test_tokenizer()
