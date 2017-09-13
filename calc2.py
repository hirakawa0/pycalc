#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import re

ops = {'+':operator.add, '-':operator.sub,
        '*':operator.mul, '/':operator.truediv}

unary = {'+':operator.pos, '-':operator.neg}

def expr(s, i):
    r, i = term(s, i)
    while s[i] in '+-':
        op = ops[s[i]]
        t, i = term(s, i+1)
        r = op(r,t)
    return r, i

def term(s, i):
    r, i = fact(s,i)
    while s[i] in '*/':
        op = ops[s[i]]
        t, i = fact(s, i+1)
        r = op(r,t)
    return r, i

def fact(s, i):
    if s[i] in '+-':
        uny = unary[s[i]]
        r, i = fact(s, i+1)
        return uny(r), i
    return prim(s, i)

def prim(s, i):
    if s[i] == '(':
        r, i = expr(s, i+1)
        return r, i+1
    elif s[i] == '[':
        ret = []
        while True:
            r, i = expr(s, i+1)
            ret.append(r)
            if s[i] == ']':
                break
        return ret, i+1
    j = i
    while s[i].isdigit() or s[i] == '.':
        i += 1
    return float(s[j:i]), i

def calc(s):
    s = re.sub(r'\s','',s)
    return expr(s+'@',0)[0]

s = input('input expression:\n')
print(calc(s))
