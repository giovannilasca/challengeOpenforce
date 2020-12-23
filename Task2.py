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
    file = open(path, "rt")
    data = csv.reader(file)
    return data

def filter_method(data):
    instructors = []
    instructor = input('Inserisci il nome di un professore per visualizzarne i corsi o premere Invio per visualizzarli tutti: ')
    if instructor == '':
        for row in data:
            print(row[1] + ', ' + row[3] + ', ' + row[0])
    elif instructor != '':
        instructors.append(instructor)
        while True:
            instructor = input('Vuoi inserire il nome di un altro professore? Inserire un altro nome oppure "q" per andare avanti: ')
            if instructor.lower() == 'q':
                break
            instructors.append(instructor)
        for row in data:
            for instructor in instructors:    
                if instructor.lower().strip() in row[4].lower():
                    print(row[1] + ', ' + row[3] + ', ' + row[0])

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

main()