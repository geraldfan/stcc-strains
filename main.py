# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:12:48 2020

@author: Gerald
"""

# main.py

from app import app
from db_setup import init_db, db_session
from forms import StrainSearchForm
from flask import flash, render_template, request, redirect, send_file
from strains import Strain
from tables import Results

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders the index.html template with a StrainSearchForm"""
    search = StrainSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

# Calls the search function and returns the results in results.html
@app.route('/results')
def search_results(search):
    """Takes in a StrainSearchForm and queries the database using the search String from the StrainSearchForm

    Parameters
    ----------
    search: StrainSearchForm
        The StrainSearchForm containing the "search" string used to query the sBase

    Returns
    result.html: html
        The html template containing a flask-table with the String that contains the "search" String
    """
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Strain No.':
            qry = db_session.query(Strain).filter(
                    Strain.stcc_number.contains(search_string, autoescape=True))
            results = qry.all()
        elif search.data['select'] == 'Strain Name':
            qry = db_session.query(Strain).filter(
                Strain.strain_name.contains(search_string, autoescape=True))
            results = qry.all()
        else:
            qry = db_session.query(Strain)
            results = qry.all()
    else:
        qry = db_session.query(Strain)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        result = Results(results)
        result.border = True

        search = StrainSearchForm(request.form)
        counter = 'Number of Strains found: ' + str(len(results))
        return render_template('results.html', form=search, result=result, counter=counter)


if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(threaded = True, port=5000)