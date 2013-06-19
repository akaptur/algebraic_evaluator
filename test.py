import algebra_parser as a

def test_parser():
    e = a.Evaluator()
    assert e.evaluate('2*3+1') == 7

if __name__ == '__main__':
    test_parser()