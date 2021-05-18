import sqlite3


if __name__ == "__main__":
    pokedexdb =sqlite3.connect("pokedex.db")
    cur = pokedexdb.cursor()
    cur.execute('''UPDATE ABILITIES set generation_id='8' WHERE is_main_series='0' ''')
    pokedexdb.commit()    
    pokedexdb.close()
