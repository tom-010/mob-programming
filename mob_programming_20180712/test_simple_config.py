import pytest
from simple_config import parse_ini_string

@pytest.mark.parametrize("test_input,expected", [
    (None, {}),
    ("", {}),
    (" ", {}),
    ("\n", {}),
    (" \n      \n    \n\n", {}),
    ("\n\n\n\t\n\n\t\n", {})
])
def test_parse_empty_edge_cases(test_input, expected):
    assertParse(test_input, expected)

def test_parse_global_option():
    assert parse_ini_string("global_option=true") == {
        None: {'global_option': 'true'}}

def test_parse_global_option_without_value_and_equal():
    assert parse_ini_string("global_option=") == {
        None: {'global_option': ""}}

@pytest.mark.parametrize("test_input,expected", [
    ("global_option=true", {None: {"global_option": "true"}}),
])
def test_parse_single_global_options(test_input, expected):
    assertParse(test_input, expected)

@pytest.mark.parametrize("test_input,expected", [
    ("global_option=", {None: {"global_option": ""}}),
    ("global_option=\n", {None: {"global_option": ""}}),
    ("\nglobal_option=", {None: {"global_option": ""}}),
])
def test_key_without_value(test_input, expected):
    assertParse(test_input, expected)

@pytest.mark.parametrize("test_input,expected", [
    ("  global=val", {None: {"global": "val"}}),
    ("global =val", {None: {"global": "val"}}),
    ("global= val", {None: {"global": "val"}}),
    ("global=    val   ", {None: {"global": "val"}}),
])
def test_lines_with_whitespace(test_input, expected):
    assertParse(test_input, expected)

@pytest.mark.parametrize("test_input,expected", [
    ("global=a=b", {None: {"global": "a=b"}}),
    ("global=a=b=c=d=e", {None: {"global": "a=b=c=d=e"}}),
    ("global==", {None: {"global": "="}})
])
def test_multiple_equals(test_input, expected):
    assertParse(test_input, expected)

@pytest.mark.parametrize("test_input,expected", [
    ("global_option1=true\nglobal_option2=false", {
     None: {'global_option1': 'true', 'global_option2': 'false'}}),
])
def test_parse_multiple_global_options(test_input, expected):
    assertParse(test_input, expected)

def assertParse(ini_string, expected):
    assert parse_ini_string(ini_string) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("global_option", {}),
    ("=val", {}),
    ("=val2", {})
])
def test_parse_invalid_input(test_input, expected):
    assertParse(test_input, expected)

def test_emtpy_section():
    assertParse("[]", {})

@pytest.mark.parametrize("test_input,expected", [
    ("[]\na=b", {}),
    ("""
    []
    a=b
    """, {}),
    ("[] \n a=b", {}),
    ("[ \n a=b", {}),
    ("] \n a=b", {}),
])
def test_invalid_section(test_input, expected):
      assertParse(test_input, expected)


# Empty Section
# Section without keys but with value
# Section without value but with key
# Validate Section with regex
