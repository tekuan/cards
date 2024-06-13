import os
import sqlite3
from yoyo import read_migrations, get_backend

db_path = 'deck_of_cards.db'
migrations_dir = 'migrations'

if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    conn.close()

backend = get_backend(f'sqlite:///{db_path}')

migrations = read_migrations('migrations')
with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))

print("Migrações aplicadas com sucesso!")
