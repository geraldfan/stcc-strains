# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:36:19 2020

@author: Gerald
"""

from app import db

# Class for the "model" table in the sBase.db file
class Strain(db.Model):
    """Class corresponding to the model table in the sBase.db

    ...
    Attributes
    ----------
    __tablename__ : str
        the name of the table in sBase.db
    stcc_number : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the stcc_number column in the sBase.db
    strain_name : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the strain_name column in the sBase.db
    identification : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the stcc_number column in the sBase.db
    genome_sequence : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the genome_sequence column in the sBase.db
    group : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the group column in the sBase.db
    biosefaty_level : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the biosefaty_level column in the sBase.db
    medium : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the medium column in the sBase.db
    cultivation_temperature : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the cultivation_temperature column in the sBase.db
    cultivating_condition : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the cultivating_condition column in the sBase.db
    source_of_isolation : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the source_of_isolation column in the sBase.db
    isolated_deposited_year : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the isolated_deposited_year column in the sBase.db
    remarks : db.Column(db.String)
        a Column object from the db module, with a db.String object as its parameter
        represents the stcc_number column in the sBase.db
    """
    __tablename__ = "strains"

    stcc_number = db.Column(db.String, primary_key=True)
    strain_name = db.Column(db.String)
    identification = db.Column(db.String)
    genome_sequence = db.Column(db.String)
    group = db.Column(db.String)
    biosefaty_level = db.Column(db.String)
    medium = db.Column(db.String)
    cultivation_temperature = db.Column(db.String)
    cultivating_condition = db.Column(db.String)
    source_of_isolation = db.Column(db.String)
    isolated_deposited_year = db.Column(db.String)
    remarks = db.Column(db.String)



    def __repr__(self):
        return "{}".format(self.system_type)