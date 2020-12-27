from flask import Flask, render_template, request, url_for
import urllib.request as req
import csv
import json
import pandas as pd
import xlsxwriter

app = Flask(__name__)

def url_method(): #preleva file tramite url
    url = 'https://raw.githubusercontent.com/reisanar/datasets/master/harvardMIT.csv'
    file = req.urlopen(url)
    lines = [l.decode('utf-8-sig') for l in file.readlines()]
    data = csv.reader(lines)
    return data

def local_method(f): #preleva file localmente
    file = open(f)
    data = csv.reader(file)
    return data

def filter_instructor(instructor, data): #filtra per instructor
    data_filtered = []
    for row in data:
        if instructor.lower().strip() in row[4].lower():
            institution = row[0]
            course_number = row[1]
            launch_date = row[2]
            course_title = row[3]
            teachers = row[4]
            course_year = row[6]
            data_filtered.append([institution, course_number, launch_date, course_title, teachers, course_year])

    return data_filtered

def filter_year(year, data): #filtra per anno di corso
    if year == '0':
        return data
    year_filtered = []
    for row in data:
        if year == row[5]:
            year_filtered.append(row)
    data = year_filtered
    return data
   
def filter_date(date, data): #filtra per anno solare
    if date == '0':
        return data
    date_filtered = []
    for row in data:
        if row[2].endswith(date):
            date_filtered.append(row)
    data = date_filtered
    return data

@app.route('/') # Home
def index():
    return render_template('index.html')

@app.route('/datasubmit', methods = ["POST"]) # Crea json a partire dai dati inseriti nella form
def datasubmit():
    if request.method == 'POST':
        f = request.form['csvfile']
        local_method(f)
        instructor = request.form['instructor']
        launch_date = request.form['launch_date']
        course_year = request.form['year']
        json = '{ "instructor": "' + instructor + '", "launch_date": "'+ launch_date + '", "year": "'+ course_year + '" }'
        return render_template('datasubmit.html', json = json)           

# webserver route
@app.route('/server', methods = ['POST'])
def server():
    csvdata = url_method()
    data = request.json
    instructor = data['instructor']
    launch_date = data['launch_date']
    year = data['year']
    data_filtered = filter_date(launch_date, filter_year(year, filter_instructor(instructor, csvdata)))

    result_json = '{ '

    for row in data_filtered:
        json += '{ "institution": ' + row[0] + ', "course_number": ' + row[1] + ', "launch_date": ' + row[2] + ', "course_title": ' + row[3] + ', "instructors": ' + row[4] + ', "course_year": ' + row[5] + '}, '

    result_json += ' }'
    return result_json

# @app.route('/save', methods=['GET', 'POST']) # 3. Stampa risultati a schermo e possibilità di salvare in formato .xlsx
# def save():
#     return "File salvato correttamente!"

if __name__ == '__main__':
    app.run(debug=True)