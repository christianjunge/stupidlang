import pytest
from stupidlang.lang import parse_args

__author__ = "cs207labs"
__copyright__ = "cs207abs"
__license__ = "mit"


def test_parse_args():
    assert(parse_args(["-l", "tests/fake.txt"]).load[0] == 'tests/fake.txt')
    assert(parse_args(["-l", "tests/fake.txt", "tests/test1.sl"]).load[0] == 'tests/fake.txt')
