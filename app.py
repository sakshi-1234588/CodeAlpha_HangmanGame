from flask import Flask, render_template, request, session, redirect, url_for
import random
import string

app = Flask(__name__)
app.secret_key = "secret123"

# Word list
words = ["python", "hangman", "simple", "coding", "random"]

def new_game():
    word = random.choice(words).upper()
    session['word'] = word
    session['guessed'] = []
    session['attempts'] = 6
    session['wrong_letters'] = []

@app.route("/", methods=["GET", "POST"])
def index():
    if 'word' not in session:
        new_game()

    message = ""

    if request.method == "POST":
        letter = request.form['letter'].upper()
        if letter not in session['guessed']:
            session['guessed'].append(letter)
            if letter not in session['word']:
                session['wrong_letters'].append(letter)
                session['attempts'] -= 1

        if all(ch in session['guessed'] for ch in session['word']):
            message = "🎉 You Won!"
        elif session['attempts'] <= 0:
            message = f"💀 Game Over! Word was {session['word']}"

    display_word = [ch if ch in session['guessed'] else "_" for ch in session['word']]
    letters = list(string.ascii_uppercase)

    return render_template(
        "index.html",
        display_word=display_word,
        attempts=session['attempts'],
        wrong=session['wrong_letters'],
        letters=letters,
        message=message
    )

@app.route("/reset")
def reset():
    new_game()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
