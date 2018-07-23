# -*- coding: utf-8 -*-

import re
import sqlite3
from contextlib import closing
import shaping_text as st

class NLPText():
    def __init__(self, ):
        texts=[]

    def remove_duplicate():
        self.texts = list(set(texts))

    def load_from_db(db_name, clm_name, table_name,bool_strip):
        select = 'select %s from %s' % (clm_name,table_name)
        with closing(sqlite3.connect(dbname)) as conn:
            for row in c.execute(select_sql):
                if(bool_strip):
                    texts.append(row[0].strip())
                else:
                    texts.append(row[0])

    def load_from_file(text_name,bool_strip):
        with open(text_name,'r') as f:
            for row in f:
                if(bool_strip):
                    texts.append(row.strip())
                else:
                    texts.append(row)

    def get_text_from_index(index):
        return texts[index]

    def get_hiragana():
        res=[]
        for text in texts:
            if(st.is_Hiragana(text)):
                res.append(text)
        return res

    def get_katakana():
        res=[]
        for text in texts:
            if(st.is_Katakana(text)):
                res.append(text)
        return res

