from flask import Flask, render_template, request, make_response
from passwordGen import genPassword
import random, string

users = {}

app = Flask(__name__)

def getUID():
	return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

@app.route("/", methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		name=request.form['name']
		print name
 
		if form.validate():
			# Save the comment here.
			flash('Hello ' + name)
		else:
			flash('All the form fields are required. ')
	
	thisUser = {
		"p1":genPassword(),
		"p2":genPassword(),
		"p3":genPassword()
	}

	uid = getUID()
	
	response = make_response(render_template('password.html', p1=thisUser['p1'], p2=thisUser['p2'], p3=thisUser['p3']))
	response.set_cookie('uid', uid)
	return response

@app.route("/verify", methods=['POST'])
def verify():

	print request.args.get("test")
	return 1

if __name__ == "__main__":
	# App config.
	app.config.from_object(__name__)

	#Allows server to be hosted externally
	app.run(host='0.0.0.0')
	app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
	app.jinja_env.globals.update(genPassword=genPassword)
