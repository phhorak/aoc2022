#!/bin/bash

mkdir $1
cd $1
echo "pairs =  [l.split('\n')for l in open('input').read().rstrip().split('\n\n')]" > day$1.py
atom day$1.py
atom input
