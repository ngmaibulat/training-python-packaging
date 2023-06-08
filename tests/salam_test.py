from ngm_salam.message import salam


def test_salam():
    expected = "Salam Aleikum!"
    result = salam()
    assert result == expected
