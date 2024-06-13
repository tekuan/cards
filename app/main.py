import httpx
from prefect import flow, task
from flask import Flask, render_template, request, redirect, url_for
from app.database import add_card, add_new_cards, get_all_cards,get_card_by_id, update_card, delete_card
import time

app = Flask(__name__)
base_url = "https://deckofcardsapi.com/api/deck/"

@app.route('/')
def index():
    cards = get_all_cards()
    return render_template('index.html', cards=cards)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        code = request.form['code']
        image = request.form['image']
        value = request.form['value']
        suit = request.form['suit']
        add_card(code, image, value, suit)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        code = request.form['code']
        image = request.form['image']
        value = request.form['value']
        suit = request.form['suit']
        update_card(id, code, image, value, suit)
        return redirect(url_for('index'))
    else:
        card = get_card_by_id(id)
        return render_template('update.html', card=card)

@app.route('/delete/<int:id>')
def delete(id):
    delete_card(id)
    return redirect(url_for('index'))

@app.route('/new/card')
def new_card():
    cards = get_new_card()
    add_new_cards(cards)
    return redirect(url_for('index'))

@flow
def get_new_card():
    deck_id = get_deck_id_data()
    cards = get_deck_cards_data(deck_id, 1)
    return cards


@task(retries=3, retry_delay_seconds=5)
def get_deck_id_data():
    url = base_url + "new/shuffle/?deck_count=1"
    response = httpx.get(url)
    response.raise_for_status()
    res = response.json()
    return res['deck_id']

@task
def get_deck_cards_data(deck_id, count = 2):
    url = base_url + deck_id + "/draw/?count=" + str(count)
    response = httpx.get(url)
    response.raise_for_status()
    res = response.json()
    return res['cards']

@flow
def get_deck_data():
    deck_id = get_deck_id_data()
    cards = get_deck_cards_data(deck_id)
    add_new_cards(cards)

if __name__ == '__main__':
    get_deck_data()    
    app.run(debug=True)