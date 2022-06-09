import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS arenas(
    name varchar,
    PRIMARY KEY (name))
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS lobbywarp(
    name varchar UNIQUE,
    x float,
    y float,
    z float,
    FOREIGN KEY (name) REFERENCES arenas)
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS arenawarp(
    name varchar UNIQUE,
    x float,
    y float,
    z float,
    FOREIGN KEY (name) REFERENCES arenas)
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS specwarp(
    name varchar UNIQUE,
    x float,
    y float,
    z float,
    FOREIGN KEY (name) REFERENCES arenas)
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS exitwarp(
    name varchar UNIQUE,
    x float,
    y float,
    z float,
    FOREIGN KEY (name) REFERENCES arenas)
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS p1(
    name varchar UNIQUE,
    x float,
    y float,
    z float,
    FOREIGN KEY (name) REFERENCES arenas)
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS p2(
    name varchar UNIQUE,
    x float,
    y float,
    z float,
    FOREIGN KEY (name) REFERENCES arenas)
            ''')
cur.execute('''CREATE TABLE IF NOT EXISTS classes(
    name varchar UNIQUE,
    helmet varchar,
    chest varchar,
    leggings varchar,
    boots varchar)
            ''')

def insert_arena(name):
    cur.execute('INSERT OR IGNORE INTO arenas VALUES(?);', [name])
    con.commit()

def insert_warp(warp_type, name, x, y, z):

    if (warp_type == "arena"):
        cur.execute('INSERT OR REPLACE INTO arenawarp VALUES (?, ?, ?, ?);', (name, x, y, z))
        con.commit()

    if (warp_type == "exit"):
        cur.execute('INSERT OR REPLACE INTO exitwarp VALUES (?, ?, ?, ?);', (name, x, y, z))
        con.commit()

    if (warp_type == "spec"):
        cur.execute('INSERT OR REPLACE INTO lobbywarp VALUES (?, ?, ?, ?);', (name, x, y, z))
        con.commit()

    if (warp_type == "exit"):
        cur.execute('INSERT OR REPLACE INTO specwarp VALUES (?, ?, ?, ?);', (name, x, y, z))
        con.commit()

def fetch_arenas():
    cur.execute("SELECT * FROM arenas")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def fetch_arena(name):
    cur.execute("SELECT * FROM arenas WHERE name = (?)", [name])
    arena = cur.fetchone()
    #arena[0] is needed for two reasons. One, I want to get only the name (at least for now), second, if I instead said SELECT name FROM it would give me a tuple containing the string of the arena name, not the actual string, so this makes it actually get the string.
    return arena[0]

def fetch_lobby(name):
    cur.execute("SELECT x,y,z FROM lobbywarp WHERE name = (?)", [name])
    lobbywarp = cur.fetchone()
    return lobbywarp

def insert_class(name, helmet, chest, leggings, boots):
    cur.execute('INSERT OR REPLACE INTO classes VALUES (?, ?, ?, ?, ?);', (name, helmet, chest, leggings, boots))
    con.commit()