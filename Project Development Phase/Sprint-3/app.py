from flask import *
import mysql.connector

app=Flask(__name__)
app.secret_key = "69420"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success")
def success():
    return render_template('success.html',username=session['username'])

@app.route("/jobfeed")
def jobfeed():
    return render_template('joblist.html')

@app.route("/zoho")
def zoho():
    return render_template('zoho.html')

@app.route("/mindtree")
def mindtree():
    return render_template('mindtree.html')

@app.route("/virtusa")
def virtusa():
    return render_template('virtusa.html')

@app.route("/mindtree1")
def mindtree1():
    return render_template('mindtree1.html')

@app.route("/byteridge")
def byteridge():
    return render_template('Byteridge.html')

@app.route("/parallel")
def parallel():
    return render_template('parallel.html')

@app.route("/lg")
def lg():
    return render_template('lg.html')

@app.route("/binance")
def binance():
    return render_template('binance.html')


@app.route("/teleperformane")
def tele():
    return render_template('teleperfomance.html')

@app.route("/hp")
def hp():
    return render_template('hp.html')

@app.route("/visionnet")
def visionnet():
    return render_template('visionnet.html')


@app.route("/ntt")
def ntt():
    return render_template('ntt.html')

@app.route("/Queries")
def contact():
    return render_template('contactus.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/clients")
def clients():
    return render_template('clients.html')

@app.route('/login', methods=('GET', 'POST'))
def signin():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = mysql.connector.connect(host="localhost",user="root",password="Goutham17",database="user",port="3306",auth_plugin='mysql_native_password')
        cur=db.cursor()
        user = cur.execute('SELECT * FROM reg WHERE username = %s AND password =%s', (username,password ))
        record=cur.fetchone()
        
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('jobfeed'))
        else:
            error='Incorrect username/password.Try again!!'
    return render_template('login.html', title='Sign In', error=error)



@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect(url_for('home'))
    

@app.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        db = mysql.connector.connect(host="localhost",user="root",password="Goutham17",database="user",port="3306",auth_plugin='mysql_native_password')
        curr = db.cursor()
        
        curr.execute( "INSERT INTO reg (username, password, email, name) VALUES (%s, %s, %s, %s);", (username, password, email, name) )
        db.commit()
        curr.close()
        db.close()
        return render_template('index.html', title="Home", succ="Registration Successfull!")
    return render_template('register.html', title='Sign Up')


@app.route('/forget', methods=('POST', 'GET'))

def forget():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
       
        db = mysql.connector.connect(host="localhost",user="root",password="Goutham17",database="user",port="3306",auth_plugin='mysql_native_password')
        curr = db.cursor()
        
        curr.execute( "UPDATE reg SET password=%s WHERE name = %s",(password,name,) )
        db.commit()
        curr.close()
        db.close()
        return render_template('index.html', title="login", succ="password Changed Successfull!")
    return render_template('forgetpass.html', title='Sign Up')



if(__name__=='__main__'):
    app.run(debug=True)
