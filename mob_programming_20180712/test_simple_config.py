import pytest
from simple_config import parse_ini_string

@pytest.mark.parametrize("test_input,expected", [
    (None, {}),
    ("", {}),
    (" ", {}),
    ("\n", {}),
    (" \n      \n    \n\n", {})
])
def parse_empty_edge_cases(test_input, expected):
    assertParse(test_input, expected)

def test_parse_global_option():
    assert parse_ini_string("global_option=true") == {
        None: {'global_option': 'true'}}


def test_parse_global_option_without_value_and_equal():
    assert parse_ini_string("global_option=") == {
        None: {'global_option': ""}}


@pytest.mark.parametrize("test_input,expected", [
    ("global_option", {}),
    ("=val", {})
])
def test_parse_invalid_input(test_input, expected):
    assertParse(test_input, expected)


@pytest.mark.parametrize("test_input,expected", [
    ("global_option=true", {None: {"global_option": "true"}}),
    ("global_option=", {None: {"global_option": ""}}),
    ("global_option=\n", {None: {"global_option": ""}}),
    ("\nglobal_option=", {None: {"global_option": ""}}),
    ("  global=val", {None: {"global": "val"}}),
    ("global=a=b", {None: {"global": "a=b"}})
])
def test_parse_single_global_options(test_input, expected):
    assertParse(test_input, expected)


@pytest.mark.parametrize("test_input,expected", [
    ("global_option1=true\nglobal_option2=false", {
     None: {'global_option1': 'true', 'global_option2': 'false'}}),
])
def test_parse_multiple_global_options(test_input, expected):
    assertParse(test_input, expected)


def assertParse(ini_string, expected):
    assert parse_ini_string(ini_string) == expected


# leerzeichen vor key, nach key, vor value, nach value
# Section without keys and
# =value
