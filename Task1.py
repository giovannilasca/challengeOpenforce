import csv
import urllib.request as req

def main():
    print('1. Scegliere il file' )
    answer = input('Si desidera aprire un file presente in locale o da un particolare indirizzo url? Digitare "u" per la prima opzione, "l" per la seconda: ')
    if answer == 'u':
        url = input('Inserire l\'indirizzo url del file: ')
        with req.urlopen(url, 't') as file:
            #completare

    elif answer == 'l':
        path = input('Inserire il percorso del file: ')
        file = open(path, "rt")
        data = csv.reader(file)
        instructor = input("Inserisci il nome di un professore per visualizzarne i corsi: ")
        for row in data:
            if instructor == '':
                print(row[1] + ', ' + row[3] + ', ' + row[0])
            elif instructor.lower().strip() in row[4].lower():
                print(row[1] + ', ' + row[3] + ', ' + row[0])
    else:
        print('Solo "u" o "l" sono risposte valide!')
        main()

main()