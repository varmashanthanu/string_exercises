from app import db
from models import Word


def add_single_word(word, category):
    if Word.query.filter_by(name=word).first():
        return 'Word already exists'
    letters = list(word)
    letters.sort()
    letters = ''.join(letters)
    anagrams = Word.query.filter_by(letters=letters).all()
    if anagrams:
        for anagram in anagrams:
            db.session.delete(anagram)
        db.session.commit()
        return 'An anagram for this word exists'
    length = len(word)
    new_word = Word(name=word, length=length, category=category, letters=letters)
    db.session.add(new_word)
    db.session.commit()
    return '"'+word+'" has been added.'


def add_from_file():
    return 202
