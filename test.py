#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codeql

def test_basic():
    db = codeql.Database.create_from_cpp('int main() { return 0; }')
    res = db.query('''
        select "Test"
    ''')
    assert res[1][0] == "Test"

def test():
    test_basic()

if __name__ == '__main__':
    test()
