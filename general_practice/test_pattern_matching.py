# -*- coding: utf-8 -*-

import pytest
from pattern_matching import find_match_indexes

def test_pattern_matching():

    text = 'itit'
    assert len(find_match_indexes('it',text)) == 2
