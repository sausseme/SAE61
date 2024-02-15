from flask import Flask, render_template, request, redirect, url_for, flash
import re
import hashlib
import pymysql

app = Flask(__name__)
app.secret_key = 'MQjdqzp6sdçàà(fgf@-2ldcx' 

# Connexion à la base de données
conn = pymysql.connect(
    host='localhost',
    port=3307,  # Modifier le port si nécessaire
    user='root',
    password='foo',
    database='demosql',
    cursorclass=pymysql.cursors.DictCursor
)
@app.route('/')
def index():
    # Redirection vers la page de création d'un nouvel utilisateur
    return redirect(url_for('new_user'))

@app.route('/newuser/', methods=['GET', 'POST'])
def new_user():
    error = None
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validation de l'e-mail avec regex
        email_regex = r'^[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
        if not re.match(email_regex, email):
            error = "L'adresse e-mail n'est pas valide."

        # Validation du mot de passe avec regex
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
        if not re.match(regex, password):
            error = "Le mot de passe doit contenir au moins 6 caractères, dont au moins une majuscule, une minuscule et un chiffre."

        # Vérifier si l'utilisateur existe déjà dans la base de données
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            existing_user = cursor.fetchone()

        if existing_user:
            error = "L'identifiant ou l'adresse e-mail est déjà utilisé."

        # Si aucune erreur n'est détectée, continuer le processus d'inscription
        if error is None:
            # Ajouter l'utilisateur à la base de données
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO users (username, email, MDP) VALUES (%s, %s, %s)", (username, email, hashed_password))
                conn.commit()
            return render_template('success.html', username=username)
    
    return render_template('newuser.html', error=error)

@app.route('/confirmation/<username>')
def confirmation(username):
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
