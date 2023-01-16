from src.dni import DNI


def test_formato_incorrecto():
    assert False == DNI('2837A212').checkFormatoDni()

    assert False == DNI('E2749391').checkFormatoDni()

    assert False == DNI.checkFormatoDni(
        '182945Y2')

    assert False == DNI.checkFormatoDni(
        'P1825482')

    assert False == DNI.checkFormatoDni(
        'X1827381')

    assert False == DNI.checkFormatoDni(
        '3927571Q')

    assert False == DNI.checkFormatoDni(
        '481693K1')

    assert False == DNI.checkFormatoDni(
        '5724149I')

    assert False == DNI.checkFormatoDni(
        '882936W2')

    assert False == DNI.checkFormatoDni(
        '1924528Ñ')


def test_dni_corto():
    assert False == DNI('4892').checkLongitud()

    assert False == DNI('9').checkLongitud()

    assert False == DNI('4892992').checkLongitud()

    assert False == DNI('4322173').checkLongitud()

    assert False == DNI('194721').checkLongitud()

    assert False == DNI('2947128').checkLongitud()

    assert False == DNI('2504745').checkLongitud()

    assert False == DNI('849212').checkLongitud()

    assert False == DNI('849212').checkLongitud()

    assert False == DNI('123456').checkLongitud()


def test_dni_correcto():
    assert True == DNI('43221731').checkDni()

    assert True == DNI('87654321').checkDni()

    assert True == DNI('12345678').checkDni()

    assert True == DNI('88328718').checkDni()

    assert True == DNI('56271662').checkDni()

    assert True == DNI('99326312').checkDni()

    assert True == DNI('58493726').checkDni()

    assert True == DNI('11458293').checkDni()


def test_dnis_completos():

    assert '66582415Z' == DNI('66582415').acoplarLetraDni()

    assert '86261461F' == DNI('86261461').acoplarLetraDni()

    assert '34737037E' == DNI('34737037').acoplarLetraDni()

    assert '43221731Q' == DNI('43221731').acoplarLetraDni()

    assert '49640019Q' == DNI('49640019').acoplarLetraDni()

    assert '93835983P' == DNI('93835983').acoplarLetraDni()

    assert '95225497T' == DNI('95225497').acoplarLetraDni()

    assert '57984320D' == DNI('57984320').acoplarLetraDni()

    assert '59105244M' == DNI('59105244').acoplarLetraDni()

    assert '63741486E' == DNI('63741486').acoplarLetraDni()

    assert '33135166D' == DNI('33135166').acoplarLetraDni()
