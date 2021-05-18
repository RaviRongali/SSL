import sqlite3


if __name__ == "__main__":
    pokedexdb =sqlite3.connect("pokedex.db")
    cur = pokedexdb.cursor()

    cur.execute('''CREATE TABLE ABILITIES (id int,identifier varchar(20), generation_id int, is_main_series int)''')
    cur.execute('''CREATE TABLE POKEMON (id int,identifier varchar(20), species_id int, height int, weight int, base_experience int, order1 int, is_default int)''')
    cur.execute('''CREATE TABLE POKEMON_ABILITIES (pokemon_id int,ability_id int, is_hidden int,slot int)''')
    pokedexdb.close()


