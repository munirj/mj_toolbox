# tests/test_lib.py
from mj_toolbox.lib import try_me


def test_type_of_try_me():
    assert type(try_me()) == str
