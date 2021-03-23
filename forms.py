# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:19:51 2020

@author: Gerald
"""

# forms.py

from wtforms import Form, StringField, SelectField, validators

# Class for the search form
class StrainSearchForm(Form):
    """Takes in a Form object and outputs a custom form with choices specific to Models"""
    choices = [('Strain No.', 'Strain No.'),
               ('Strain Name', 'Strain Name')]
    select = SelectField('Search for strain:', choices=choices)
    search = StringField('')