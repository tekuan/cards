from yoyo import step

steps = [
    step('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            image TEXT NOT NULL,
            value TEXT NOT NULL,
            suit TEXT NOT NULL
        )
    ''')
]
