from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import os

app =Flask(__name__)

#Configure db
db = yaml.safe_load(open('db.yaml'))
flask_env = os.environ.get('ENV')
mysql_host = os.environ['MYSQL_HOST']
app.config['MYSQL_HOST'] = mysql_host
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	ip_address = request.remote_addr
    # return "Requester IP: " + ip_address

	if request.method == 'POST':
		userDetails = request.form
		name = userDetails['name']
		email = userDetails['email']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
		mysql.connection.commit()
		cur.close()	
		#return 'success'
		return redirect('/users')
	return render_template('index.html', ipDetails=ip_address, flaskEnv = flask_env, mysqlHost=mysql_host)
	
@app.route('/users')
def users():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM users")
	if resultValue > 0:
		userDetails = cur.fetchall()
		return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


