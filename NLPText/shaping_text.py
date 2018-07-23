# -*- coding: utf-8 -*-

import re

hiraganas = re.compile(r'[\u3041-\u3093]*')
katakanas = re.compile(r'[\u30A1-\u30F4]*')

def is_Hiragana(word):
	return hiraganas.fullmatch(words)

def is_Katakana(word):
	return katakanas.fullmatch(word)
	