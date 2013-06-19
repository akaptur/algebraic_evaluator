import algebra_parser as a

def test_parser():
    e = a.Evaluator()
    assert e.evaluate('2*3+1') == 7

def test_whitespace():
    e = a.Evaluator()
    assert e.evaluate('2 * 3 + 1') == 7

def test_multi_digit_num():
    e = a.Evaluator()
    assert e.evaluate('142*2') == 284

def test_tokenizer():
    e = a.Evaluator()
    assert e.tokenize('2*3+4') == ['2', '*', '3', '+', '4']
    assert e.tokenize('55*3+4') == ['55', '*', '3', '+', '4']
    assert e.tokenize('') == []
    try:
        e.tokenize('$')
    except Exception as e:
        assert e.message == "Invalid character in expression, cannot tokenize"


if __name__ == '__main__':
    test_parser()
    test_whitespace()
    test_multi_digit_num()
    test_tokenizer()
