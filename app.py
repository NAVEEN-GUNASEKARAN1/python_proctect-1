from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Varshini@30'
app.config['MYSQL_DB'] = 'students'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fees', methods=['POST'])
def get_fees():
    roll_num = request.form['roll_num']
    name = request.form['name']
    dob = request.form['dob']

    cursor = mysql.connection.cursor()
    query = "SELECT fees FROM fees WHERE roll_num = %s AND name = %s AND dob = %s"
    cursor.execute(query, (roll_num, name, dob))
    result = cursor.fetchone()

    if result:
        fees = result[0]
        return render_template('index.html', fees=fees)
    else:
        return render_template('index.html', error='No student found')

if __name__ == '__main__':
    app.run(debug=True)
