import sqlite3
import csv
if __name__ == "__main__":
    pokedexdb =sqlite3.connect("pokedex.db")
    cur = pokedexdb.cursor()
    with open('pokemon.csv','rU') as data:
        dr=csv.DictReader(data)
        to_db=[(i['id'], i['identifier'], i['species_id'], i['height'], i['weight'], i['base_experience'], i['order'], i['is_default']) for i in dr]
    cur.executemany('''INSERT INTO POKEMON ('id', 'identifier', 'species_id', 'height', 'weight', 'base_experience', 'order1', 'is_default') VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', to_db)
    pokedexdb.commit()
    with open('pokemon_abilities.csv','rU') as data1:
        dr1=csv.DictReader(data1)
        to_db1=[(i['pokemon_id'], i['ability_id'], i['is_hidden'], i['slot']) for i in dr1]
    cur.executemany('''INSERT INTO POKEMON_ABILITIES ('pokemon_id', 'ability_id', 'is_hidden','slot') VALUES (?, ?, ?, ?)''', to_db1)
    pokedexdb.commit()
    with open('abilities.csv','rU') as data2:
        dr2=csv.DictReader(data2)
        to_db2=[(i['id'], i['identifier'], i['generation_id'], i['is_main_series']) for i in dr2]
    cur.executemany('''INSERT INTO ABILITIES ('id', 'identifier', 'generation_id', 'is_main_series') VALUES (?, ?, ?, ?)''', to_db2)
    pokedexdb.commit()   
    pokedexdb.close()


