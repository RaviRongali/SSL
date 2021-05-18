#!/usr/bin/env python3

import csv
import sqlite3

db = sqlite3.connect('cse_students.sqlite')
db.execute('CREATE TABLE COUNT (CATEGORY, NUMBER)')
with open('count.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for name, num in reader:
        db.execute('INSERT INTO COUNT VALUES (?, ?)', (name, num))


def returnCount(name):
    return db.execute('SELECT NUMBER FROM COUNT WHERE CATEGORY=?', (name,)).fetchall()[0][0]


while True:
    category = input('Please enter name of category (or "q" to quit): ')
    if category == 'q':
        exit()
    else:
        print('The number of students in {category} is {x}' .format(category=category, x=returnCount(category)))
