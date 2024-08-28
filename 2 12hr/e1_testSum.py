from c3_refactor import sum


def test_sum():
    assert sum(1, 2) == 3, "❌ sum(1, 2) does not return 3"
    assert sum(-20, 20) == 0, "❌ sum(-20, 20) does not return 0"
    assert sum(20, 20) == 40, "❌ sum(20, 20) does not return 40"
    assert sum(560, 780) == 1340, "❌ sum(560, 780) does not return 1340"
    assert sum(1, 2) == 2, "❌ sum(1, 2) does not return 2"


test_sum()
