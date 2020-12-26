from flask import Flask, render_template, request, url_for
import csv
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) #home, 1. Selezionare file da locale
def index():
    return render_template('index.html')

@app.route('/filter', methods = ['GET', 'POST']) # 2. Selezionare le informazioni da filtrare
def filter():
    if request.method == 'POST':
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('filter.html', data = data)           

@app.route('/save', methods=['GET', 'POST']) # 3. Stampa risultati a schermo e possibilità di salvare in formato .xlsx
def save():

    return "File salvato correttamente!"

if __name__ == '__main__':
    app.run(debug=True)