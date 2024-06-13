import sqlite3

def connect():
    return sqlite3.connect('deck_of_cards.db')

def add_card(code, image, value, suit):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cards (code, image, value, suit) VALUES (?, ?, ?, ?)', (code, image, value, suit))
    conn.commit()
    conn.close()

def get_all_cards():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cards ORDER BY created_at DESC')
    cards = cursor.fetchall()
    conn.close()
    return cards

def get_card_by_id(card_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cards WHERE id = ?', (card_id,))
    card = cursor.fetchone()
    conn.close()
    return card

def update_card(card_id, code, image, value, suit):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE cards SET code = ?, image = ?, value = ?, suit = ? WHERE id = ?', (code, image, value, suit, card_id))
    conn.commit()
    conn.close()

def delete_card(card_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cards WHERE id = ?', (card_id,))
    conn.commit()
    conn.close()

def add_new_cards(cards):
    conn = connect()
    cursor = conn.cursor()

    for card in cards:
        code = card['code']
        image = card['image']
        value = card['value']
        suit = card['suit']

        cursor.execute('''
            INSERT INTO cards (code, image, value, suit) 
            VALUES (?, ?, ?, ?)
        ''', (code, image, value, suit))

    conn.commit()
    conn.close()