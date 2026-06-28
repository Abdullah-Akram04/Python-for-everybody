import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Remove old tables and create new ones
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# Open the CSV file
handle = open('tracks.csv')

# Skip the header row
next(handle)

for line in handle:
    line = line.strip()
    pieces = line.split(',')

    if len(pieces) < 7:
        continue

    title = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # Insert Artist
    cur.execute('''
        INSERT OR IGNORE INTO Artist (name)
        VALUES (?)
    ''', (artist,))

    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert Genre
    cur.execute('''
        INSERT OR IGNORE INTO Genre (name)
        VALUES (?)
    ''', (genre,))

    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert Album
    cur.execute('''
        INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)
    ''', (album, artist_id))

    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    # Insert Track
    cur.execute('''
        INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, album_id, genre_id, length, rating, count))

# Save changes
conn.commit()

# Display first 3 records to verify
sql = '''
SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track
JOIN Album ON Track.album_id = Album.id
JOIN Artist ON Album.artist_id = Artist.id
JOIN Genre ON Track.genre_id = Genre.id
ORDER BY Artist.name
LIMIT 3
'''

print("Verification:\n")
for row in cur.execute(sql):
    print(row)

cur.close()
conn.close()