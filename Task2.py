import csv
import urllib.request as req

def url_method():
    url = input('Inserire l\'indirizzo url del file: ')
    file = req.urlopen(url)
    lines = [l.decode('utf-8-sig') for l in file.readlines()]
    data = csv.reader(lines)
    return data

def local_method():
    path = input('Inserire il percorso del file: ')
    file = open(path)
    data = csv.reader(file)
    return data
    
def filter_method(data):
    instructors = []
    instructor = input('Inserisci il nome di un professore per visualizzarne i corsi o premere Invio per visualizzarli tutti: ')
    if instructor == '':
        remove_dup(data)
        for row in dup_free:
            print(row[1] + ', ' + row[3] + ', ' + row[0])
    elif instructor != '':
        instructors.append(instructor)
        while instructor.lower() != 'q':
            instructor = input('Vuoi inserire il nome di un altro professore? Inserire un altro nome oppure "q" per andare avanti: ')
            instructors.append(instructor)
        for row in data:
            for instructor in instructors:    
                if instructor.lower().strip() in row[4].lower():
                    print(row[1] + ', ' + row[3] + ', ' + row[0])

def filter_year():
    year = int(input('Vuoi filtrare i risultati per anno di corso? Se sì inserire un numero da 1 a 4, altrimenti inserire "0": '))
    if year == 0:
        return None
    while year not in range(0,5):
        year = int(input('Inserire un numero da 1 a 4: '))
    
def filter_date():
    date = int(input('Vuoi filtrare i risultati per anno solare? Se sì inserire un anno, altrimenti inserire "0": '))
    if date == 0:
        return None
    while date not in range(2011, 2017):
        date = int(input('Inserire un anno compreso tra 2012 e 2016: '))

def remove_dup(data):
    for x in data:
        if x not in dup_free:
            dup_free.append(x)
    return dup_free

def main():
    print('Scegliere il file .csv da leggere')
    answer = input('Si desidera aprire un file presente in locale o da un particolare indirizzo url? Digitare "l" per la prima opzione, "u" per la seconda: ')
    if answer == 'u':
        filter_method(url_method()) 
    elif answer == 'l':  
        filter_method(local_method())
    else:
        print('Solo "u" o "l" sono risposte valide!')
        main()

dup_free = []
main()
filter_year()
filter_date()

# reader = csv.reader(lines)
# header = next(reader)
# for row in reader:
#     institution = row[0]
#     course_number = row[1]
#     launch_date = row[2]
#     course_title = row[3]
#     instructors = row[4]
#     year = int(row[6])
#     data.append([institution, course_number, launch_date, course_title, instructors, year])