from simple_config import SimpleConfig


def test_parse_empyt_string():
    sc = SimpleConfig()
    assert sc.params == {}
