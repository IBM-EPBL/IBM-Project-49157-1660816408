from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app=Flask(__name__)
app.secret_key = "69420"


def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route("/")

def home():
    return render_template('home.html')
@app.route("/welcome")

def welcome():
    return render_template('welcome.html')

@app.route('/signin', methods=('GET', 'POST'))
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT password FROM users WHERE username = ?', (username, )).fetchone()
        
        if user is None:
            error = 'Incorrect Username/Password.'
        elif password != user['password']:
            print(user)
            error = 'Incorrect Password.'

        if error is None:
            return redirect(url_for('welcome'))
        flash(error)
        db.close()

    return render_template('login.html', title='Sign In', error=error)


    
@app.route('/signup', methods=('POST', 'GET'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        db = get_db()
        curr = db.cursor()
        
        curr.execute(
            'INSERT INTO users (username, password, email, name) VALUES (?, ?, ?, ?);', (username, password, email, name)
        )
        db.commit()
        curr.close()
        db.close()
        return render_template('home.html', title="Home", succ="Registration Successfull!")
    return render_template('register.html', title='Sign Up')

@app.route('/about')

def about():
    return render_template('about.html')

if(__name__=='__main__'):
    app.run(debug=True)
    