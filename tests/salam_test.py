from salam.salam import salam


def test_salam():
    expected = "Salam Aleikum!"
    result = salam()
    assert result == expected
