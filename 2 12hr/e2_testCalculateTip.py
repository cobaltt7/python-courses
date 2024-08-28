from c3_refactor import calculate_tip


def test_calculate_tip():
    assert calculate_tip(100, 20) == 20
    assert calculate_tip(-100, -20) == 20
    assert calculate_tip(100.23, 20) == 20.046


test_calculate_tip()
