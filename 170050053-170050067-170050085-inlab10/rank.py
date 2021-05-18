import sqlite3
if __name__ == "__main__":
    pokedexdb =sqlite3.connect("pokedex.db")
    cur = pokedexdb.cursor()
    cur.execute(''' SELECT identifier FROM POKEMON ORDER BY base_experience DESC LIMIT 3;''')
    pokedexdb.commit()    
    for row in cur:
        print(row[0])
    print()
    pokedexdb.close()
