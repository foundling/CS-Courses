# -*- coding: utf-8 -*-

import pytest
from pattern_matching import find_match_indexes

def test_match_start():
    text = 'it is great'
    indexes = find_match_indexes('it',text)
    assert len(indexes) == 1
    assert indexes[0] == 0


def test_match_middle():
    text = 'is it great?'
    indexes = find_match_indexes('it',text)
    assert len(indexes) == 1
    assert indexes[0] == 3

def test_match_end():

    text = 'is it great?, yes it is'
    indexes = find_match_indexes('it',text)
    assert len(indexes) == 2
    assert indexes[0] == 3
    assert indexes[1] == 18
