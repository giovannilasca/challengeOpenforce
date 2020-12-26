import csv
import urllib.request as req

def url_method(): #preleva file tramite url
    url = input('Inserire l\'indirizzo url del file: ')
    file = req.urlopen(url)
    lines = [l.decode('utf-8-sig') for l in file.readlines()]
    data = csv.reader(lines)
    return data

def local_method(): #preleva file localmente
    path = input('Inserire il percorso del file: ')
    file = open(path)
    data = csv.reader(file)
    return data

def filter_instructor(data): #filtra per instructor
    instructors = []
    instructor = input('Inserisci il nome di un professore per visualizzarne i corsi o premere Invio per visualizzarli tutti: ')
    if instructor == '': #aggiunge a data_filtered tutti i corsi
        for row in data:
            institution = row[0]
            course_number = row[1]
            launch_date = row[2]
            course_title = row[3]
            teachers = row[4]
            course_year = row[6]
            data_filtered.append([institution, course_number, launch_date, course_title, teachers, course_year])
        
    elif instructor != '': #aggiunge a data_filtered tutti i corsi dei professori inseriti
        while instructor != '':
            instructors.append(instructor)
            instructor = input('Vuoi inserire il nome di un altro professore? Inserire un altro nome oppure Invio per andare avanti: ')            
        for row in data:
            for instructor in instructors:
                if instructor.lower().strip() in row[4].lower():
                    institution = row[0]
                    course_number = row[1]
                    launch_date = row[2]
                    course_title = row[3]
                    teachers = row[4]
                    course_year = row[6]
                    data_filtered.append([institution, course_number, launch_date, course_title, teachers, course_year])

    return data_filtered

def filter_year(data): #filtra per anno di corso
    year = str(input('Vuoi filtrare i risultati per anno di corso? Se sì inserire un numero da 1 a 4, altrimenti inserire "0": '))
    if year == '0':
        return data
    while year not in ['1', '2', '3', '4']:
        year = str(input('Inserire un numero da 1 a 4: '))
    year_filtered = []
    for row in data:
        if year == row[5]:
            year_filtered.append(row)
    data = year_filtered
    return data
   
def filter_date(data): #filtra per anno solare
    date = str(input('Vuoi filtrare i risultati per anno solare? Se sì inserire un anno, altrimenti inserire "0": '))
    if date == '0':
        return data
    while date not in ['2012', '2013', '2014', '2015', '2016']:
        date = str(input('Inserire un anno compreso tra 2012 e 2016: '))
    date_filtered = []
    for row in data:
        if row[2].endswith(date):
            date_filtered.append(row)
    data = date_filtered
    return data

def remove_dup(data): #rimuove duplicati dalla lista finale dei risultati
    for row in data:
        if row not in dup_free:
            dup_free.append(row)
    if not dup_free:
        a = input('Non ci sono risultati per questa ricerca, vuoi cercare di nuovo o terminare il programma? "s" per cercare ancora, "q" per terminare: ')
        if a.lower() == 's':
            main()
        elif a.lower() == 'q':
            return 0
    else:
        return dup_free

def main():
    print('Scegliere il file .csv da leggere')
    answer = input('Si desidera aprire un file presente in locale o da un particolare indirizzo url? Digitare "l" per la prima opzione, "u" per la seconda: ')
    if answer == 'u':
        remove_dup(filter_date(filter_year(filter_instructor(url_method()))))
        for row in dup_free:
            print(row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', ' + row[4] + ', ' + row[5]) 
    elif answer == 'l':  
        remove_dup(filter_date(filter_year(filter_instructor(local_method()))))
        for row in dup_free:
            print(row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', ' + row[4] + ', ' + row[5])
    else:
        print('Solo "u" o "l" sono risposte valide!')
        main()

data_filtered = []
dup_free = []
main()
