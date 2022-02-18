from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import yaml
import os

app =Flask(__name__)

db_str = yaml.safe_load(open('db.yaml'))

#mysql://username:password@server/db
SQLALCHEMY_DATABASE_URI = 'mysql://akhil:password@x.x.x.x:3306/flaskapp'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
mysql_host=db_str['mysql_host']

# SQLALCHEMY_DATABASE_URI = 'mysql://'+db_str['mysql_user']+':'+db_str['mysql_password']+'@'+db_str['mysql_host']+'/'+db_str['mysql_db']

#app.config['SQLALCHEMY_BINDS'] = {
#   'worker': 'mysql://akhil:Avengers123@54.147.44.42:3306/flaskapp'
#}
#db.Model_R = db.make_declarative_base()

#Create db model
class usersflask(db.Model):
	name = db.Column(db.String(20))
	email = db.Column(db.String(40),primary_key=True)

#class usersflask(db.Model_R):
#	name = db.Column(db.String(20))
#	email = db.Column(db.String(40),primary_key=True)
	
flask_env = "testing"

# mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	ip_address = request.remote_addr
    # return "Requester IP: " + ip_address

	if request.method == 'POST':
		userDetails = request.form
		username = userDetails['name']
		useremail = userDetails['email']
		new_user = usersflask(name=username,email=useremail)

		#push to database
		try:
			db.session.add(new_user)
			db.session.commit()
		#return 'success'
			return redirect('/users')
		# except:
		# 	return "There was an error adding your users...."
		except Exception as e:
			return str(e)
	return render_template('index.html', ipDetails=ip_address, flaskEnv = flask_env, mysqlHost=mysql_host)
	
@app.route('/users')
def users():
	users_qry = usersflask.query.all()
	#print(users_qry)
	return render_template('users.html', userDetails=users_qry)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

