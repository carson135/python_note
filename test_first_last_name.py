from make_pizza import get_formatted_name

def test_first_last_name():
    """can handle normal name correctly"""
    formatted_name = get_formatted_name('matt', 'liu')
    assert formatted_name == 'Matt Liu'