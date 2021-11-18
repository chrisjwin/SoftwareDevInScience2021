def check_if_number(numberstring):
    return numberstring.isdigit()

def test_check_if_number():
    assert check_if_number(numberstring='24')
    assert not check_if_number(numberstring='text')

