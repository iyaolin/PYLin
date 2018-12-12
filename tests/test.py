from PYLin import demo

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''

    
    assert demo.fahrToKelv(32) == 273.15, 'incorrect freezing point!'
