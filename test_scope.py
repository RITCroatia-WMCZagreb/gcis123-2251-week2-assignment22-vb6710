
from scope import STRING_GLOBAL, INT_GLOBAL, FLOAT_GLOBAL, print_param, print_local
import pytest
import io
import sys
import re
import inspect


def test_string_global_type():
    assert isinstance(STRING_GLOBAL, str)

def test_int_global_type():
    assert isinstance(INT_GLOBAL, int)

def test_float_global_type():
    assert isinstance(FLOAT_GLOBAL, float)


