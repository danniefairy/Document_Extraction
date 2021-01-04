#!/bin/bash

# Install pip, python
yum install epel-release -y
yum install python36-pip -y
yum install python36 -y

# Install repo dependency
yum install gcc -y
python3 -m pip install -U pip
python3 -m pip install Flask==1.1.1
python3 -m pip install Flask-Cors==3.0.3
python3 -m pip install transformers
python3 -m pip install sentence-transformers==0.3.7.2
python3 -m pip install googletrans==3.1.0a0
python3 -m pip install --upgrade cython
python3 -m pip install sklearn
python3 -m pip install nltk