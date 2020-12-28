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
            # data_filtered.append([institution, course_number, launch_date, course_title, teachers, course_year])
            data_filtered.append(
                {
                    "Institution": institution,
                    "CourseNumber": course_number,
                    "LaunchDate": launch_date,
                    "CourseTitle": course_title,
                    "Instructors": teachers,
                    "Year": course_year
                }
            )

    return data_filtered

def filter_year(year, data): #filtra per anno di corso
    if year == '0':
        return data
    year_filtered = []
    for row in data:
        # if year == row[5]:
        #     year_filtered.append(row)
        if year == row.get('Year'):
            year_filtered.append(row)
    data = year_filtered
    return data
   
def filter_date(date, data): #filtra per anno solare
    if date == '0':
        return data
    date_filtered = []
    for row in data:
        if row.get('LaunchDate').endswith(date):
            date_filtered.append(row)
    data = date_filtered
    return data

@app.route('/') # Home
def index():
    return render_template('index.html')      

# Non sono riuscito a fare in modo che la form passasse i dati in input al server in formato json, però la route del server accetta il json, filtra i risultati e restituisce un json come richiesto
# Allego screen della chiamata al server fatto su Postman

# webserver route
@app.route('/server', methods = ['POST'])
def server():
    csvdata = url_method()
    data = request.json
    instructor = data['instructor']
    launch_date = data['launch_date']
    year = data['year']
    data_filtered = filter_date(launch_date, filter_year(year, filter_instructor(instructor, csvdata)))
    print(data_filtered)
    return json.dumps(data_filtered)

if __name__ == '__main__':
    app.run(debug=True)