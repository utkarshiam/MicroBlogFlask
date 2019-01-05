#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:20:22 2019

@author: mudita
"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
