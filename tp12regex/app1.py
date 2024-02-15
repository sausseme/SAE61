# app.py

from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/')
def index():
    # Redirection vers la page de création d'un nouvel utilisateur
    return redirect(url_for('new_user'))

@app.route('/newuser/', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        username = request.form['username']
        validation_message = validate_username(username)
        return render_template('result.html', username=username, validation_message=validation_message)
    return render_template('newuser.html')

def validate_username(username):
    # Expression régulière pour valider les critères demandés
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
    if re.match(regex, username):
        return 'Identifiant valide!'
    else:
        return 'L\'identifiant doit contenir au moins 6 caractères, au moins 1 chiffre, une majuscule et une minuscule.'

if __name__ == '__main__':
    app.run(debug=True)