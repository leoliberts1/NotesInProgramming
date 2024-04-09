def add(x,y):
    return x+y

def test_myfirst_test():
    assert (add(2,3) == 5)

def seconds_to_hours(x):
    return x/3600
def test_seconds():
    assert seconds_to_hours(3600) == 1
    assert seconds_to_hours(-1) == (-1/3600)
    assert seconds_to_hours(0) == 0
    assert seconds_to_hours(3) == 3/3600
    assert seconds_to_hours(4.00000000000000000000000000000000000000043) == 4.00000000000000000000000000000000000000043/3600
    #TODO For floating point number never ever compare numbers like this
# function to be tested
def capital_case(x):
    return chr(ord(x)-ord('a')+ord('A'))
def test_capital_case():
    assert capital_case('a') == 'A'
    assert capital_case('x') == 'X'
    assert capital_case('z') == 'Z'

    for ( inp,out) in [("a","A"),("b","B"),("2","2")]:
        assert (capital_case(inp) == out)



def revWords(sentence):
    return " ".join(sentence.split()[::-1])
def test_rev():
    assert (revWords("Some Words") == "Words Some")
    assert (revWords("") == "")
    assert (revWords("Happy") == "Happy")
    assert (revWords(" Happy ") == " Happy ")



