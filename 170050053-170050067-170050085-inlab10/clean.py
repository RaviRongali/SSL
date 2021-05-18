import sqlite3


if __name__ == "__main__":
    pokedexdb =sqlite3.connect("pokedex.db")
    cur = pokedexdb.cursor()
    cur.execute('''DELETE FROM POKEMON WHERE identifier LIKE 'rogue%' ''')
    pokedexdb.commit()
    cur.execute('''select * from POKEMON''')
    for row in cur:
        print(row)
    print()
    pokedexdb.close()
