import pytest

from section_splitter import split_sections

def test_emtpy_section():
    assert_split("[]", [("", "")])

def test_empty_string__empty_global_section():
    assert_split("", [(None, "")])

def test_string_in_global__global_section_filled():
    assert_split("content in section does not matter", [(None, "content in section does not matter")])
    assert_split("foo", [(None, "foo")])

def test_global_plus_section__list_with_two_elements():
    assert len(split_sections("\n[]")) == 2

def test_global_plus_two_sections__list_with_three_elements():
    assert len(split_sections("\n[]\n[]")) == 3
    assert len(split_sections("[]\n[]")) == 2

def test_global_and_named_section_with_content__list_with_tuple_with_name_and_content():
    assert_split("\n[name]\nfoo", [(None, ""), ('name', 'foo')])

def test_named_section_with_content__list_with_tuple_with_name_and_content():
    assert_split("[name]\nfoo", [('name', 'foo')])

def assert_split(ini_string, expected):
    assert split_sections(ini_string) == expected