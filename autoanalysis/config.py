"""
Python script config.py
Created by Anne Pajon @pajanne on 25/01/2017
"""

import yaml
import os

yml_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'autoanalysis.yml')

with open(yml_filepath, 'r') as yml_file:
    cfg = yaml.load(yml_file)


print cfg
