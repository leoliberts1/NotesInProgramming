import pytest

def capital_case(x):
    return chr(ord(x)-ord('a')+ord('A'))

@pytest.mark.parametrize ('inp, outp',[('a', 'A'),('1', '1'),('#', '#'),('-', '-'),('c', 'C'),])
def test_capital_case3(inp, outp):
    assert capital_case(inp) == outp