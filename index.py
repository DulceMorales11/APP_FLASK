from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re



app  = Flask(__name__)

app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dulce11042001'
app.config['MYSQL_DB'] = 'taller'

mysql = MySQL(app)



@app.route('/')
def principal():
   return render_template('index.html')

@app.route('/especialidades')
def especialidades():
    especialidades=("medicina general","optometria", "ginecologia", "psicologia", "rayos x")
    return render_template('especialidades.html', especialidades= especialidades)

@app.route('/contactanos')
def contactanos():
   return render_template('contactanos.html')

@app.route('/servicios')
def servicios():
   return render_template('servicios.html')

@app.route('/somos')
def somos():
   return render_template('somos.html')

@app.route ('/login.html', methods=['GET', 'POST'])
def login():
   if request.method == "POST" and 'Email' in request.form and 'Password' in request.form:
        Email = request.form['Email']
        Password = request.form['Password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Usuarios WHERE Email= %s AND Password= %s', (Email, Password, ))
        user = cursor.fetchone()
        if user:
               session['loggedin'] = True
               session['Email'] = user['Email']
               return render_template('index.html')
        else:
            flash("Correo o Contraseñas Incorrectas")
   return render_template('login.html')

   
   

if __name__== '__main__':
    app.run(debug= True, port=4000, host= '0.0.0.0')
    








