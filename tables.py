# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:22:22 2020

@author: Gerald
"""

from flask_table import Table, Col, LinkCol

# Result html table outputted on the website.
class Results(Table):
    """Class corresponding to the search results HTML table displayed on the website

    ...
    Attributes
    ----------
    classes: List[str]
        a List containing the html classes the table belongs to
        used for CSS purposes
    stcc_number:Col(str)
        a Col object from the flask_table module, maps to the stcc_number in Strain
    strain_name:Col(str)
        a Col object from the flask_table module, maps to the strain_name in Strain
    identification:Col(str)
        a Col object from the flask_table module, maps to the identification in Strain
    genome_sequence:Col(str)
        a Col object from the flask_table module, maps to the genome_sequence in Strain
    group:Col(str)
        a Col object from the flask_table module, maps to the group in Strain
    biosefaty_level:Col(str)
        a Col object from the flask_table module, maps to the biosefaty_level in Strain
    medium:Col(str)
        a Col object from the flask_table module, maps to the medium in Strain
    cultivation_temperature:Col(str)
        a Col object from the flask_table module, maps to the cultivation_temperature in Strain
    cultivating_condition:Col(str)
        a Col object from the flask_table module, maps to the cultivating_condition in Strain
    source_of_isolation:Col(str)
        a Col object from the flask_table module, maps to the source_of_isolation in Strain
    isolated_deposited_year:Col(str)
        a Col object from the flask_table module, maps to the isolated_deposited_year in Strain
    remarks:Col(str)
        a Col object from the flask_table module, maps to the remarks in Strain
    """

    classes = ['blueTable']
    stcc_number = Col('STCC No.')
    strain_name = Col('Strain Name')
    identification = Col('Identification')
    genome_sequence = Col('Genome Sequence')
    group = Col('Group')
    biosefaty_level = Col('Biosefaty Level');
    medium = Col('Medium')
    cultivation_temperature = Col('Cultivation Temperature (°C)')
    cultivating_condition = Col('Cultivating Condition')
    source_of_isolation = Col('Source Of Isolation')
    isolated_deposited_year = Col('Isolated/Deposited Year')
    remarks = Col('Remarks')

