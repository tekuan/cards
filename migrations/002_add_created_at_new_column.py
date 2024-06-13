from yoyo import step

steps = [
    step('''
        ALTER TABLE cards ADD COLUMN created_at TIMESTAMP
    ''')
]
