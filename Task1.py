import csv

file = open("harvardMIT.csv", "rt")
myReader = csv.reader(file)

instructor = input("Inserisci il nome di un professore per visualizzarne i corsi: ")
for row in myReader:
    if instructor == '':
        print(row[1] + ', ' + row[3] + ', ' + row[0])
    if instructor.lower().strip() in row[4].lower():
        print(row[1] + ', ' + row[3] + ', ' + row[0])
