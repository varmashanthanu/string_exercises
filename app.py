from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy as Sql
from sqlalchemy import create_engine
from forms import WordForm, PuzzleForm
import sys
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
HOST = os.environ['HOST']
PORT = os.environ['PORT']
DEBUG = os.environ['DEBUG']

db = Sql(app)

# from models import Word, Puzzle

db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_word', methods=['get', 'post'])
def add_word():
    print(request.method, file=sys.stderr)
    if request.method == 'POST' and request.form:
        print(request.form, file=sys.stderr)
        flash('"'+request.form.get('word')+'" Added')
        form = WordForm()
        return render_template('add_word.html', title='Add Word', form=form)
    else:
        form = WordForm()
        return render_template('add_word.html', title='Add Word', form=form)


@app.route('/build_puzzle/<puzzle_id>', methods=['get'])
@app.route('/build_puzzle', methods=['get', 'post'])
def build_puzzle(puzzle_id=None):
    if request.method == 'POST' and request.form:
        flash('Puzzle Created')
        return render_template('build_puzzle.html', title='Build Puzzle')
    elif puzzle_id:
        flash('fetching puzzle')
        render_template('build_puzzle.html', title='Puzzle Screen')
    else:
        form = PuzzleForm()
    return render_template('build_puzzle.html', title='Build Puzzle', form=form)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=5000, debug=True)
