from rules import LifeRule


def test_parse_rule():
    rule = LifeRule.from_string("23/3")

    assert rule.survival == {2, 3}
    assert rule.birth == {3}