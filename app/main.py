import httpx
from prefect import flow, task
from flask import Flask, render_template, request, redirect, url_for
from app.database import add_card, add_new_cards, get_all_cards,get_card_by_id, update_card, delete_card

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
