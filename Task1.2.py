import csv
import unicodecsv
import urllib.request as req

# Questa è una versione del primo task con i metodi definiti anche per il file preso dall'url, ma purtroppo non funziona in quanto dopo aver passato il nome del 
# professore per filtrare non printa i risultati (non riesco a trovare una soluzione purtroppo ma è così che avrei voluto organizzare il codice di questo task
# quindi allego anche questo file)

def url_method():
    url = input('Inserire l\'indirizzo url del file: ')
    with req.urlopen(url) as file:
        data = unicodecsv.reader(file, encoding='utf-8-sig', delimiter=',')
    return data

def local_method():
    path = input('Inserire il percorso del file: ')
    file = open(path, "rt")
    data = csv.reader(file)
    return data

def filter_method(data):
    instructor = input("Inserisci il nome di un professore per visualizzarne i corsi: ")
    for row in data:
        if instructor == '':
            print(row[1] + ', ' + row[3] + ', ' + row[0])
        elif instructor.lower().strip() in row[4].lower():
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