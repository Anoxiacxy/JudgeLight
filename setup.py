#!/usr/bin/env python
# coding=utf-8
from distutils.core import setup, Extension

sources = [
    'judgelight/src/judgelight.c', 'judgelight/src/limit.c', 'judgelight/src/listen.c', 'judgelight/src/run.c'
]
setup(
    name='judgelight',
    version='1.0.0',
    ext_modules=[Extension('judgelight/judgelight', sources=sources)],
    packages=['judgelight']
)