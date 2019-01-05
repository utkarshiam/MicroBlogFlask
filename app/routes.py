#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:20:22 2019

@author: mudita
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user= {'username': 'utkarsh'}
    return render_template('index.html', title='Home', user=user)
