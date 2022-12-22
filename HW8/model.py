import csv

def get_people():
# чтение csv-файла
    with open('people.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        #title = next(reader)
        sp = list(reader)
        return sp
       # for row in sp:
        #    print(row)

def add(man):
    with open('people.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(man)

def delet(namber):
    with open('people.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
    if namber < len(sp):
        del sp[namber]
        with open('people.csv', 'w', encoding="utf8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in sp:
                writer.writerow(row)