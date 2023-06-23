#!/usr/env python3
# -*- coding: utf-8 -*-
def even(a, b, c):
    f = False
    if a % 2 == 0:
        f = True
    if b % 2 == 0:
        f = True
    if c % 2 == 0:
        f = True
    return f
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    f = False
    if a % 2 == 0:
        f = True
    if b % 2 == 0:
        f = True
    if c % 2 == 0:
        f = True
    print(f)
