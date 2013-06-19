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


if __name__ == '__main__':
    test_parser()
    test_whitespace()
    test_multi_digit_num()
