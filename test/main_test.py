import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app.main import get_deck_cards_data, get_deck_id_data, get_new_card

def test_get_deck_id_data():
    deck_id = get_deck_id_data()
    assert isinstance(deck_id, str)
    assert len(deck_id) > 0        

def test_get_deck_cards_data():
    deck_id = get_deck_id_data()
    cards = get_deck_cards_data(deck_id)
    assert isinstance(cards, list)
    assert len(cards) == 2

def test_get_new_card():
    cards = get_new_card()
    assert isinstance(cards, list)
    assert len(cards) == 1

