bool_v1 = True
bool_v2 = False
bool_v3 = None


def test_my_boolean_ideas():
    assert not (bool_v1 == bool_v2), "It seems that two are not equal"
    assert not (bool_v1 == bool_v3)
    assert not (bool_v2 == bool_v3)
    assert bool_v3 is None


def test_more_bools():
    assert 1 < 2 and 2 < 3
    assert 1 < 2 <= 3
    assert 1 != 2 and 1 != 3

    one = 1
    yek = 1
    bir = 1
    assert one == yek == bir
